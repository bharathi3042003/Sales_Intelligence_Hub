import streamlit as st
import pandas as pd
from db import get_connection

def show_reports():
    st.title("Sales Report")

    conn = get_connection()

   # query = "SELECT * FROM customer_sales"
    if st.session_state["role"] == "Admin":
     query = f"""
        SELECT * FROM customer_sales
        WHERE branch_id = {st.session_state['branch_id']}
        """
    else:
        query = "SELECT * FROM customer_sales"
    df = pd.read_sql(query, conn)

    st.dataframe(df)

    conn.close()