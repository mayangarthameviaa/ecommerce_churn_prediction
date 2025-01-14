import streamlit as st

# Page configuration
st.set_page_config(
    page_title="E-commerce Customer Churn Prediction App"
)

# Adding custom CSS to style the page
st.markdown("""
    <style>
        .main {
            background-color: #f4f7f6;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            font-size: 2.5em;
            color: #4B8E8D;
            text-align: center;
        }
        h2 {
            font-size: 2em;
            color: #3c7c72;
            text-align: center;
        }
        .description {
            font-size: 1.2em;
            color: #333;
            line-height: 1.6;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .image-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .image-container img {
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .caption {
            font-style: italic;
            color: #666;
            margin-top: 10px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Page title with Markdown
st.markdown('<h1>E-commerce Customer Churn Prediction</h1>', unsafe_allow_html=True)

# Application description with styled text and HTML
st.markdown("""
<div class="description">
    <p><strong>This application is designed to predict whether an e-commerce customer is at risk of churning.</strong></p>
    <p>By entering customer behavior and transaction data, this app will provide a prediction of whether 
    the customer is likely to stop using the platform or not.</p>
</div>
""", unsafe_allow_html=True)

# Display an illustrative image with caption below it
st.markdown("""
<div class="image-container">
    <img src="https://miro.medium.com/v2/resize:fit:1400/1*YEBB4XJvcabjp1vL37LLQQ.png" alt="Illustration of E-commerce Customer Churn" width="800">
    <p class="caption">Illustration of E-commerce Customer Churn</p>
</div>
""", unsafe_allow_html=True)
