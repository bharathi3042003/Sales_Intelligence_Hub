import streamlit as st
from auth import login

st.set_page_config(page_title="Sales Dashboard")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    st.sidebar.title("Menu")

    page = st.sidebar.radio("Go to", [
        "Dashboard",
        "Add Sales",
        "Add Payment",
        "Reports"
    ])

    if page == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()

    elif page == "Add Sales":
        from pages.add_sales import add_sales
        add_sales()

    elif page == "Add Payment":
        from pages.payments import add_payment
        add_payment()

    elif page == "Reports":
        from pages.reports import show_reports
        show_reports()