
## 🏗️ Project Architecture

This repository is structured cleanly into modular subcomponents separating data ingestion, statistical metrics extraction, and interactive visual rendering.

```text
bank-marketing-analytics/
│
├── data/
│   └── bank-full.csv            # Semicolon-delimited target dataset
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Ingestion & preprocessing engine
│   ├── analysis_engine.py      # Core functional statistical modules
│   └── app.py                  # Interactive Streamlit dashboard pipeline
│
├── requirements.txt            # System dependencies
└── EXPLANATION.md              # Methodology and strategic choices documentation

⚙️ Functional Code Modules:
1. Ingestion Engine (src/data_loader.py)
This script isolates the structural ingestion system. It maps data properties dynamically and ensures uniform data validation before feeding calculations to the dashboard:

load_clean_data(filepath): Consumes the raw text dataset utilizing explicit separation controls (sep=';'). It maps raw targets (yes/no) into clean binary data variables (1/0) and handles age discretization into targeted generational buckets (18-30, 31-45, 46-60, 60+).

2. Statistical Analysis Engine (src/analysis_engine.py)
This module houses pure data functions, separating calculations from user interface rendering. It directly computes the answers to key business questions:

calculate_job_metrics(df): Aggregates conversion rate properties over distinct professional industry types.

calculate_age_metrics(df): Computes sub-cohort conversion velocity across age brackets.

calculate_housing_metrics(df): Evaluates product enrollment behavior against outstanding real estate liens.

3. Interactive Web UI Portal (src/app.py)
The master runtime environment for the Streamlit web server. It establishes an active analytics control deck:

Global Filters: Leverages live cache memory (@st.cache_data) for fluid parameter evaluations on real-time filters (Job profile, Marital status, and Housing debt).

Cross-Filtering Matrix: Dynamically re-computes key performance indicators (Total Population Size, Subscription Yield, and Average Balances) on matching consumer criteria instantly.

🚀 Installation & Local Execution:

Follow these steps to deploy and run the infrastructure locally on your machine:

1. Clone the Workspace Repository:

git clone [https://github.com/YOUR_USERNAME/bank-marketing-analytics.git](https://github.com/YOUR_USERNAME/bank-marketing-analytics.git)
cd bank-marketing-analytics

2. Configure a Virtual Environment:

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Mac / Linux terminal
python3 -m venv venv
source venv/bin/activate

3. Deploy Project Dependencies:

pip install -r requirements.txt

4. Fire up the Interactive Dashboard Server
Bash:

cd src
python eda_analysis.py
python -m streamlit run app.py

This will be live at: http://localhost:8501
The following two main screendhot of steps attached:
python eda_analysis.py
<img width="1293" height="457" alt="image" src="https://github.com/user-attachments/assets/a1b20e4e-b841-4b67-a56d-d367bbba8c59" />
python -m streamlit run app.py
<img width="1194" height="463" alt="image" src="https://github.com/user-attachments/assets/c08d324d-6265-4a5e-ab57-9f4ad1cdf3ac" />

The result will look like:
<img width="1906" height="985" alt="image" src="https://github.com/user-attachments/assets/d9c21057-f6ac-44ad-a9f0-13e3c66f70f3" />
<img width="1891" height="1023" alt="image" src="https://github.com/user-attachments/assets/1d72b256-bcb6-49ff-8d42-b34af643fd98" />
<img width="1898" height="904" alt="image" src="https://github.com/user-attachments/assets/ac096688-4bbb-40ed-bf8c-1e4b1819b608" />
For Management:
<img width="1907" height="968" alt="image" src="https://github.com/user-attachments/assets/c2149566-8b75-4a7d-9a8c-510a9cd2b06c" />
<img width="1372" height="795" alt="image" src="https://github.com/user-attachments/assets/b57b5ef4-f1b8-4ff1-9729-0e040b3359b7" />
Like this, for all datas it will show the graphs

Answers of the questions asked:

Q1: Which job types have the highest subscription rate?

Answer: Students have the absolute highest conversion rate at 28.68%, followed closely by Retired individuals at 22.79%.

Business Insight: These two demographics represent the highest-performing cohorts for the campaign. Conversely, traditional blue-collar workers and entrepreneurs display the lowest conversion velocities. RMs should focus their primary term deposit marketing efforts toward senior wealth management accounts (retired) and structural entry-level savings packages (students).

Q2: Is there a pattern between account balance and likelihood to subscribe?

Answer: Yes, there is a clear positive correlation. Customers who ultimately subscribe (yes) maintain a significantly higher median liquid balance (~$733) than those who decline the product (no, median balance ~$417).

Business Insight: The boxplot distribution displays an upward shift in the interquartile range for subscribers. This indicates that available liquid capital is a direct prerequisite for product locking. RMs can drastically increase campaign efficiency by filtering their outreach lists to target prospects holding higher available balances.

Q3: How does subscription rate differ across age groups? (Binned into 18-30, 31-45, 46-60, 60+)

Answer: Conversion follows a highly pronounced U-shaped curve:

60+ Group: Highest conversion velocity at 42.26%.

18-30 Group: Moderate conversion velocity at 16.22%.

31-45 & 46-60 Groups: Lowest performance, dipping below a 10% subscription rate.

Business Insight: Mid-career segments are likely weighed down by higher personal or family expenses, making long-term fund locking unattractive. RMs should reallocate marketing budget away from the 31–60 demographic and lean into capital preservation products for the high-performing senior bracket.

Q4: Does having an existing housing loan make someone less likely to take a new product?

Answer: Yes, dramatically less likely. Customers without an existing housing loan convert at a rate of 16.70%, whereas those carrying active housing debt drop sharply to a conversion rate of just 7.70%.

Business Insight: An active mortgage acts as a heavy financial encumbrance, locking up a consumer’s discretionary cash flow and creating debt aversion. Individuals free of housing debt possess double the propensity to allocate assets into a new term deposit product.
