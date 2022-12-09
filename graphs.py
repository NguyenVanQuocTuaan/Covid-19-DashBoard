import streamlit as st


def draw_tot_cases_graph(df):
    tot_cases_by_day = df.groupby("date")["cases"].sum()
    st.write("Tổng số trường hợp (Hoa Kỳ):")
    st.line_chart(tot_cases_by_day)


def draw_daily_cases_graph(df):
    cases_by_day = df.groupby("date")["cases"].sum().reset_index(name="cases")
    shifted = cases_by_day["cases"].shift(1)
    cases_by_day["daily_cases"] = cases_by_day["cases"] - shifted
    cases_by_day.drop(columns=["cases"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write("Các trường hợp hàng ngày (Hoa Kỳ):")
    st.bar_chart(cases_by_day)


def draw_tot_deaths_graph(df):
    tot_cases_by_day = df.groupby("date")["deaths"].sum()
    st.write("Các trường hợp tử vong(Hoa Kỳ):")
    st.line_chart(tot_cases_by_day)


def draw_daily_deaths_graph(df):
    cases_by_day = df.groupby("date")["deaths"].sum().reset_index(name="deaths")
    shifted = cases_by_day["deaths"].shift(1)
    cases_by_day["daily_deaths"] = cases_by_day["deaths"] - shifted
    cases_by_day.drop(columns=["deaths"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write("Các trường hợp tử vong hàng ngày(Hoa Kỳ):")
    st.bar_chart(cases_by_day)


def draw_county_state_cases_graph(df, co, state):
    county_state_cases_by_day = df.groupby("date")["cases"].sum()
    st.write(f"Tổng số trường hợp({co}, {state}):")
    st.line_chart(county_state_cases_by_day)


def draw_daily_county_state_cases_graph(df, co, state):
    cases_by_day = df.groupby("date")["cases"].sum().reset_index(name="cases")
    shifted = cases_by_day["cases"].shift(1)
    cases_by_day["daily_cases"] = cases_by_day["cases"] - shifted
    cases_by_day.loc[cases_by_day.daily_cases < 0, "daily_cases"] = 0
    cases_by_day.drop(columns=["cases"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write(f"Các trường hợp hàng ngày({co}, {state}):")
    st.bar_chart(cases_by_day)


def draw_county_state_deaths_graph(df, co, state):
    county_state_deaths_by_day = df.groupby("date")["deaths"].sum()
    st.write(f"Các trường hợp tử vong({co}, {state}):")
    st.line_chart(county_state_deaths_by_day)


def draw_daily_county_state_deaths_graph(df, co, state):
    cases_by_day = df.groupby("date")["deaths"].sum().reset_index(name="deaths")
    shifted = cases_by_day["deaths"].shift(1)
    cases_by_day["daily_deaths"] = cases_by_day["deaths"] - shifted
    cases_by_day.loc[cases_by_day.daily_deaths < 0, "daily_deaths"] = 0
    cases_by_day.drop(columns=["deaths"], axis=1, inplace=True)
    cases_by_day.set_index("date", inplace=True)
    st.write(f"Các trường hợp tử vong hàng ngày({co}, {state}):")
    st.bar_chart(cases_by_day)

