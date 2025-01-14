import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

with open('xgboost_model.sav', 'rb') as file:
    model = pickle.load(file)

# Page title
st.title("E-commerce Customer Churn Prediction")

# Sidebar for file upload
st.header("Upload Your File")

# Brief explanation
st.write("""
    Please upload your data file for analysis. Make sure the file is in CSV format.
    After the file is uploaded, the application will read your data, and you can proceed with predictions.
""")

# File upload component
uploaded_file = st.file_uploader(
    label="Choose your file", 
    type=["csv"],  
    help="Upload a CSV file."
)

# If a file is uploaded, display its name and contents
if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' has been successfully uploaded!")
    st.write("Here is the content of the file you uploaded:")
    
    try:
        data = pd.read_csv(uploaded_file)
        
        # Display the data for review
        st.dataframe(data)
        
        # Replace 'Mobile' with 'Mobile Phone' in the relevant column
        if 'PreferedOrderCat' in data.columns:
            data['PreferedOrderCat'].replace(to_replace="Mobile", value="Mobile Phone", inplace=True)
        
        # Ensure the data has the necessary columns for prediction
        required_columns = ['Tenure', 'WarehouseToHome', 'NumberOfDeviceRegistered', 
                            'PreferedOrderCat', 'SatisfactionScore', 'MaritalStatus', 
                            'NumberOfAddress', 'Complain', 'DaySinceLastOrder', 'CashbackAmount']
        
        if all(col in data.columns for col in required_columns):
            st.success("The data contains all the necessary columns for prediction.")
            
            # Button to proceed with prediction
            if st.button("Make Prediction"):
                # Perform prediction using the trained model and pipeline
                predictions = model.predict(data[required_columns])
                
                # Map prediction results to 'Churn' or 'Non-Churn'
                data['Prediction'] = predictions
                data['Prediction'] = data['Prediction'].map({1: 'Churn', 0: 'Non-Churn'})
                
                # Display prediction results with a prettier table
                st.write("### Prediction Results:")
                
                # Styling with st.dataframe() or plotly for a more interactive table display
                st.dataframe(data[['Prediction']].style.applymap(
                    lambda x: 'background-color: lightgreen' if x == 'Non-Churn' else 'background-color: lightcoral')
                )

                # Visualize the distribution of predictions
                churn_count = data['Prediction'].value_counts()
                churn_pie = px.pie(churn_count, names=churn_count.index, values=churn_count.values, 
                                   title="Churn vs Non-Churn Prediction Distribution")
                st.plotly_chart(churn_pie)

                # Save the prediction results to a CSV file for download
                csv = data.to_csv(index=False)
                st.download_button(
                    label="Download Prediction Results",
                    data=csv,
                    file_name='predictions.csv',
                    mime='text/csv'
                )
        else:
            st.error(f"Your file does not contain the required columns: {', '.join(required_columns)}")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
else:
    st.info("Please upload a CSV file to get started.")
