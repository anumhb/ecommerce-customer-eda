import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Configuration (Light Theme & Wide Layout)
st.set_page_config(
    page_title="E-Commerce Customer Behavior Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Light Theme Styling via Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
        color: #262730;
    }
    .stSidebar {
        background-color: #F8F9FA;
    }
    h1, h2, h3 {
        color: #1F385C;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Load Data with Caching
@st.cache_data
def load_data():
    df = pd.read_csv('ecommerce_customers.csv')
    return df

df = load_data()

# 3. Main Title & Overview
st.title("🛍️ E-Commerce Customer Behavior & Revenue Analytics Dashboard")
st.markdown("""
This interactive web application explores customer engagement channels, loyalty metrics, and key revenue drivers 
based on the e-commerce customer dataset. Use the sidebar filters to drill down into specific customer segments.
""")
st.markdown("---")

# 4. Sidebar Filters (3 Mixed Widget Types)
st.sidebar.header("🔍 Filter Customer Segments")

# Filter 1: Membership Tenure Range Slider
min_m = float(df['Length of Membership'].min())
max_m = float(df['Length of Membership'].max())
tenure_range = st.sidebar.slider(
    "Select Membership Tenure Range (Years):",
    min_value=min_m,
    max_value=max_m,
    value=(min_m, max_m)
)

# Filter 2: Spending Tier Category Dropdown
spend_tier = st.sidebar.selectbox(
    "Select Spending Tier Category:",
    options=["All Customers", "Standard Spenders (< $500)", "High Spenders ($500+)", "VIP Top 10% Spenders"]
)

# Filter 3: Minimum Time on App Number Input
min_app_time = st.sidebar.number_input(
    "Minimum Time on App (Minutes):",
    min_value=0.0,
    max_value=float(df['Time on App'].max()),
    value=0.0,
    step=0.5
)

# Apply Filters to DataFrame
filtered_df = df[
    (df['Length of Membership'] >= tenure_range[0]) & 
    (df['Length of Membership'] <= tenure_range[1]) &
    (df['Time on App'] >= min_app_time)
]

if spend_tier == "Standard Spenders (< $500)":
    filtered_df = filtered_df[filtered_df['Yearly Amount Spent'] < 500]
elif spend_tier == "High Spenders ($500+)":
    filtered_df = filtered_df[filtered_df['Yearly Amount Spent'] >= 500]
elif spend_tier == "VIP Top 10% Spenders":
    threshold_90 = df['Yearly Amount Spent'].quantile(0.90)
    filtered_df = filtered_df[filtered_df['Yearly Amount Spent'] >= threshold_90]

# 5. Top Key Performance Indicators (4 Key Numbers)
st.subheader("📊 Key Performance Indicators (KPIs)")
col1, col2, col3, col4 = st.columns(4)

total_cust = len(filtered_df)
avg_spend = filtered_df['Yearly Amount Spent'].mean() if total_cust > 0 else 0
avg_tenure = filtered_df['Length of Membership'].mean() if total_cust > 0 else 0
max_spend = filtered_df['Yearly Amount Spent'].max() if total_cust > 0 else 0

col1.metric("Total Customers", f"{total_cust:,}")
col2.metric("Average Yearly Spend", f"${avg_spend:,.2f}")
col3.metric("Average Membership Length", f"{avg_tenure:.2f} years")
col4.metric("Maximum Yearly Spend", f"${max_spend:,.2f}")

st.markdown("---")

# 6. Eight Professional Analytical Tabs with Detailed Answers
st.subheader("📈 Interactive Analytical Explorations & Detailed Insights")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Spending Distribution", 
    "Loyalty Profile", 
    "App Engagement", 
    "App vs Revenue", 
    "Web vs Revenue", 
    "Tenure Impact", 
    "Correlation Heatmap", 
    "VIP Top Spenders"
])

# Tab 1: Yearly Spending Distribution (Univariate)
with tab1:
    st.markdown("### Distribution of Yearly Amount Spent")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.histplot(filtered_df['Yearly Amount Spent'], kde=True, color='royalblue', bins=30, ax=ax)
    if total_cust > 0:
        ax.axvline(avg_spend, color='red', linestyle='--', label=f"Mean: ${avg_spend:.2f}")
    ax.set_title("Customer Yearly Spending Frequency Distribution")
    ax.set_xlabel("Yearly Amount Spent ($)")
    ax.set_ylabel("Customer Count")
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    **Detailed Analytical Findings:**
    * **Central Tendency & Spread:** The distribution of yearly customer spending exhibits a normal, bell-shaped curve centered closely around the mean expenditure of ~$499. 
    * **Business Implication:** Most customers fall into a predictable mid-tier spending bracket, indicating a stable core revenue base with fewer extreme outliers on either the lower or upper tails.
    """)

# Tab 2: Customer Loyalty Profile (Univariate)
with tab2:
    st.markdown("### Customer Membership Duration Spread")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.histplot(filtered_df['Length of Membership'], kde=True, color='teal', bins=30, ax=ax)
    if total_cust > 0:
        ax.axvline(avg_tenure, color='red', linestyle='--', label=f"Mean: {avg_tenure:.2f} yrs")
    ax.set_title("Distribution of Length of Membership")
    ax.set_xlabel("Length of Membership (Years)")
    ax.set_ylabel("Customer Count")
    ax.legend()
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **Subscription Tenure Spread:** Customer loyalty tenure spans evenly across a 0 to 7-year range, with an average duration hovering around 3.5 years.
    * **Business Implication:** The symmetrical distribution shows a healthy retention pipeline, though targeted milestones around years 3 and 4 present key opportunities to convert mid-term users into long-term brand advocates.
    """)

# Tab 3: Mobile App Engagement (Univariate)
with tab3:
    st.markdown("### Mobile App Session Duration Spread")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.histplot(filtered_df['Time on App'], kde=True, color='darkorange', bins=30, ax=ax)
    if total_cust > 0:
        app_mean = filtered_df['Time on App'].mean()
        ax.axvline(app_mean, color='red', linestyle='--', label=f"Mean: {app_mean:.2f} min")
    ax.set_title("Distribution of Time Spent on Mobile App")
    ax.set_xlabel("Time on App (Minutes)")
    ax.set_ylabel("Customer Count")
    ax.legend()
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **App Usage Patterns:** Daily or session-based time spent on the mobile application centers tightly around 12 minutes, reflecting consistent user engagement habits.
    * **Business Implication:** The uniformity of app interaction times suggests that users find a reliable rhythm within the mobile environment, making it an ideal channel for timed promotions or personalized push notifications.
    """)

# Tab 4: App Usage vs Revenue (Bivariate)
with tab4:
    st.markdown("### Mobile App Usage vs. Yearly Amount Spent")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.scatterplot(x='Time on App', y='Yearly Amount Spent', data=filtered_df, color='purple', alpha=0.7, ax=ax)
    sns.regplot(x='Time on App', y='Yearly Amount Spent', data=filtered_df, scatter=False, color='black', ax=ax)
    ax.set_title("Time on App vs. Yearly Spending")
    ax.set_xlabel("Time on App (Minutes)")
    ax.set_ylabel("Yearly Amount Spent ($)")
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **Positive Correlation:** There is a clear, moderate positive relationship (~0.50 correlation) between the amount of time customers spend on the mobile app and their total annual spending.
    * **Business Implication:** Enhancing the mobile app experience directly contributes to higher customer monetization. Customers who invest more time navigating the app convert into higher spenders.
    """)

# Tab 5: Website Engagement vs Revenue (Bivariate)
with tab5:
    st.markdown("### Website Engagement vs. Yearly Amount Spent")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.scatterplot(x='Time on Website', y='Yearly Amount Spent', data=filtered_df, color='crimson', alpha=0.7, ax=ax)
    sns.regplot(x='Time on Website', y='Yearly Amount Spent', data=filtered_df, scatter=False, color='black', ax=ax)
    ax.set_title("Time on Website vs. Yearly Spending")
    ax.set_xlabel("Time on Website (Minutes)")
    ax.set_ylabel("Yearly Amount Spent ($)")
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **Flat Trend & Weak Correlation:** Unlike the mobile app, time spent browsing the company website shows a flat regression line and minimal correlation with yearly revenue.
    * **Business Implication:** The current web interface suffers from conversion inefficiencies. Users browsing on the website do not translate session duration into higher monetary purchases, highlighting an urgent need for a website UI/UX audit.
    """)

# Tab 6: Membership Tenure Impact (Bivariate - Strongest Predictor)
with tab6:
    st.markdown("### Impact of Membership Tenure on Revenue")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    sns.scatterplot(x='Length of Membership', y='Yearly Amount Spent', data=filtered_df, color='forestgreen', alpha=0.7, ax=ax)
    sns.regplot(x='Length of Membership', y='Yearly Amount Spent', data=filtered_df, scatter=False, color='black', ax=ax)
    ax.set_title("Length of Membership vs. Yearly Amount Spent (Strongest Predictor)")
    ax.set_xlabel("Length of Membership (Years)")
    ax.set_ylabel("Yearly Amount Spent ($)")
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **Primary Revenue Driver:** `Length of Membership` exhibits the strongest linear correlation (~0.81) with `Yearly Amount Spent` across the entire dataset.
    * **Business Implication:** Customer loyalty and long-term retention are far more valuable to yearly revenue than short-term browsing spikes. Retaining customers past their initial subscription years is the single most critical lever for business growth.
    """)

# Tab 7: Correlation Heatmap
with tab7:
    st.markdown("### Numerical Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    ax.set_title("Feature Correlation Matrix")
    st.pyplot(fig)

    st.markdown("""
    **Detailed Analytical Findings:**
    * **Matrix Summary:** The correlation matrix confirms that `Length of Membership` (0.81) and `Time on App` (0.50) are the primary positive drivers of annual spending, whereas website metrics and auxiliary inputs show negligible correlation.
    * **Business Implication:** Strategic resource allocation should heavily favor mobile app enhancements and customer retention initiatives over general website traffic generation.
    """)

# Tab 8: VIP Top Spenders Segmentation
with tab8:
    st.markdown("### Top 10% Spenders Profile vs. Rest")
    if total_cust > 10:
        threshold = filtered_df['Yearly Amount Spent'].quantile(0.90)
        top_spenders = filtered_df[filtered_df['Yearly Amount Spent'] >= threshold]
        other_spenders = filtered_df[filtered_df['Yearly Amount Spent'] < threshold]
        
        comparison_df = pd.DataFrame({
            'Top 10% Spenders': top_spenders[['Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']].mean(),
            'Rest of Customers': other_spenders[['Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']].mean()
        })
        st.dataframe(comparison_df.style.format("${:.2f}" if 'Yearly Amount Spent' in comparison_df.index else "{:.2f}"))
        
        st.markdown("""
        **Detailed Analytical Findings:**
        * **VIP Behavioral Characteristics:** The top 10% high-spending customers are distinguished primarily by significantly longer membership tenures and higher app engagement metrics compared to standard customers.
        * **Business Implication:** VIP customers are built over time through loyalty rather than accidental high-value initial purchases. Nurturing mid-tier customers toward multi-year commitments will naturally expand the high-spender segment.
        """)
    else:
        st.warning("Not enough customers in the current filtered selection to compute top 10% comparison.")

st.markdown("---")

# 7. Raw Data Toggle Checkbox
if st.checkbox("☑️ Show underlying filtered dataset table"):
    st.subheader("Raw Data Preview")
    st.dataframe(filtered_df)

st.markdown("---")

# 8. Main Findings & Business Insights Section
st.subheader("💡 Main Findings & Strategic Business Recommendations")
st.markdown("""
* **Customer Retention is King:** `Length of Membership` is by far the strongest predictor of annual revenue (~0.81 correlation). Long-term subscribers yield significantly higher lifetime value.
* **Mobile App Outperforms Website:** `Time on App` shows a robust positive relationship with spending (~0.50), whereas website engagement shows minimal correlation. 
* **Strategic Recommendation:** Reallocate marketing and UI/UX investments toward optimizing the mobile application experience, introducing app-exclusive offers, and launching tiered loyalty programs to extend membership tenure.
""")