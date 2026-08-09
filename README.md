# DS Job Market Skills Analysis: What Remote Data Science Roles Actually Ask For

## The business problem
Job postings for data science and ML roles vary wildly in how they describe required skills, making it hard to know where to focus a learning plan. The question: pull real, current postings and let the data — not intuition or outdated advice — identify which skills actually show up most, and where the biggest gaps are relative to a specific candidate's current skill set.

## Key findings
- Collected 96 current remote data science / ML job postings via the JSearch API (RapidAPI)
- Extracted mentions of 18 target skills using regex-based NLP across all postings
- Python appeared in 67% of postings, SQL in 34%, and AWS in 27% — the three highest-demand skills in the sample
- A co-occurrence matrix revealed skills cluster into distinct role archetypes (e.g., Python + SQL + Tableau reads as a different role than Python + PyTorch + Docker + Kubernetes)
- A personal skills-gap bubble chart mapped current skills against market demand, identifying SQL as the single highest-priority, most addressable gap

## My recommendation
Prioritize closing the SQL gap first, since it combines high market demand (34% of postings) with being the fastest of the identified gaps to close through structured coursework — a better first move than spreading effort evenly across all 18 tracked skills.

![skills gap bubble chart](visuals/skills-gap-bubble.png)

## How I did it
Built in Python using the JSearch API for live job data collection, regex-based extraction for skill detection across 18 predefined skills, a co-occurrence matrix to reveal skill clustering, and a bubble chart to visualize the personal skills-gap analysis. Data limitations: a single snapshot of 96 postings from one API source, so results reflect a point in time rather than a longitudinal trend, and skill detection via regex can miss non-standard phrasing.

## What I'd do next
Expand to 500+ postings for more statistical reliability, add salary data to correlate compensation with specific skill combinations, and re-run monthly to track how demand shifts over time.
