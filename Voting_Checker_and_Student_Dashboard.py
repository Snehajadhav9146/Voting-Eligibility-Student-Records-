import streamlit as st
import pandas as pd
#import uuid  # For generating unique IDs

# Title
st.title("Voting Checker & Student Dashboard")

# Enter Name
name = st.text_input('Enter your name')

# Enter Age
age = st.number_input("Enter your age", min_value=0, step=1)

if name:
    st.write(f"Hi, {name}")

    # Check voting eligibility
    if age > 0:
        if age < 18:
            st.write(f"Hi {name}, You are not eligible to vote.")
        else:
            st.write(f"Hi {name}, You are eligible to vote.")

# Enter Marks
marks = st.number_input("Enter Your Marks", min_value=0, max_value=100, step=1)

# Assign Pass/Fail and First Class
if marks >= 75:
    status = "First Class"
elif marks >= 40:
    status = "Pass"
else:
    status = "Fail"

# Generate a Unique Student ID
#student_id = str(uuid.uuid4())[:8]  # Shortened UUID for readability

# Store Data in DataFrame
df = pd.DataFrame({
    #'Student ID': [student_id],
    'Name': [name],
    'Age': [age],
    'Marks': [marks],
    'Status': [status]
})

# Display Data
st.write("Entered Data:")
st.dataframe(df)

# Save to CSV (Append Mode)
if st.button("Save Data"):
    try:
        existing_df = pd.read_csv('data.csv')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # If file does not exist, a new one will be created

    df.to_csv('data.csv', index=False)
    st.success(f"Data saved successfully!")

# Display All Stored Data
if st.button("Show All Data"):
    try:
        full_data = pd.read_csv('data.csv')
        st.write("Stored Data:")
        st.dataframe(full_data)
    except FileNotFoundError:
        st.error("No data available yet.")
