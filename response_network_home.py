# app.py
import streamlit as st

def main():
    st.title("Response Network Home")
    st.write("Welcome to the Response Network!")
    st.write("This platform is designed to track and manage scholars' progress and alumni network.")

    st.header("Features")
    with st.expander("Scholar Management"):
        st.write("• General Education Scholars: View and manage general education scholars.")
        st.write("• Tertiary Education Scholars: View and manage tertiary education scholars.")
        st.write("• Scholar Tracker: Monitor scholars' progress and performance.")

    with st.expander("Alumni Network"):
        st.write("• Response Network Alumni: Connect with our alumni and stay updated on their achievements.")

    with st.expander("Instructions"):
        st.write("• To get started, select a page from the menu.")
        st.write("• Use the scholar management features to view and manage scholars.")
        st.write("• Use the alumni network feature to connect with our alumni.")

if __name__ == "__main__":
    main()