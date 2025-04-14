<a id="readme-top"></a>



# :rocket: Project: AI-Powered Cold Email Generator for Services Sales 
Automates personalized cold outreach using job listings and LLMs to boost sales pipeline for software services companies.

 


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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#notes">Notes</a></li>

  </ol>
</details>



<!-- PROBLEM STATEMENT -->
## :jigsaw: Problem Statement
In the highly competitive software services industry, companies such as TCS, Infosys, and LTIMindtree must constantly seek new client projects. One proven technique is cold emailing potential clients who have posted job openings on their careers pages. Sales teams often manually analyze these job listings and craft personalized emails to offer contract-based engineers who match the job requirements.

This process is manual, time-consuming, and often inconsistent.

**This project automates the end-to-end process of crafting high-quality, hyper-relevant cold emails using LLMs**—accelerating outreach efforts, increasing conversions, and creating a scalable solution for business development executives.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## :building_construction: Architecture Overview
This project leverages cutting-edge AI tools and modern software architecture to automate the cold email generation process from job descriptions:

### :wrench: Core Components
- **Web Scraper (LangChain):** Extracts job descriptions from target companies' career portals.

- **LLM (Llama 3.3 via Groq):** Analyzes job descriptions to extract required skills and roles.

- **Vector Database (ChromaDB):** Stores pre-indexed portfolio links mapped to skillsets for fast semantic retrieval.

- **Cold Email Generator (LLM + LangChain):** Combines parsed job data and relevant project portfolio links to generate a personalized email pitch.

### :bulb: Workflow Summary
- **Input:** A job listing URL is provided by the user.

- **Scraping & Extraction:** LangChain scrapes the job page, and Llama 3.1 extracts structured data (skills, role, description) as JSON.

- **Portfolio Matching:** ChromaDB finds relevant internal projects/portfolio links for the extracted skillset.

- **Email Generation:** All data is fed into the LLM to generate a personalized cold email tailored to the job post.

- **Output:** A ready-to-send, targeted cold email with supporting portfolio references.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Live Demo
Try out the app here: https://cold-email-creator.streamlit.app/

## How to Use the Cold Email Generator Code
1. Clone the Repository
- git clone https://github.com/UjuAyoku/cold-email-generator.git
- cd cold-email-generator/app

2. Create and Activate Virtual Environment (Optional but Recommended)
* python -m venv env
* source env/bin/activate      # On macOS/Linux
* env\Scripts\activate         # On Windows

3. Install Dependencies:
<pre><code>```python pip install -r requirements.txt```</code></pre>

4. Set Up .env File
Create a .env file inside the app directory and add your credentials:
* GROQ_API_KEY=your_groq_api_key
* This is used to authenticate and access Groq’s Llama 3.3 model.

5. Update the Job Posting URL
* Open main.py and update the placeholder URL to a valid job posting:
url_input = "https://careers.example.com/job/software-engineer-ai"

6. Run the App
From inside the app/ folder, launch the Streamlit app:
```sh
python streamlit run main.py
```

Your app will open in your browser at http://localhost:8501.

### :pushpin: Notes
- The project relies on your curated project portfolio in app/resource/portfolio.csv. Ensure it's up-to-date.

- Groq’s API is blazing fast for Llama 3.3—perfect for real-time cold email generation.

- You can further extend this by integrating multiple job sources.

<p align="right">(<a href="#readme-top">back to top</a>)</p>