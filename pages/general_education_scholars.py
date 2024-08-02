import streamlit as st
import pandas as pd
from utils.data_utils import load_csv, save_csv

def render():
    st.title("General Education Scholars")
    st.write("This page displays information about scholars in grade school.")

    try:
        # Load the data
        data = load_csv("data/general_education_scholars.csv")
        st.dataframe(data)
    except FileNotFoundError:
        st.write("No data file found. Please enter data manually.")

    # Create a form to add new scholars
    st.write("Add a new scholar:")
    form = st.form(key="add_scholar")
    name = form.text_input("Name")
    grade_level = form.text_input("Grade Level")
    school = form.text_input("School")
    date_of_birth = form.date_input("Date of Birth", min_value=pd.to_datetime("1970-01-01"), max_value=pd.to_datetime("today"))
    date_awarded_scholarship = form.date_input("Date Awarded Scholarship")
    submit = form.form_submit_button("Add Scholar")

    # Add the new scholar to the data
    if submit:
        new_scholar = pd.DataFrame({
            "Name": [name],
            "Grade Level": [grade_level],
            "School": [school],
            "Date of Birth": [date_of_birth],
            "Date Awarded Scholarship": [date_awarded_scholarship]
        })

        try:
            # Load existing data and append new scholar
            data = load_csv("data/general_education_scholars.csv")
            data = pd.concat([data, new_scholar])
        except FileNotFoundError:
            # If no data file exists, create a new one
            data = new_scholar

        save_csv(data, "data/general_education_scholars.csv")
        st.success("Scholar added successfully!")

render()