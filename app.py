import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image
from newspaper import fulltext
import requests

pickle_in=open("bert.pkl","rb")
bert_model=pickle.load(pickle_in)

def welcome():
    return "Welcome to the world of Aditya Raj"

def summary_gen_txt(file_txt,minimum,maximum):
    result_txt=bert_model(file_txt,min_length=minimum,max_length=maximum)
    summary_txt="".join(result_txt)
    print(summary_txt)
    return summary_txt

def summary_gen_url(url,minimum,maximum):
    article=fulltext(requests.get(url).text)
    result_url=bert_model(article,min_length=minimum,max_length=maximum)
    summary_url="".join(result_url)
    print(summary_url)
    return summary_url


def main():
    st.title("SUMMARIZE YOUR LENGTHY READING DATA")

    st.sidebar.title("Enter the Type Of Text-Source:")

    st.markdown("This app does the extractive text summarization for your document/blog/report/book etc..")

    st.sidebar.markdown("Text source can be .txt file or url address/link of the blog or article you wamt to summarize ")
    
    source_destination = st.text_input("URL or File Path","Type Here")

    minimum=st.text_input("minimum_summary_length","Type Here")

    maximum=st.text_input("maximum_summary_length","Type Here")

    summary=""

    if st.sidebar.button("Url link"):
        summary=summary_gen_url(source_destination,minimum,maximum)

    if st.sidebar.button(".txt File"):
        uploaded_file=st.file_uploader("Choose the txt file to uploaded",type="txt")
        summary=summary_gen_txt(uploaded_file,minimum,maximum)

    st.success(summary)

if __name__=='__main__':
    main()


