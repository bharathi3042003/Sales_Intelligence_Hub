import streamlit as st
from db import get_connection

def add_payment():
    st.title("Add Payment")

    sale_id = st.number_input("Sale ID")
    amount = st.number_input("Amount Paid")
    method = st.selectbox("Method", ["Cash", "UPI", "Card"])

    if st.button("Add Payment"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO payment_splits (sale_id, payment_date, amount_paid, payment_method)
            VALUES (%s, CURRENT_DATE, %s, %s)
        """, (sale_id, amount, method))

        conn.commit()
        conn.close()

        st.success("Payment added")