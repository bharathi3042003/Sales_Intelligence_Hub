import streamlit as st
from db import get_connection

def show_dashboard():
    st.title("Dashboard")

    conn = get_connection()
    cur = conn.cursor()

   # cur.execute("SELECT SUM(gross_sales), SUM(received_amount), SUM(pending_amount) FROM customer_sales")
    if st.session_state["role"] == "Admin":
        cur.execute("""
        SELECT SUM(gross_sales), SUM(received_amount), SUM(pending_amount)
        FROM customer_sales
        WHERE branch_id = %s
        """, (st.session_state["branch_id"],))
    else:
        cur.execute("""
        SELECT SUM(gross_sales), SUM(received_amount), SUM(pending_amount)
        FROM customer_sales
        """)
    data = cur.fetchone()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", data[0])
    col2.metric("Received", data[1])
    col3.metric("Pending", data[2])
    cur.execute  ('''
select status, count(*) from customer_sales
      group by status    
''')
    data_open= cur.fetchone()
    
    col1 = st.columns(1)

    st.write("open sales ", data_open)

    cur.execute ('''
    SELECT * FROM customer_sales WHERE pending_amount > 5000;
''')
    sales_5000= cur.fetchone()
    st.write("sales that has pending_amount>5000 ", sales_5000)
    conn.close()