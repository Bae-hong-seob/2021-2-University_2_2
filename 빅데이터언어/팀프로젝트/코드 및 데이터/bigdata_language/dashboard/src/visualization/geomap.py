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
