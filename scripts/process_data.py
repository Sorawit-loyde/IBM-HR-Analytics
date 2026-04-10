import pandas as pd
import os

def run_automation():
    # 1. Path Management (Ensures it works even if run from root)
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_path, 'data_raw', 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
    output_file = os.path.join(base_path, 'data_cleaned', 'HR_Cleaned_Data.csv')

    print(f"📂 Loading data from: {input_file}")
    df = pd.read_csv(input_file)

    # 2. Data Engineering (HR & Finance logic)
    # Drop columns that have no variance (useless for analysis)
    # Based on your headline: EmployeeCount, Over18, and StandardHours are usually constant
    cols_to_drop = ['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])

    # Convert Attrition to binary (0 and 1) for easier math in Power BI
    df['Attrition_Flag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Convert OverTime to binary
    df['OverTime_Flag'] = df['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

    # 3. Create Categorical Buckets (Feature Engineering)
    # Create Income Tiers for the Financial Dashboard
    df['Income_Tier'] = pd.qcut(df['MonthlyIncome'], q=4, labels=['Entry', 'Associate', 'Lead', 'Executive'])

    # Create Distance Groups for Operations analysis
    df['Commute_Distance'] = pd.cut(df['DistanceFromHome'], 
                                     bins=[0, 5, 15, 100], 
                                     labels=['Near', 'Moderate', 'Far'])

    # 4. Save the Cleaned Dataset
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
        
    df.to_csv(output_file, index=False)
    print(f"✅ Automation Complete! Saved to: {output_file}")

if __name__ == "__main__":
    run_automation()