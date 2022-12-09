import streamlit as st
import pandas as pd
import config as cfg
from datetime import datetime, date
from numpy import insert

from func_lib import (
    get_coord,
    get_data,
    get_county_key,
    get_state_key,
    filter_data_by_county_state,
)
from graphs import (
    draw_tot_cases_graph,
    draw_tot_deaths_graph,
    draw_county_state_cases_graph,
    draw_county_state_deaths_graph,
    draw_daily_cases_graph,
    draw_daily_deaths_graph,
    draw_daily_county_state_cases_graph,
    draw_daily_county_state_deaths_graph,
)


covid_data = get_data()




nav_disease_link = st.sidebar.radio("Trang chủ", ("Thông tin", "Dashboard"))

# main nav
if nav_disease_link == "Thông tin":
    nav_link = 1
   
    st.header(
        "ĐẠI DỊCH COVID-19 TẠI HOA KỲ "
    )
    html_img2 = '''<img src="https://muonglat.thanhhoa.gov.vn/portal/Photos/2022-06/14e123649f6082bdCoronavirus-COVID-19.jpg" width="700" height="400">'''
    st.markdown(html_img2,unsafe_allow_html=True)
    html1 = "<br>Trường hợp đầu tiên được xác nhận về sự bùng phát đại dịch toàn cầu của bệnh virus corona 2019 (COVID-19) tại Hoa Kỳ đã được công bố vào ngày 21 tháng 1 năm 2020. Các ca nhiễm bệnh đã được xác nhận ở tất cả 50 tiểu bang của Hoa Kỳ, quận Columbia và tất cả các vùng lãnh thổ hải ngoại của Hoa Kỳ.[3] Tính đến ngày 31 tháng 12 năm 2021, Hoa Kỳ có số ca nhiễm bệnh và tổng số ca tử vong nhiều nhất thế giới do virus này,[4] với bang New York là trung tâm của dịch bệnh với hơn một nửa số ca.[5] </br>"
    st.markdown(html1,unsafe_allow_html=True)
    html2 = '''<br>Ca đầu tiên nhiễm COVID-19 được biết đến ở Hoa Kỳ đã được xác nhận ngày 20 tháng 1 năm 2020, ở một người phụ nữ 35 tuổi đã trở về từ Vũ Hán, Trung Quốc năm ngày trước đó.. Lực lượng đặc nhiệm coronavirus của Nhà Trắng được thành lập vào ngày 29 tháng 1.] Hai ngày sau, chính quyền Donald Trump đã tuyên bố tình trạng khẩn cấp y tế công cộng và tuyên bố hạn chế đối với du khách đến từ Trung Quốc. Vào ngày 26 tháng 2, trường hợp đầu tiên ở Mỹ ở một người "không biết phơi nhiễm với virus thông qua du lịch hoặc tiếp xúc gần gũi với một người nhiễm bệnh đã biết" đã được xác nhận bởi Trung tâm kiểm soát và phòng ngừa dịch bệnh (Centers for Disease Control, viết tắt là CDC) tại Bắc California. </br>'''
    st.markdown(html2,unsafe_allow_html=True)
    html3 = '''<br>Kể từ ngày 24 tháng 2 năm 2020, Trung tâm Kiểm soát và Phòng ngừa Dịch bệnh đã xác nhận 76 trường hợp nhiễm virus corona tại Hoa Kỳ. CDC công bố các thông số mới vào mỗi thứ Hai, thứ Tư và thứ Sáu, báo cáo một số loại trường hợp: du khách cá nhân, người mắc bệnh từ những người khác ở Hoa Kỳ và công dân hồi hương từ các địa điểm khủng hoảng, như tàu du lịch Vũ Hán và Diamond Princess.[9]</br>'''
    st.markdown(html3,unsafe_allow_html=True)
    html4 = '''<br>Từ tháng 1 đến giữa tháng 3, Hoa Kỳ đã khởi đầu chậm chạp trong xét nghiệm COVID-19.[10][11] Trong giai đoạn đó, chính phủ liên bang Mỹ đã từ chối các bộ dụng cụ thử nghiệm được sử dụng trên phạm vi quốc tế, đã phát triển bộ dụng cụ thử nghiệm của chính phủ bị lỗi, chỉ bộ dụng cụ thử nghiệm phi chính phủ được phê duyệt từ cuối tháng 2 và có hướng dẫn kiểm tra đủ điều kiện hạn chế cho đến đầu tháng 3.[10][11] Tiếp theo đó là việc chính phủ công bố một loạt các biện pháp nhằm tăng tốc độ xét nghiệm. Tính đến ngày 20 tháng 3, 100.000 bài kiểm tra đã được tiến hành, nhưng vẫn chưa đủ.[12] Các công ty tư nhân đã bắt đầu gửi hàng trăm ngàn thử nghiệm. Các trạm kiểm tra lái xe đang bắt đầu trên toàn quốc.[12] CDC cảnh báo rằng việc lây truyền rộng rãi có thể buộc một số lượng lớn người phải nhập viện và chăm sóc sức khỏe khác, khiến các hệ thống chăm sóc sức khỏe quá tải.[13] Kể từ ngày 19 tháng 3 năm 2020, Bộ Ngoại giao Hoa Kỳ đã khuyên công dân Hoa Kỳ tránh tất cả các chuyến du lịch quốc tế.[14] Chính phủ Hoa Kỳ đã khuyên không nên tập hợp hơn 10 người.[15]</br>'''
    st.markdown(html4,unsafe_allow_html=True)
    html5 = '''<br>Sau giữa tháng 3 năm 2020, Chính phủ Liên bang đã thực hiện một thay đổi đáng kể tất nhiên là sử dụng quân đội Hoa Kỳ để khởi xướng và nỗ lực phát triển nhanh chóng các cơ sở chăm sóc đặc biệt COVID-19 toàn quốc. Công binh Lục quân Hoa Kỳ, dưới quyền lực pháp lý hiện có đến từ Quốc hội ủy quyền và quyền hạn của Fema, sẽ nhanh chóng cho thuê một số lượng lớn các tòa nhà trên khắp Hoa Kỳ trong các khách sạn và tại một tòa nhà mở lớn hơn để ngay lập tức tăng số lượng phòng và giường với khả năng ICU cho bệnh nhân của đại dịch coronavirus năm 2020, theo một cuộc họp ngắn vào tháng 3 & nbsp; 20. Quân đoàn Kỹ sư sẽ xử lý cho thuê và kỹ thuật, với các hợp đồng sửa đổi và thiết lập cơ sở nhanh chóng được cấp cho các nhà thầu địa phương. Kế hoạch dự kiến rằng hoạt động của các cơ sở và cung cấp nhân viên y tế sẽ được xử lý hoàn toàn bởi các tiểu bang Hoa Kỳ chứ không phải chính phủ Liên bang.[16]</br>'''
    st.markdown(html5,unsafe_allow_html=True)
    html6 = '''<br>Tính đến 12 tháng Bảy năm 2020, Hoa Kỳ có 3.236.130 ca nhiễm, trong đó 134.572 ca tử vong. Tâm dịch các bang: New York 402.561 ca (riêng thành phố New York 220.242 ca, các nơi khác 182.319 ca; các hạt / quận nhiều ca: Queens 66.323 ca; Kings 60.647 ca; Bronx 48.267 ca; Nassau 42.267 ca; Suffolk 41.987 ca;...); California 312.344 ca (các hạt / quận nhiều ca: Los Angeles 130.242 ca; Riverside 25.481 ca; Orange 23.901 ca; San Diego 19.371 ca; San Bernardino 18.912 ca;...); Florida 250.984 ca (Miami-Dade: 60.868 ca; Broward 28.253 ca; Palm Beach 19.847 ca; Hillsborough 18.360 ca; Orange 16.630 ca;...); Texas 250.462 ca (Harris 42.000 ca; Dallas 31.525 ca; Bexar 18.602 ca; Tarrant 17.334 ca;...); New Jersey 174.959 ca (Bergen 19.847 ca; Hudson 19.089 ca; Essex: 18.988 ca; Passaic 17.050 ca;...); Illinois 154.094 ca (Cook 95.138 ca; Lake 10.318 ca;...); Arizona 119.930 ca (Maricopa 78.481 ca; Pima 11.443 ca;...); Georgia 114.401 ca (Gwinnett 11.114 ca; Fulton 10.381 ca;...); Massachusetts 111.398 ca (Middlesex 24.436 ca; Suffolk 20.272 ca;...)...</br>'''
    st.markdown(html6,unsafe_allow_html=True)
    html7 = '''<br>Ngày 2 tháng 10, tổng thống Donald Trump tiết lộ trên Twitter rằng cả ông và Đệ Nhất Phu nhân Hoa Kỳ Melania Trump cùng cố vấn Hope Hicks có kết quả dương tính với COVID-19.[18][19][20]
Kể từ khi đại dịch covid lan sang Hoa Kỳ, quốc gia này đã phải đối mặt với một số khó khăn như số người mắc covid cũng như số người tử vong do dịch bệnh này cao. Nguyên nhân là do sự phản ứng chậm trễ của Tổng thống Donald Trump. Tuy nhiên, sang đến năm sau, nhờ sự nỗ lực của tân Tổng thống Joe Biden cũng như Chính quyền liên bang, cùng với đó là sự ra đời của các loại vaccine nên tình hình dịch bệnh cơ bản đã được kiểm soát.
</br>'''
    st.markdown(html7,unsafe_allow_html=True)
elif nav_disease_link == "Dashboard":
    nav_link = st.sidebar.radio("COVID-19 DASHBOARD", ( "Toàn nước Mỹ", "Từng khu vực"))
    st.header(
        " COVID-19 DASHBOARD"
    )
    html_img2 = '''<img src="https://muonglat.thanhhoa.gov.vn/portal/Photos/2022-06/14e123649f6082bdCoronavirus-COVID-19.jpg" width="700" height="400">'''
    st.markdown(html_img2,unsafe_allow_html=True)

elif nav_disease_link == "Zika":
    nav_link = st.sidebar.radio("COVID-19 DASHBOARD", ("Graphs"))
    st.header(
        "Exploring Zika in the US. "
    )

# covid
if nav_link == "Thông tin":
    st.header(
        "Resources:"
    )

elif nav_link == "Toàn nước Mỹ":
    draw_tot_cases_graph(covid_data)
    draw_tot_deaths_graph(covid_data)
    draw_daily_cases_graph(covid_data)
    draw_daily_deaths_graph(covid_data)

elif nav_link == "Từng khu vực":
    cov_coord = get_coord(covid_data)
    

    state_key = get_state_key(cov_coord)
    # state_key = insert(state_key, 0, "All")
    st.sidebar.header(f"Chọn một tiểu bang dưới đây:")
    state = st.sidebar.selectbox("Chọn một bang: ", state_key)
    st.sidebar.header(f"Chọn một hạt dưới đây:")
    county_key = get_county_key(cov_coord, state)
    county_key = insert(county_key, 0, "All")
    county = st.sidebar.selectbox("Chọn một hạt: ", county_key)

    st_co_data = filter_data_by_county_state(covid_data, county, state)

    if not st_co_data.empty:
        draw_county_state_cases_graph(st_co_data, county, state)
        draw_county_state_deaths_graph(st_co_data, county, state)
        draw_daily_county_state_cases_graph(st_co_data, county, state)
        draw_daily_county_state_deaths_graph(st_co_data, county, state)
        # date_to_filter = st.date_input(
        #     "Check for date",
        #     datetime.strptime(cfg.default_date_for_map, "%Y-%m-%d").date(),
        # )
    else:
        st.write("This combination will not work")
