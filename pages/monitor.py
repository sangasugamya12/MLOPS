import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from auth import login

# 🔧 Set page config first
st.set_page_config(page_title="📉 Drift Monitoring", layout="centered")

# 🔐 Auth Check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("🔐 You must be logged in to view this page.")
    st.stop()

# 🧭 Title
st.title("📉 Model Drift Monitoring Dashboard")

# 🔍 Path to logs
log_path = "logs/metrics_log.csv"

# 🔒 Check log file
if not os.path.exists(log_path) or os.path.getsize(log_path) == 0:
    st.warning("⚠️ No training logs found yet. Please train the model first.")
    st.stop()

# 📄 Load logs
try:
    logs_df = pd.read_csv(log_path)
    logs_df["timestamp"] = pd.to_datetime(logs_df["timestamp"])
    logs_df["run"] = range(1, len(logs_df) + 1)
except Exception as e:
    st.error(f"❌ Failed to read or parse log file: {e}")
    st.stop()

# 🧾 Recent Logs
st.subheader("🧾 Recent Training Runs")
st.dataframe(logs_df.tail(5), use_container_width=True)

# 🚨 Drift Detection
latest_r2 = logs_df.iloc[-1]["r2_score"]
if latest_r2 < 0.75:
    st.error(f"⚠️ Drift Detected! R² has dropped to {latest_r2:.2f}")
else:
    st.success(f"✅ Latest R² is {latest_r2:.2f} — No drift detected.")

# 📈 R² Score Trend
st.subheader("📊 R² Score Over Time")
fig, ax = plt.subplots()
ax.plot(logs_df["run"], logs_df["r2_score"],
        marker="o", color="blue", label="R² Score")
ax.set_xlabel("Training Run")
ax.set_ylabel("R² Score")
ax.set_title("📈 R² Score Trend")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# 📉 MSE Trend
st.subheader("📊 MSE Over Time")
fig2, ax2 = plt.subplots()
ax2.plot(logs_df["run"], logs_df["mse"], marker="x", color="red", label="MSE")
ax2.set_xlabel("Training Run")
ax2.set_ylabel("Mean Squared Error (MSE)")
ax2.set_title("📉 MSE Trend")
ax2.grid(True)
ax2.legend()
st.pyplot(fig2)

# 📁 Full Log Viewer
with st.expander("📁 Show Full Log Data"):
    st.dataframe(logs_df, use_container_width=True)