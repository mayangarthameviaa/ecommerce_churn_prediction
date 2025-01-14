import streamlit as st

# Header with a larger title and added styling
st.markdown("<h2 style='text-align: center;'>How to Use the Application</h2>", unsafe_allow_html=True)

# Adding some space before instructions
st.markdown("<br>", unsafe_allow_html=True)

# Instructions with added emojis, bold text, and a bit of styling for visual appeal
st.write("""
1. **Enter your customer data**: Input customer behavior and transaction details in the sidebar or on the data input page. 📝
   - Make sure to provide accurate and up-to-date information to get the most accurate prediction.
   
2. **Click the 'Predict Customer Churn' button**: Once you have entered the data, click on the button to get the result. 🚀
   - The prediction will process the data you provided and analyze it using our machine learning model.

3. **View the prediction result**: The app will indicate whether the customer is **at risk of churning** or not. ⚠️
   - If the result is positive, consider strategies to retain the customer. If negative, feel free to celebrate their loyalty! 🎉
""")

# Adding a little more styling and color to the text for emphasis
st.markdown("""
<style>
    p {
        font-size: 18px;
        color: #4B8E8D;
    }
</style>
""", unsafe_allow_html=True)
