# HR Intelligence Pipeline: Employee Attrition & Predictive Risk

![Dashboard Preview](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/reports/final_dashboard_screenshot.png)

## 🚀 Project Overview
This project provides an automated end-to-end solution for analyzing employee attrition using the IBM HR Analytics dataset. It features a **Python-based ETL pipeline** integrated with a **high-fidelity Power BI dashboard** to identify high-risk departments and demographic trends.

## 🛠️ Technical Stack
* **Data Engineering:** Python (Pandas) for automated cleaning and feature engineering.
* **Business Intelligence:** Power BI (DAX, Power Query).
* **Visualization:** Custom UI/UX design using professional color theory and grid systems.

## ⚙️ The Data Pipeline
Unlike standard static reports, this project utilizes a custom Python script (`process_data.py`) to automate the "heavy lifting" before the data reaches Power BI:
1.  **Feature Engineering:** Categorized employees into `Income_Tier` and `Commute_Distance` groups.
2.  **Ordinal Mapping:** Implemented a `Tier_Rank` system to ensure visual charts sort logically (Entry → Executive) rather than alphabetically.
3.  **Data Type Integrity:** Managed type conversions to ensure seamless DAX calculations (e.g., converting boolean flags to integers for SUM operations).

### Example Python Logic:
```python
# Custom mapping for logical chart sorting
tier_map = {'Entry': 1, 'Associate': 2, 'Lead': 3, 'Executive': 4}
df['Tier_Rank'] = df['Income_Tier'].map(tier_map)