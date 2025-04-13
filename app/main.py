import sys
import pysqlite3
sys.modules["sqlite3"] = pysqlite3
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # st.title("📧 Cold Mail Generator")
    st.title(":e-mail: Email Generator")
    # specify an ACTIVE job posting. Using an expired job link will not work.
    url_input = st.text_input("Enter a URL:", value="https://careers.arcresources.com/job/Calgary-Senior-Data-Scientist-Albe/589984817/")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()  # create chromadb         
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
 

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)