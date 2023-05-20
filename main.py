import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
# Sample DataFrame

file = st.file_uploader('Upload a CSV file', type=['csv'])


if file:
    question = st.text_input('Question ?')
    df = pd.read_csv(file)

    llm = OpenAI(api_token="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")
    pandas_ai = PandasAI(llm, conversational=False)

    st.dataframe(df)
    if question:
        response = pandas_ai(df, prompt=question)
        st.text(response)
