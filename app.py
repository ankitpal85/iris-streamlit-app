import streamlit as st
import numpy as np
import pickle
import sklearn

st.set_page_config(
    page_title="Iris Predictor",
    page_icon="Iris",
    layout="centered",
)

st.markdown(
    """
    <style>
    /* Hide top header bar & footer */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }

    .stApp {
        background: #ffffff !important;
        color: #17202a !important;
    }

    .main .block-container {
        max-width: 860px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label, span {
        letter-spacing: 0;
        color: #17202a;
    }

    /* Ensure slider labels and values are clearly visible in light mode */
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] p,
    .stSlider label,
    .stSlider p,
    .stSlider span {
        color: #17202a !important;
        font-weight: 600 !important;
    }

    .hero {
        border: 1px solid #dfe7ef;
        border-radius: 8px;
        padding: 28px 30px;
        background: linear-gradient(135deg, #f7fbff 0%, #ffffff 55%, #f4fff8 100%);
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 36px;
        line-height: 1.1;
        font-weight: 750;
        color: #123047;
        margin: 0 0 8px;
    }

    .hero-text {
        font-size: 16px;
        color: #52616f;
        margin: 0;
    }

    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #123047;
        margin: 6px 0 12px;
    }

    .result-box {
        border: 1px solid #cfe8d8;
        border-left: 5px solid #2e9f63;
        border-radius: 8px;
        padding: 18px 20px;
        background: #f6fff9;
        margin-top: 18px;
    }

    .result-label {
        font-size: 13px;
        text-transform: uppercase;
        color: #5d7067;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .result-name {
        font-size: 28px;
        font-weight: 800;
        color: #18643a;
        margin: 0;
    }

    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 0;
        background: #1769aa;
        color: white;
        font-weight: 700;
        padding: 0.72rem 1rem;
    }

    .stButton > button:hover {
        background: #11598f;
        color: white;
        border: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with open("iris_dataset.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">Iris Flower Prediction</div>
        <p class="hero-text">Adjust the flower measurements and predict the iris species.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">Flower Measurements</div>', unsafe_allow_html=True)

left_col, right_col = st.columns(2)

with left_col:
    sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1, 0.1)
    petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4, 0.1)

with right_col:
    sepal_width = st.slider("Sepal width (cm)", 2.0, 5.0, 3.5, 0.1)
    petal_width = st.slider("Petal width (cm)", 0.0, 3.0, 0.2, 0.1)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    species = ["setosa", "versicolor", "virginica"]
    predicted_species = species[prediction[0]].title()

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-label">Predicted species</div>
            <p class="result-name">{predicted_species}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
