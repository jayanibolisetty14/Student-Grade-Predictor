import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bolisetty Jayani's Grade Predictor",
    page_icon="🎓",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main{
        background-color:#f4f8ff;
    }
    h1{
        color:#1f77b4;
        text-align:center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎓 Bolisetty Jayani's Grade Predictor")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")

st.subheader("Enter Marks (Out of 100)")

english = st.number_input("English", 0, 100, 80)
maths = st.number_input("Mathematics", 0, 100, 80)
science = st.number_input("Science", 0, 100, 80)
social = st.number_input("Social", 0, 100, 80)
computer = st.number_input("Computer", 0, 100, 80)

if st.button("Predict Grade"):

    total = english + maths + science + social + computer
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
        st.balloons()
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.success(f"Student: {name}")
    st.info(f"Roll Number: {roll}")

    st.metric("Total Marks", total)
    st.metric("Percentage", f"{percentage:.2f}%")
    st.metric("Grade", grade)

    st.progress(int(percentage))

    df = pd.DataFrame({
        "Subject": ["English", "Maths", "Science", "Social", "Computer"],
        "Marks": [english, maths, science, social, computer]
    })

    st.subheader("Marks Table")
    st.dataframe(df)

    st.subheader("Bar Chart")
    st.bar_chart(df.set_index("Subject"))

    st.subheader("Pie Chart")
    st.pyplot(df.set_index("Subject").plot.pie(
        y="Marks",
        autopct="%1.1f%%",
        figsize=(5,5)
    ).figure)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Marks CSV",
        csv,
        "marks.csv",
        "text/csv"
    )

st.markdown("---")
st.markdown(
    "<center><h4>Developed by ❤️ Bolisetty Jayani</h4></center>",
    unsafe_allow_html=True
)