<a id="readme-top"></a>

## Project: AI-Powered Cold Email Generator for Services Sales 
Automates personalized cold outreach using job listings and LLMs to boost sales pipeline for services companies.

<a name="live-demo"></a>
## Live Demo
Try out the app here: https://cold-email-creator.streamlit.app/
</br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#problem-statement">Problem Statement</a>
    </li>
    <li>
      <a href="#architecture-overview">Architecture Overview</a>
      <ul>
        <li><a href="#core-components">Core Components</a></li>
        <li><a href="#workflow-summary">Workflow Summary</a></li>
      </ul>
    </li>
    <li><a href="#live-demo">Live Demo</a></li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#clone-repository">Clone the Repository</a></li>
        <li><a href="#activate-venv">Create and Activate Virtual Environment (Optional but Recommended)</a></li>
        <li><a href="#install-dependencies">Install Dependencies</a></li>
        <li><a href="#.env">Set Up .env File</a></li>
        <li><a href="#job-post-url">Update the Job Posting URL</a></li>
        <li><a href="#run-app">Run the App</a></li>
      </ul>
    <li><a href="#notes">Notes</a></li>

  </ol>
</details>

<!-- PROBLEM STATEMENT -->
<a name="problem-statement"></a>
## :jigsaw: Problem Statement
In the highly competitive software services industry, companies constantly seek new client projects. One proven technique is cold emailing potential clients who have posted job openings on their careers pages. Sales teams often manually analyze these job listings and craft personalized emails to offer contract-based engineers who match the job requirements. 

**Challenge:** This process is manual, time-consuming, and often inconsistent.

**This project automates the end-to-end process of crafting high-quality, hyper-relevant cold emails using LLMs**—accelerating outreach efforts, increasing conversions, and creating a scalable solution for business development executives.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="architecture-overview"></a>
## :building_construction: Architecture Overview
This project leverages cutting-edge AI tools and modern software architecture to automate the cold email generation process from job descriptions:

<a name="core-components"></a>
### :wrench: Core Components
- **Web Scraper (LangChain):** Extracts job descriptions from target companies' career portals.

- **LLM (Llama 3.3 via Groq):** Analyzes job descriptions to extract required skills and roles.

- **Vector Database (ChromaDB):** Stores pre-indexed portfolio links mapped to skillsets for fast semantic retrieval.

- **Cold Email Generator (LLM + LangChain):** Combines parsed job data and relevant project portfolio links to generate a personalized email pitch.

<a name="workflow-summary"></a>
### :bulb: Workflow Summary
- **Input:** A job listing URL is provided by the user.

- **Scraping & Extraction:** LangChain scrapes the job page, and Llama 3.1 extracts structured data (skills, role, description) as JSON.

- **Portfolio Matching:** ChromaDB finds relevant internal projects/portfolio links for the extracted skillset.

- **Email Generation:** All data is fed into the LLM to generate a personalized cold email tailored to the job post.

- **Output:** A ready-to-send, targeted cold email with supporting portfolio references.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="usage"></a>
## Usage
<a name="clone-repository"></a>
1. Clone the Repository
```sh
git clone https://github.com/UjuAyoku/cold-email-generator.git

cd cold-email-generator/app
```

<a name="activate-virtual-env"></a>
2. Create and Activate Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate      # On macOS/Linux
env\Scripts\activate         # On Windows
```

<a name="install-dependencies"></a>
3. Install Dependencies
```sh
pip install -r requirements.txt
```

<a name=".env"></a>
4. Set Up .env File </br>
Create a .env file inside the app directory and add your credentials. This is used to authenticate and access Groq’s Llama 3.3 model.
```sh
GROQ_API_KEY=your_groq_api_key
```

<a name="job-post-url"></a>
5. Update the Job Posting URL </br>
* Open main.py and update the placeholder URL to a valid job posting
```sh
url_input = "https://careers.example.com/job/software-engineer-ai"
```

<a name="run-app"></a>
6. Run the App </br>
From inside the app/ folder, launch the Streamlit app:
```sh
python streamlit run main.py
```
The app will open in your browser at http://localhost:8501.

<a name="notes"></a>
### :pushpin: Notes
- The project relies on your curated project portfolio in app/resource/portfolio.csv. Ensure it's up-to-date.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
