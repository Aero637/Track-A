import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Bank Marketing RM Insights Dashboard",
    page_icon="🏦",
    layout="wide"
)

# Cache data loading for performance
@st.cache_data
def load_data():
    df = pd.read_csv('bank-full.csv', sep=';')
    df['subscribed_binary'] = df['y'].map({'yes': 1, 'no': 0})
    # Pre-calculate age groups
    bins = [18, 30, 45, 60, 120]
    labels = ['18-30', '31-45', '46-60', '60+']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)
    return df

df = load_data()

# Sidebar title and interactive filters
st.sidebar.title("🏦 Client Filter Panel")
st.sidebar.markdown("Use filters below to isolate specific customer cohorts.")

# Job filter
all_jobs = ['All'] + list(df['job'].unique())
selected_job = st.sidebar.selectbox("Select Client Job Profile:", all_jobs)

# Marital Status filter
all_marital = ['All'] + list(df['marital'].unique())
selected_marital = st.sidebar.selectbox("Select Marital Status:", all_marital)

# Housing Loan filter
housing_filter = st.sidebar.radio("Has Housing Loan?", ['All', 'yes', 'no'])

# Apply filters dynamically
filtered_df = df.copy()
if selected_job != 'All':
    filtered_df = filtered_df[filtered_df['job'] == selected_job]
if selected_marital != 'All':
    filtered_df = filtered_df[filtered_df['marital'] == selected_marital]
if housing_filter != 'All':
    filtered_df = filtered_df[filtered_df['housing'] == housing_filter]

# Header section
st.title("🏦 Bank Term Deposit Campaign Analytics")
st.markdown("### 📊 Relationship Manager (RM) Decision Support System")
st.write("Optimize your outreach programs by identifying cohorts with the highest conversion velocities.")

# Key Performance Indicator (KPI) Metric Cards
total_clients = len(filtered_df)
if total_clients > 0:
    sub_rate = filtered_df['subscribed_binary'].mean() * 100
    avg_bal = filtered_df['balance'].mean()
else:
    sub_rate = 0.0
    avg_bal = 0.0

col1, col2, col3 = st.columns(3)
col1.metric("Selected Cohort Size", f"{total_clients:,} clients")
col2.metric("Subscription Conversion Rate", f"{sub_rate:.2f}%")
col3.metric("Average Cohort Balance", f"${avg_bal:,.2f}")

st.markdown("---")

if total_clients == 0:
    st.warning("⚠️ No clients match the selected combination of filters. Please adjust your criteria.")
else:
    # Row 1: Business Question 1 & 2
    row1_col1, row1_col2 = st.columns(2)
    
    with row1_col1:
        st.subheader("1. Conversion Velocity by Job Category")
        job_stats = filtered_df.groupby('job')['subscribed_binary'].mean().sort_values(ascending=False).reset_index()
        
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.barplot(data=job_stats, x='subscribed_binary', y='job', palette='viridis', ax=ax)
        ax.set_xlabel('Subscription Conversion Rate')
        ax.set_ylabel('Job Type')
        st.pyplot(fig)
        st.caption("Insight: Students and retirees consistently hold premium conversion probabilities.")
        
    with row1_col2:
        st.subheader("2. Likelihood to Subscribe vs Account Balance")
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.boxplot(data=filtered_df, x='y', y='balance', showfliers=False, palette='Set2', ax=ax)
        ax.set_xlabel('Subscribed to Term Deposit?')
        ax.set_ylabel('Liquid Account Balance ($)')
        st.pyplot(fig)
        st.caption("Insight: Subscribing customers typically display significantly more liquid asset tailwinds.")

    st.markdown("---")
    
    # Row 2: Business Question 3 & 4
    row2_col1, row2_col2 = st.columns(2)
    
    with row2_col1:
        st.subheader("3. Conversion Behavior across Age Demographics")
        age_stats = filtered_df.groupby('age_group', observed=False)['subscribed_binary'].mean().reset_index()
        
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.barplot(data=age_stats, x='age_group', y='subscribed_binary', palette='coolwarm', ax=ax)
        ax.set_xlabel('Age Cohort Brackets')
        ax.set_ylabel('Subscription Conversion Rate')
        st.pyplot(fig)
        st.caption("Insight: Conversion follows a U-shaped dynamic, spiking in the 60+ and 18-30 groups.")
        
    with row2_col2:
        st.subheader("4. Impact of Existing Housing Debt")
        house_stats = filtered_df.groupby('housing')['subscribed_binary'].mean().reset_index()
        
        fig, ax = plt.subplots(figsize=(6, 4.5))
        sns.barplot(data=house_stats, x='housing', y='subscribed_binary', palette='pastel', ax=ax)
        ax.set_xlabel('Has Existing Housing Loan?')
        ax.set_ylabel('Subscription Conversion Rate')
        st.pyplot(fig)
        st.caption("Insight: Unencumbered clients are more than twice as likely to lock up funds in new term deposits.")