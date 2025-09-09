## Problem Statement
Cold outreach remains a widely used strategy in B2B sales and recruiting, but personalization at scale presents significant challenges. Traditional approaches rely on manual review of job postings and handcrafted emails, which are labor-intensive and error-prone.

The research challenge is whether Large Language Models (LLMs), combined with retrieval-augmented generation (RAG) and vector similarity search, can:

- Extract structured information from unstructured job descriptions
- Retrieve semantically relevant portfolio projects
- Generate context-aware emails that balance fluency, accuracy, and persuasiveness
- Scale outreach without sacrificing personalization quality

This work explores the feasibility of such a system and evaluates its architecture in terms of automation, quality consistency, and adaptability.

## Methodology
- Data Collection: Job listings scraped from public sources + anonymized sample emails.
- Preprocessing: Extracted structured fields (role, skills, company, requirements) → fed into LLM prompts.
- Models:
  - Baseline: Template-based email generator.
  - LLM Approach: Llama 3.1 (via GroqCloud) + LangChain for orchestration.
  - Embedding Search: ChromaDB to match job descriptions with relevant skills.
- Pipeline:
1. Parse job description.
2. Retrieve relevant skills/experience.
3. Construct context-aware LLM prompt.
4. Generate and evaluate email.

## Experiments
- Automatic Metrics:
  - BLEU, ROUGE → lexical similarity to human-written emails.
  - BERTScore → semantic similarity.
- Human Evaluation (n=30):
  - Relevance (0–5 scale)
  - Persuasiveness (0–5 scale)
  - Clarity (0–5 scale)
- Comparisons:
  - Template baseline vs. fine-tuned prompting strategies.
  - With vs. without ChromaDB retrieval.
 
## Results
- LLM approach achieved +35% higher semantic similarity (BERTScore) vs. template baseline.
- Emails generated with retrieval augmentation scored 1.2 points higher in relevance (human eval).
- Persuasiveness improved when tone control was explicitly added to the prompt.
- Main limitation: occasional hallucination of company details not in job description.

## Future Work
- Fine-tune LLM on a curated dataset of cold emails for domain adaptation.
- Explore reinforcement learning with human feedback (RLHF) to optimize persuasiveness.
- Extend evaluation to real-world A/B testing of conversion rates.
- Investigate integration with CRM systems for end-to-end sales agent automation.
