import streamlit as st
from backend.predict import run_prediction

st.set_page_config(page_title="NIFTY Option Predictor", layout="centered")
st.title("📈 NIFTY Option Predictor")

if st.button("🔮 Predict Now"):
    direction, spot, suggestions = run_prediction()

    st.write(f"**Current NIFTY Spot:** ₹{spot:.2f}")
    st.write(f"**Prediction:** {'📈 UP (Buy CALL)' if direction == 1 else '📉 DOWN (Buy PUT)'}")

    st.subheader("🎯 Recommended Options (Expected gain ₹10+)")
    for s in suggestions:
        st.markdown(f"""
        - **Strike**: ₹{s['strike']} | **Type**: {s['type']}
        - **LTP**: ₹{s['ltp']} → **Target**: ₹{s['target']}
        - **IV**: {s['iv']} | **Delta**: {s['delta']} | **Theta**: {s['theta']}
        ---
        """)
