import streamlit as st
from db import get_connection

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT user_id, role, branch_id 
            FROM users 
            WHERE username=%s AND password=%s
        """, (username, password))

        user = cur.fetchone()

        if user:
            st.session_state["logged_in"] = True
            st.session_state["role"] = user[1]
            st.session_state["branch_id"] = user[2]
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

        conn.close()