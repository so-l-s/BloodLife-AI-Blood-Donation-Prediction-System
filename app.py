import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(
    page_title="BloodLife AI",
    page_icon="🩸",
    layout="wide"
)

st.markdown("""
# 🩸 BloodLife AI

### Predict. Connect. Save Lives.

Helping blood banks identify potential donors using Machine Learning.
""")

st.markdown("---")

tab1, tab2 = st.tabs([
    "Single Donor Prediction",
    "Bulk CSV Prediction"
])

# ===================================
# SINGLE DONOR
# ===================================

with tab1:

    st.header("Single Donor Prediction")

    col1, col2 = st.columns(2)

    with col1:
        recency = st.number_input(
            "Months Since Last Donation",
            min_value=0
        )

        frequency = st.number_input(
            "Total Donations",
            min_value=0
        )

    with col2:
        monetary = st.number_input(
            "Total Blood Donated (cc)",
            min_value=0
        )

        time = st.number_input(
            "Months Since First Donation",
            min_value=0
        )

    if st.button("Predict Donor"):

        prediction = model.predict(
            [[recency,
              frequency,
              monetary,
              time]]
        )

        if prediction[0] == 1:
            st.success(
                "✅ Likely to Donate Blood Again"
            )
        else:
            st.error(
                "❌ Not Likely to Donate"
            )

# ===================================
# BULK PREDICTION
# ===================================

with tab2:

    st.header("Bulk Donor Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        features = df[
            ['Recency',
             'Frequency',
             'Monetary',
             'Time']
        ]

        predictions = model.predict(features)

        df['Prediction'] = predictions

        df['Prediction'] = df[
            'Prediction'
        ].map({
            1: 'Likely',
            0: 'Not Likely'
        })

        st.dataframe(df)

        likely = len(
            df[df['Prediction']
            == 'Likely']
        )

        not_likely = len(
            df[df['Prediction']
            == 'Not Likely']
        )

        st.metric(
            "Total Donors",
            len(df)
        )

        st.metric(
            "Likely Donors",
            likely
        )

        st.metric(
            "Not Likely Donors",
            not_likely
        )

        st.bar_chart(
            pd.DataFrame({
                'Count':
                [likely, not_likely]
            },
            index=[
                'Likely',
                'Not Likely'
            ])
        )
# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "BloodLife AI • Machine Learning Based Blood Donation Prediction System 🩸"
)