📚 Automated Book Publication Workflow
Overview
This project simplifies and automates the process of preparing book chapters for publication. It covers everything from scraping content off the web, rewriting it with AI, allowing manual edits, managing versions with ChromaDB, and performing a simulated RL-based content search — all tied together in one smooth flow.

🚀 Key Features
Web Scraping with Screenshots
Scrapes book chapter data from:
https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1
Saves:
Raw HTML (scraped_data/page.html)
Screenshot (scraped_data/screenshot.png)
Extracted text (data/chapter1.txt)


AI-Powered Writing & Review
ai_writer.py: Rewrites the scraped text (simulated LLM).
ai_reviewer.py: Reviews and improves the rewritten content.
Output saved as: data/chapter1_spun.txt


Human-in-the-Loop Editing
Manual editing enabled via human_loop/editor.py.


Version Control with ChromaDB
All versions stored using versioning/chroma_versioning.py.
Supports retrieval and similarity search for older versions.


Simulated RL-Based Search
rl_search/rl_search.py demonstrates a simulated reinforcement learning search mechanism.


End-to-End Integration
main.py brings all modules together to show the complete workflow in action.

🛠️ Tech Stack
Python 3.11
Playwright (for scraping)
ChromaDB (for versioning and searching)
Simulated LLMs (for AI Writing & Reviewing)
Simulated RL (for search functionality)



📂 Project Structure

├── ai_processing/
│   ├── ai_writer.py
│   └── ai_reviewer.py
├── data/
│   ├── chapter1.txt
│   └── chapter1_spun.txt
├── human_loop/
│   └── editor.py
├── main.py
├── scraping/
│   └── scraper.py
├── scraped_data/
│   ├── page.html
│   └── screenshot.png
├── screenshots/
│   └── chapter1.png
├── versioning/
│   └── chroma_versioning.py
├── rl_search/
│   └── rl_search.py
├── requirements.txt
└── README.md


⚙️ How to Run
1.Install dependencies:
pip install -r requirements.txt
python -m playwright install

2.Scrape the Chapter:
python scraping/scraper.py

3.Rewrite the Content (AI Writer):
python ai_processing/ai_writer.py

4.Review the Content (AI Reviewer):
python ai_processing/ai_reviewer.py

5.Manual Edit (Human-in-the-Loop):
python human_loop/editor.py

6.Full Workflow with Versioning & RL Search:
python main.py


📑 Sample Output
✅ Version 'v1' added.
✅ Version 'v2' added.
📄 Retrieved Document: This is the AI rewritten version.
📚 All Version IDs: ['v1', 'v2']
🔍 Search Results: {'ids': [['v2', 'v1']], ...}


⚠️ Important Notes
AI Writing, Reviewing, and RL-based Search are simulated (no real LLM or RL APIs used).
ChromaDB is used for local storage and versioning.

✅ Assignment Requirements Checklist
    Feature                              Status      
 Web Scraping & Screenshots          ✅ Completed 
 AI Writing & Review (Simulated)     ✅ Completed 
 Human-in-the-Loop Editing           ✅ Completed 
 Versioning with ChromaDB            ✅ Completed 
 RL-based Search (Simulated)         ✅ Completed 
 Agentic API Simulation (`main.py`)  ✅ Completed 

👤 Author
Shubham Thakur
✉️ Email: skt95g@gmail.com
🔗 GitHub: suuvam
