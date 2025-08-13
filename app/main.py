import sys
import pysqlite3  # required to fix sqlite3 issue for streamlit cloud deployment
sys.modules["sqlite3"] = pysqlite3 # required to fix sqlite3 issue for streamlit cloud 
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # st.title("📧 Cold Mail Generator")
    st.title(":e-mail: Cold Email Generator")
    user_name = st.text_input("Your Full Name:", placeholder="e.g. Alex Johnson", help="This will appear as the sender's name in the email")
    company_name = st.text_input("Your Company Name:", placeholder="e.g. DataSolutions Inc.", help="Your business/organization name")
    # specify an ACTIVE job posting. Using an expired job link may not work.
    url_input = st.text_input("Target Job Posting URL:", value="", placeholder="https://company.com/careers/senior-data-scientist", 
                              help="Must be an active job posting. Expired listings may not work.")
    submit_button = st.button("Generate Email", help="Click to generate personalized cold email")

    if submit_button:
        if not user_name or not company_name:
            st.warning("Please enter both your name and your company name.")
            return

    if submit_button:
        if not user_name or not company_name:
            st.warning("Please enter both your name and your company name.")
            return
        
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()  # create chromadb         
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links, user_name, company_name)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
 

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
