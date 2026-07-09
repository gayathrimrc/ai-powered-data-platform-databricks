# Customer Churn Prediction Platform using Databricks MCP

## End-to-End Architecture Flow


Synthetic SaaS Data
        
        │
        
Bronze (Raw Delta Tables)
        
        │
        ▼
Silver (Cleaned & Validated)
        
        │
        ▼
Gold (Business Features)
        
        │
        ▼
Feature Engineering
        
        │
        ▼
MLflow Training
        
        │
        ▼
Unity Catalog Model Registry
       
        │
        ▼
Batch Scoring
       
        │
        ▼
High-Risk Customer Table
        
        │
        ├──────────────► AI/BI Dashboard
        │
        ├──────────────► Streamlit App
        │
        └──────────────► SQL Alert (>35% Churn)
                     │
                     ▼
                 Email Notification
