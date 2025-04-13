# cold-email-generator
Automates personalized cold outreach using job listings and LLMs to boost sales pipeline for software services companies.

## :rocket: Project: AI-Powered Cold Email Generator for Services Sales 

## :jigsaw: Problem Statement
In the highly competitive software services industry, companies such as TCS, Infosys, and LTIMindtree must constantly seek new client projects. One proven technique is cold emailing potential clients who have posted job openings on their careers pages. Sales teams often manually analyze these job listings and craft personalized emails to offer contract-based engineers who match the job requirements.

This process is manual, time-consuming, and often inconsistent.

**This project automates the end-to-end process of crafting high-quality, hyper-relevant cold emails using LLMs**—accelerating outreach efforts, increasing conversions, and creating a scalable solution for business development executives.

## :building_construction: Architecture Overview
This project leverages cutting-edge AI tools and modern software architecture to automate the cold email generation process from job descriptions:

## :wrench: Core Components
- **Web Scraper (LangChain):** Extracts job descriptions from target companies' career portals.

- **LLM (Llama 3.3 via Groq):** Analyzes job descriptions to extract required skills and roles.

- **Vector Database (ChromaDB):** Stores pre-indexed portfolio links mapped to skillsets for fast semantic retrieval.

- **Cold Email Generator (LLM + LangChain):** Combines parsed job data and relevant project portfolio links to generate a personalized email pitch.

## :bulb: Workflow Summary
- **Input:** A job listing URL is provided by the user.

- **Scraping & Extraction:** LangChain scrapes the job page, and Llama 3.1 extracts structured data (skills, role, description) as JSON.

- **Portfolio Matching:** ChromaDB finds relevant internal projects/portfolio links for the extracted skillset.

- **Email Generation:** All data is fed into the LLM to generate a personalized cold email tailored to the job post.

- **Output:** A ready-to-send, targeted cold email with supporting portfolio references.

