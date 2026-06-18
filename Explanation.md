# Track A: Data Analyst Assignment Explanation

 1. Project Architecture & Decisions
* **Data Ingestion Pipeline:** The data is loaded dynamically using a semicolon delimiter (`sep=';'`). 
* **Interactive Tooling:** Streamlit was chosen for the interactive front-end as it allows Relationship Managers to isolate variables on the fly without writing SQL or modifying python scripts.
* **Missing Value Handling Strategy:** Instead of removing or arbitrarily modifying rows with `"unknown"` tokens, we retained them explicitly within the structural category breakdowns. This tracks downstream system gaps without introducing bias into demographic calculations.

 2. Core Business Insights & Answers

 Q1: Which job types have the highest subscription rate?
* **Findings:** **Students** (~28.68%) and **Retired** individuals (~22.79%) possess the highest conversion probabilities.
* **RM Action Strategy:** RMs should pitch structural cash accumulation packages to younger students looking for low-risk alternatives, and stable asset preservation models to retirees.

 Q2: Account Balance Pattern vs Likelihood to Subscribe
* **Findings:** Subscribers have a significantly higher median capital reserve (~$733) compared to non-subscribers (~$417). 
* **RM Action Strategy:** Implement a filter threshold focusing outreach efforts on clients holding over $700 in available balances to avoid inefficient cold-calling.

Q3: Subscription Rate across Age Groups
* **Findings:** Outbound campaigns show a distinct U-shaped curve. Seniors (**60+**) convert at an exceptional **42.26%**, and younger groups (**18-30**) follow at **16.22%**. Mid-career segments remain low.
* **RM Action Strategy:** Pivot campaign intensity away from target demographics aged 31–60 towards older wealth management groups.

 Q4: Does having an existing housing loan make someone less likely to take a new product?
* **Findings:** Yes. Unencumbered individuals subscribe at a rate of **16.70%**, while clients carrying existing housing loans fall sharply to **7.70%**.
* **RM Action Strategy:** Filter out clients with active housing liens to protect margin and efficiency.

 3. How to Execute the Project
1. Install requirements:
   ```bash
   pip install streamlit pandas matplotlib seaborn

2. After the installation, type the following command:
python eda_analysis.py

3. Next type: python -m streamlit run app.py

Finally the output will get visible