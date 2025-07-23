# auth.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime


def login():
    st.set_page_config(page_title="🔐 Login", layout="centered")
    st.title("🔐 Secure Login")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("🔓 Login"):
        file_path = "data/users.csv"

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            try:
                users = pd.read_csv(file_path)
                user = users[(users["username"] == username) &
                             (users["password"] == password)]

                if not user.empty:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.role = user.iloc[0]["role"]

                    os.makedirs("logs", exist_ok=True)
                    with open("logs/user_log.csv", "a") as f:
                        f.write(f"{datetime.now()}, {username}, login\n")

                    st.success(f"✅ Welcome, {username}!")
                    st.rerun()

                else:
                    st.error("❌ Invalid username or password.")
            except Exception as e:
                st.error(f"⚠️ Error reading user file: {e}")
        else:
            st.warning("🚫 No registered users found. Please register first.")

    st.markdown("---")
    if st.button("📝 Go to Register Page"):
        try:
            st.switch_page("pages/register.py")
        except Exception:
            st.warning("⚠️ Navigation only works in multipage apps.")

    if st.button("📊 Go to Monitoring Dashboard"):
        try:
            st.switch_page("pages/monitor.py")
        except Exception:
            st.warning("⚠️ Navigation only works in multipage apps.")