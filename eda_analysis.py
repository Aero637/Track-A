import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda():
    # 1. Load Data
    print("Loading bank-full.csv...")
    df = pd.read_csv('bank-full.csv', sep=';')
    
    # 2. Check Dataset Profile
    print("\n=== DATASET PROFILE ===")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    print("\n--- Missing Values (NaN) ---")
    print(df.isna().sum())
    
    print("\n--- Missing Values represented as 'unknown' ---")
    for col in df.columns:
        unknown_cnt = (df[col] == 'unknown').sum()
        if unknown_cnt > 0:
            print(f"  {col}: {unknown_cnt} values")
            
    print("\n--- Target Variable 'y' Distribution ---")
    print(df['y'].value_counts(normalize=True) * 100)
    
    # Pre-processing target for numerical analysis
    df['subscribed_binary'] = df['y'].map({'yes': 1, 'no': 0})
    
    # Apply theme
    sns.set_theme(style="whitegrid")
    
    # Question 1: Job Types vs Subscription Rate
    plt.figure(figsize=(10, 5))
    job_rate = df.groupby('job')['subscribed_binary'].mean().sort_values(ascending=False).reset_index()
    sns.barplot(data=job_rate, x='subscribed_binary', y='job', palette='viridis')
    plt.title('Subscription Rate by Job Type', fontsize=14, pad=15)
    plt.xlabel('Subscription Rate (Proportion)')
    plt.ylabel('Job Type')
    plt.tight_layout()
    plt.savefig('job_subscription_rate.png')
    plt.close()
    
    # Question 2: Account Balance Pattern
    plt.figure(figsize=(8, 5))
    # Boxplot with outliers hidden for a clean visual representation
    sns.boxplot(data=df, x='y', y='balance', showfliers=False, palette='Set2')
    plt.title('Account Balance Distribution by Subscription Status (Outliers Hidden)', fontsize=14, pad=15)
    plt.xlabel('Subscribed to Term Deposit?')
    plt.ylabel('Account Balance ($)')
    plt.tight_layout()
    plt.savefig('balance_vs_subscription.png')
    plt.close()
    
    # Question 3: Age Groups Subscription Rate
    bins = [18, 30, 45, 60, 120]
    labels = ['18-30', '31-45', '46-60', '60+']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)
    
    plt.figure(figsize=(8, 5))
    age_rate = df.groupby('age_group', observed=False)['subscribed_binary'].mean().reset_index()
    sns.barplot(data=age_rate, x='age_group', y='subscribed_binary', palette='coolwarm')
    plt.title('Subscription Rate by Age Group', fontsize=14, pad=15)
    plt.xlabel('Age Group')
    plt.ylabel('Subscription Rate (Proportion)')
    plt.tight_layout()
    plt.savefig('age_subscription_rate.png')
    plt.close()
    
    # Question 4: Existing Housing Loan Effect
    plt.figure(figsize=(6, 5))
    housing_rate = df.groupby('housing')['subscribed_binary'].mean().reset_index()
    sns.barplot(data=housing_rate, x='housing', y='subscribed_binary', palette='pastel')
    plt.title('Subscription Rate by Housing Loan Status', fontsize=14, pad=15)
    plt.xlabel('Has Housing Loan?')
    plt.ylabel('Subscription Rate (Proportion)')
    plt.tight_layout()
    plt.savefig('housing_vs_subscription.png')
    plt.close()
    
    print("\nFour analysis insight plots saved successfully in the directory!")

if __name__ == '__main__':
    run_eda()