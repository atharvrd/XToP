import streamlit as st
import os

from excel_reader import read_excel
from ppt_generator import create_ppt


st.set_page_config(
    page_title="XtoP",
    page_icon="📊",
    layout="wide"
)

st.title("📊 XtoP - Excel to PowerPoint Generator")

st.write(
    "Upload an Excel file and generate a professional PowerPoint report."
)

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file:

    st.success("File Uploaded Successfully")

    if st.button("Generate PPT"):

        os.makedirs("data", exist_ok=True)
        os.makedirs("output", exist_ok=True)

        excel_path = "data/uploaded_report.xlsx"

        with open(excel_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        sheets = read_excel(excel_path)

        ppt = create_ppt(sheets)

        ppt_path = "output/generated_report.pptx"

        ppt.save(ppt_path)

        st.success("PPT Generated Successfully!")

        with open(ppt_path, "rb") as ppt_file:

            st.download_button(
                label="📥 Download PPT",
                data=ppt_file,
                file_name="generated_report.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )