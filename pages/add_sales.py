import streamlit as st
from db import get_connection

def add_sales():
    st.title("Add Sales")

    name = st.text_input("Customer Name")
    mobile = st.text_input("Mobile Number")
    product = st.selectbox("Product", ["DS", "DA", "BA", "FSD"])
    gross = st.number_input("Gross Sales")

    if st.button("Submit"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO customer_sales 
            (branch_id, date, name, mobile_number, product_name, gross_sales, received_amount, status)
            VALUES (%s, CURRENT_DATE, %s, %s, %s, %s, 0, 'Open')
        """, (st.session_state["branch_id"], name, mobile, product, gross))

        conn.commit()
        conn.close()

        st.success("Sales added successfully")