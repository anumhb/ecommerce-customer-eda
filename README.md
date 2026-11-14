# 🛍️ E-Commerce Customer Behavior & Revenue Analytics Dashboard

An interactive, production-ready web application built with **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn** to explore customer engagement channels, subscription loyalty, and revenue drivers using the E-Commerce Customers dataset.

---

## 🚀 Live Demo
*Access the live web application here:* [Customer Value Analytics](https://customer-value-analytics.streamlit.app)[cite: 1]

---

## ✨ Key Features & Architecture

* **🎨 Light Theme UI Styling:** Designed with a clean corporate aesthetic, soft containers, and high-contrast typography.
* **🔍 Interactive Sidebar Filters:** 
  * *Membership Tenure Range Slider:* Filter customers by their subscription duration.
  * *Spending Tier Category Dropdown:* Drill down into standard spenders, high spenders, or VIP top 10% customers.
  * *Minimum App Time Number Input:* Filter by minimum mobile application engagement minutes.
* **📊 Key Performance Indicators (KPIs):** Dynamic metric cards tracking Total Customers, Average Yearly Spend, Average Membership Length, and Maximum Yearly Spend in real-time.
* **📈 8 Professional Analytical Tabs:**
  1. *Spending Distribution:* Univariate analysis of annual customer expenditures.
  2. *Loyalty Profile:* Distribution spread of customer subscription tenure.
  3. *App Engagement:* Evaluation of mobile session duration patterns.
  4. *App vs. Revenue:* Bivariate scatter plot with regression analysis for mobile app usage.
  5. *Web vs. Revenue:* Website browsing efficiency versus monetary conversion.
  6. *Tenure Impact:* Quantifying the strongest predictor of customer lifetime value.
  7. *Correlation Heatmap:* Statistical correlation matrix across all numerical variables.
  8. *VIP Top Spenders:* Benchmarking top 10% high-spending customers against the rest of the base.
* **📋 Raw Data Inspection:** Expandable toggle to view and inspect the underlying filtered dataset.
* **💡 Strategic Insights:** Summary narrative block outlining core business takeaways and retention recommendations.

---

## 🛠️ Tech Stack
* **Python** (v3.8+)
* **Streamlit** (Interactive Web Framework)
* **Pandas & NumPy** (Data Manipulation & Caching)
* **Matplotlib & Seaborn** (Data Visualization & Regression Plots)
* **Git & GitHub** (Version Control & Deployment via Streamlit Cloud)

---

## 📂 Project Structure
```text
ecommerce-customer-eda/
│
├── venv/                   # Local Python Virtual Environment (Ignored by Git)
├── app.py                  # Main Streamlit Dashboard Application
├── ecommerce_customers.csv # E-Commerce Customer Dataset (500 rows)
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation