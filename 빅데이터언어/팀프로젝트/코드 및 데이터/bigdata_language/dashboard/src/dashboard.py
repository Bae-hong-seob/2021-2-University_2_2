import matplotlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
from matplotlib.backends.backend_agg import RendererAgg
from streamlit_folium import folium_static
import folium


def draw_data(x, color, seouls):
    # 서울시 행정구역 json 불러오기
    state_geo = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"
    m = folium.Map(
        location=[37.562225, 126.978555],
        width="100%",
        height="100%",
        zoom_start=11,
    )

    folium.Choropleth(
        geo_data=state_geo,
        #         name=x,
        data=seouls,
        columns=["행정구역별(2)", x],
        key_on="feature.properties.name",
        fill_color=color,
        fill_opacity=0.9,
        line_opacity=0.6,
        legend=True,
        legend_name=x,
    ).add_to(m)

    return m



# 날짜를 datetime형식으로 바꾼 뒤 index로 설정하는 함수적용
def date(df: pd.DataFrame) -> pd.DataFrame:
    df["Unnamed: 0"] = pd.to_datetime(df["Unnamed: 0"], format="%Y-%m-%d")
    df.rename(columns={"Unnamed: 0": "날짜"}, inplace=True)
    df.set_index("날짜", inplace=True)
    return df


# 해당 지역만을 리스트로 가져오는 함수
def location(name):
    name = [
        "종합-" + name + "[2017.11=100]",
        "아파트-" + name + "[2017.11=100]",
        "연립다세대-" + name + "[2017.11=100]",
        "단독주택-" + name + "[2017.11=100]",
    ]
    return name


def load_dataset(path):
    # 제공 데이터
    c_permit = pd.read_csv(path + "건축허가현황.csv")  # Construction_Permision
    order = pd.read_csv(path + "국내건설수주액.csv")  # Domestic construction Order Amount
    unsold = pd.read_csv(path + "미분양주택현황.csv")  # Unsold housing status
    apt_price = pd.read_csv(
        path + "아파트 실거래가격지수.csv"
    )  # Actual transaction price index of apartments
    monthly = pd.read_csv(
        path + "유형별_주택월세통합가격지수.csv"
    )  # House Monthly Rent Integrated Price Index
    h_permit = pd.read_csv(
        path + "주택건설인허가실적.csv"
    )  # Housing construction permission result
    house_price = pd.read_csv(path + "주택매매가격지수(KB).csv")  # Housing Price Index
    lease_price = pd.read_csv(path + "주택전세가격지수(KB).csv")  # Housing Lease Price Index
    land_price = pd.read_csv(path + "지역별_지가변동률.csv")  # Land Price Variation Rate
    df_list = [
        c_permit,
        order,
        unsold,
        apt_price,
        monthly,
        h_permit,
        house_price,
        lease_price,
        land_price,
    ]

    for df in df_list:
        date(df)

    return (
        c_permit,
        order,
        unsold,
        apt_price,
        monthly,
        h_permit,
        house_price,
        lease_price,
        land_price,
    )


st.set_page_config(layout="wide")


(
    c_permit,
    order,
    unsold,
    apt_price,
    monthly,
    h_permit,
    house_price,
    lease_price,
    land_price,
) = load_dataset(path="../input/")

matplotlib.use("agg")

_lock = RendererAgg.lock


sns.set_style("darkgrid")

st.title("부동산 가격 분석")


row1_spacer1, row1_1, row1_spacer2 = st.columns((0.1, 3.2, 0.1))

with row1_1:
    st.markdown("부동산 가격 시간 변동")
    st.markdown("**시각화 분석 노트**👇")

line1_spacer1, line1_1, line1_spacer2 = st.columns((0.1, 3.2, 0.1))

with line1_1:
    st.header("Plotly 시각화")

st.write("")
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)


with row3_1, _lock:
    st.subheader("미분양 아파트 현황")
    fig = px.line(unsold)
    st.plotly_chart(fig)

with row3_2, _lock:
    st.subheader("미분양 아파트 전국, 서울, 수도권 분석")
    fig = px.line(unsold[["전국[호]", "서울[호]", "수도권[호]"]])
    st.plotly_chart(fig)
    st.markdown("미분양 주택이 서울과 수도권은 0으로 수렴함을 알 수 있다.")


st.subheader("제공데이터 중 가격관련 데이터 분석")
fig = px.line(apt_price)
fig.update_layout(autosize=True, width=1250, height=500)
st.plotly_chart(fig)


row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)

with row4_1, _lock:
    asc_price = apt_price.loc["2020-01"] > 100
    asc_columns = asc_price[(asc_price[asc_price])].T.dropna().index.tolist()
    st.subheader("기준점 이후 상승세인 지역들")
    fig = px.line(apt_price[asc_columns])
    st.plotly_chart(fig)

with row4_2, _lock:
    dec_price = apt_price.loc["2020-01"] < 100
    dec_columns = dec_price[(dec_price[dec_price])].T.dropna().index.tolist()
    st.subheader("기준점 이후 하락세인 지역들")
    fig = px.line(apt_price[dec_columns])
    st.plotly_chart(fig)


gap_price = (apt_price.loc["2021-01"][asc_columns].values) - (
    apt_price.loc["2018-01"][asc_columns].values
)
gap_df = pd.DataFrame(data=gap_price, columns=asc_columns)
gap_df = gap_df.T.sort_values(by=0, ascending=False)
top_5 = gap_df.iloc[:5]
gap_top5 = top_5.index.tolist()

st.subheader("격차가 큰 상위 5개지역")
fig = px.line(apt_price["2018":][gap_top5])
fig.update_layout(autosize=True, width=1250, height=500)
st.plotly_chart(fig)
st.markdown("세종시는 정부의 방침에 따라 최근 급등하는 모습을 보이며, 서울 또한 상위권을 차지하는 모습을 볼 수 있다.")


st.write("")
row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)

with row5_1, _lock:
    st.subheader("전국 주택월세통합가격지수")
    fig = px.line(monthly[location("전국")])
    st.plotly_chart(fig)


with row5_2, _lock:
    st.subheader("서울 주택월세통합가격지수")
    fig = px.line(monthly[location("서울")])
    st.plotly_chart(fig)

st.subheader("전국과 서울의 아파트 월세 변화")
d_monthly = monthly[["아파트-전국[2017.11=100]", "아파트-서울[2017.11=100]"]]
fig = px.line(d_monthly)
fig.update_layout(autosize=True, width=1250, height=500)
st.plotly_chart(fig)
st.markdown("전국에 비해 서울은 하락폭이 작고 상승폭은 크다")


row6_space1, row6_1, row6_space2, row6_2, row6_space3 = st.columns(
    (0.1, 1, 0.1, 1, 0.1)
)


with row6_1, _lock:
    st.subheader("주택매매가격지수")
    fig = px.line(monthly[location("서울")])
    st.plotly_chart(fig)


with row6_2, _lock:
    st.subheader("2019 5년전후의 총 지수와 아파트만 추출")
    fig = px.line(
        house_price.loc[
            "2014":,
            [
                "총지수[2019.01=100]",
                "아파트[2019.01=100]",
                "아파트(서울)[2019.01=100]",
                "총지수(서울)[2019.01=100]",
            ],
        ]
    )
    st.plotly_chart(fig)

st.subheader("서울시 아파트 가격에 대한 가격자료")
d_seoul = apt_price[["서울[2017.11=100]"]]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=d_seoul.index,
        y=d_seoul["서울[2017.11=100]"],
        mode="lines",
        name="아파트 실거래가",
    )
)

fig.add_trace(
    go.Scatter(
        x=d_monthly.index,
        y=d_monthly["아파트-서울[2017.11=100]"],
        mode="lines",
        name="아파트 월세가",
    )
)

fig.add_trace(
    go.Scatter(
        x=house_price.loc["2006":, :].index,
        y=house_price.loc["2006":, "아파트(서울)[2019.01=100]"],
        mode="lines",
        name="아파트 매매가",
    )
)

fig.add_trace(
    go.Scatter(
        x=lease_price.loc["2006":, :].index,
        y=lease_price.loc["2006":, "아파트(서울)[2019.01=100]"],
        mode="lines",
        name="아파트 전세가",
    )
)

fig.update_layout(autosize=True, width=1250, height=500)
st.plotly_chart(fig)

st.subheader("서울시 아파트 가격에 대한 평균가격지수 지도 시각화")

seouls = pd.read_excel("../input/서울지역별_아파트매매가격지수.xlsx")
seouls.drop(2019.75, axis=1, inplace=True)
seouls["평균가격지수"] = seouls[[2017, 2018, 2019, 2020, 2021]].mean(axis=1)
m = draw_data("평균가격지수", "Blues", seouls)

folium_static(m)
