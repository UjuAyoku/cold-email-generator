<a id="readme-top"></a>

<div align="center">
  <h1>AI-Powered Cold Email Generator</h1>
  <h3>Automate personalized outreach using AI to boost your services sales pipeline</h3>
  
  [![Live Demo](https://img.shields.io/badge/Try-Live_Demo-green)](https://cold-email-creator.streamlit.app/)

</div>

## Features

- Automatic job description scraping from career pages
- AI-powered analysis of job requirements
- Personalized email generation with relevant portfolio links
- Fast processing with Groq's inference API
- Portfolio matching using vector similarity search

<!-- TABLE OF CONTENTS -->
<details open>
  <summary><h2>Table of Contents</h2></summary>
  <ol>
    <li><a href="#problem-statement">Problem Statement</a></li>
    <li><a href="#architecture-overview">Architecture Overview</a>
      <ul>
        <li><a href="#core-components">Core Components</a></li>
        <li><a href="#workflow-summary">Workflow Summary</a></li>
      </ul>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage Guide</a>
      <ul>
        <li><a href="#config">Configuration</a></li>
        <li><a href="#portfolio-setup">Portfolio Setup</a></li>
        <li><a href="#running-the-app">Running the Application</a></li>
      </ul>
    </li>
    <li><a href="#notes">Important Notes</a></li>
  </ol>
</details>

<!-- PROBLEM STATEMENT -->
<a name="problem-statement"></a>
## Problem Statement
In the highly competitive software services industry, companies constantly seek new client projects. One proven technique is cold emailing potential clients who have posted job openings on their careers pages. Sales teams often manually analyze these job listings and craft personalized emails to offer contract-based engineers who match the job requirements. 

**Current Challenges:** 
- Manual process is time-consuming
- Inconsistent email quality
- Difficult to scale outreach efforts
- Portfolio matching is subhective

**Solution:**
- Automates the entire workflow
- Generates hyper-relevant emails in seconds
- Includes data-driven portfolio matches
- Maintains consistent quality

**This project automates end-to-end cold email generation** - from job posting analysis to personalized outreach - helping business development teams scale their pipeline efficiently.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="architecture-overview"></a>
## Architecture Overview
<a name="core-components"></a>
### Core Components

| Component | Technology | Purpose | 
|-----------|------------|---------|
| **Web Scraper** | LangChain | Extract job descriptions from target companies' job pages | 
| **LLM Processor** | Llama 3 via Groq | Analyze job requirements to extract required skills and roles| 
| **Vector Database** | ChromaDB | Stores pre-indexed portfolio links mapped to skillsets for fast semantic retrieval. | 
| **Email Generator** | LLM + LangChain | Combines parsed job data and relevant project portfolio links to generate a personalized email pitch. | 
| **Frontend UI** | Streamlit | User-friendly interface |  


<a name="workflow-summary"></a>
### Workflow Summary
graph LR
    A[Job URL] --> B[Scraper]
    B --> C[LLM Analysis]
    C --> D{{Skills/Requirements}}
    D --> E[Vector DB Match]
    E --> F[Email Generator]
    F --> G[Output Email]

- **Input:** A job listing URL is provided by the user.

- **Scraping & Extraction:** LangChain scrapes the job page, and Llama 3.1 extracts structured data (skills, role, description) as JSON.

- **Portfolio Matching:** ChromaDB finds relevant internal projects/portfolio links for the extracted skillset.

- **Email Generation:** All data is fed into the LLM to generate a personalized cold email tailored to the job post.

- **Output:** A ready-to-send, targeted cold email with supporting portfolio references.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="installation"></a>
## Installation
```sh
# Clone the repository
git clone https://github.com/UjuAyoku/cold-email-generator.git

# Navigate to project directory
cd cold-email-generator/app

# Create and Activate Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate      # On macOS/Linux
env\Scripts\activate         # On Windows
```

# Install dependencies
pip install -r requirements.txt
```

<a name="usage"></a>
## Usage
<a name="config"></a>
1. Configure Environment
This is used to authenticate and access Groq’s Llama 3.3 model.
```sh
echo "GROQ_API_KEY=your_api_key_here" > .env  
```

<a name="portfolio-setup"></a>
2. Prepare Your Portfolio
- Update app/resources/portfolio.csv with your projects
- Format: skills, link

<a name="running-the-app"></a>
3. Run the Application
```sh
python streamlit run main.py
```

4. Input Job URL
```sh
# In main.py
url_input = "https://careers.example.com/job/software-engineer"
```

5. Get Your Email
- The app will output a ready-to-send cold email
- Copy or export directly to your email client

<a name="notes"></a>
### :pushpin: Important Notes
- The project relies on your curated project portfolio in app/resource/portfolio.csv.  Keep your portfolio.csv updated for best matches
- API may have usage limits 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
