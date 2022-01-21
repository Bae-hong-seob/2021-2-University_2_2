import pandas as pd


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
