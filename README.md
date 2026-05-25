# 📱 Google Play Store Analytics Dashboard

> An end-to-end data analytics and interactive dashboard project built on Google Play Store datasets — covering preprocessing, EDA, sentiment analysis, and Power BI visualization.

---

## 📌 Project Overview

This project is a complete end-to-end data analytics and dashboard development solution built using the **Google Play Store Apps** and **User Reviews** datasets. It focuses on data preprocessing, feature engineering, exploratory data analysis (EDA), sentiment analysis, and interactive dashboard development using **Power BI**.

The dashboard was developed as part of an internship project where multiple analytical tasks and custom visualization requirements were implemented on the same dataset used during the training phase.

---

## 🎯 Objectives

- Perform complete preprocessing and cleaning of Google Play Store datasets
- Conduct exploratory data analysis (EDA) to identify trends and insights
- Perform sentiment and subjectivity analysis on user reviews
- Create task-specific filtered datasets
- Build professional and interactive Power BI dashboards
- Publish the dashboard for public access
- Present insights through visually appealing and business-focused analytics

---

## 📂 Dataset Information

### 1. 🗂️ Google Play Store Apps Dataset
| Field | Description |
|---|---|
| App Info | Name, category, content rating |
| Performance | Ratings, reviews, installs |
| Financials | Price, revenue-related info |
| Technical | Android version, app size |
| Temporal | Last updated date |

### 2. 💬 Google Play Store User Reviews Dataset
| Field | Description |
|---|---|
| Reviews | Raw user review text |
| Sentiment Labels | Positive / Negative / Neutral |
| Sentiment Polarity | Polarity score (-1 to 1) |
| Sentiment Subjectivity | Subjectivity score (0 to 1) |

---

## ⚙️ Technologies Used

### 🐍 Programming & Analytics
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

### 📊 Dashboard & Visualization
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

### 🛠️ Development Tools
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 🧹 Data Preprocessing

| Step | Details |
|---|---|
| Missing Values | Imputation and removal strategies |
| Duplicates | Removed duplicate app entries |
| Column Cleaning | Cleaned `Installs` and `Price` columns |
| Data Types | Converted to appropriate types |
| Revenue | Calculated estimated revenue |
| Date Formatting | Extracted date features |
| Feature Engineering | Created derived features |
| Review Preprocessing | Cleaned and normalized reviews |
| Sentiment Preprocessing | Prepared text for analysis |
| Dataset Merging | Joined apps and reviews datasets |

---

## 📊 Exploratory Data Analysis (EDA)

### Analyses Performed
- Statistical summaries & missing value analysis
- Outlier detection & correlation analysis
- Category, revenue, installs & rating analysis
- Time-series & trend visualization

### Visualizations Used
| Chart Type | Purpose |
|---|---|
| Bar Charts | Category comparisons |
| Box Plots | Outlier detection |
| Heatmaps | Correlation analysis |
| Trend Charts | Time-series insights |
| Scatter Plots | Relationship analysis |
| Bubble Charts | Multi-variable analysis |

---

## 😊 Sentiment Analysis

Sentiment analysis was performed on the user review dataset covering:

- **Polarity Analysis** — Positive, Negative, Neutral classification
- **Subjectivity Analysis** — Objective vs Subjective categorization
- **Review Length Analysis** — Character and word count distribution
- **Sentiment Distribution** — Visual breakdown across app categories

---

## 📈 Dashboard Features

### ✅ KPI Cards
| Metric | Description |
|---|---|
| Total Apps | Count of apps in the store |
| Average Rating | Overall average rating |
| Total Installs | Sum of installs across all apps |
| Total Revenue | Estimated cumulative revenue |
| Average Reviews | Mean review count per app |
| Average Sentiment Score | Mean polarity score from reviews |

### ✅ Interactive Filters / Slicers
- Category Filter
- Rating Filter
- App Type Filter (Free / Paid)
- Install Range Filter
- Content Rating Filter

### ✅ Interactive Visualizations

| # | Visualization | Description |
|---|---|---|
| 1 | **Rating vs Reviews** | Clustered column & line chart for top categories |
| 2 | **Global Installs Map** | Interactive map with install distribution by category |
| 3 | **Free vs Paid Analysis** | Dual-axis revenue & installs comparison |
| 4 | **Installs Trend** | Time-series growth analysis |
| 5 | **Bubble Chart** | App size vs rating, bubble size = installs |
| 6 | **Stacked Area Chart** | Cumulative installs with category contribution |

---

## 🎨 Dashboard Design Highlights

- 🎨 Google-themed color palette
- 📱 Interactive and responsive visualizations
- 🧹 Clean and professional layout
- 💼 Business-focused analytics design
- 🔍 Advanced filtering and exploration support

---

## 📌 Key Insights

> 💡 Here are some important findings from the analysis:

- 🆓 **Free apps dominate** the Play Store ecosystem
- 📡 **Communication and Social** categories lead in total installs
- ⭐ **Highly rated apps** tend to have significantly larger install counts
- 💬 **Sentiment polarity positively correlates** with app ratings
- 💰 **Revenue is concentrated** among a few top categories
- 📈 App category installs show **consistent growth over time**

---

## 🚀 Dashboard Deployment

The dashboard was published using **Power BI Service** for public access.

### 🔗 Live Dashboard
[![Power BI](https://img.shields.io/badge/View%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://app.powerbi.com/links/0Gssa2bXOm?ctid=8dbd2884-120c-413b-80b2-1117dd3469a4&pbi_source=linkShare)

---

## 👤 Author

<table>
  <tr>
    <td align="center">
      <b>Om Chauhan</b><br>
      <i>Data Analyst | Python Developer</i>
    </td>
  </tr>
</table>

### 🌐 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/om-chauhan-21043824b/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/OmChauhan07)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/omchauhan79)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:odchauhan0702@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://omchauhan.vercel.app/)

---




<p align="center">
  ⭐ If you found this project helpful, consider giving it a star!
</p>
