# 🧠 Postpartum Depression Analysis  

## 📖 Project Overview  
This project analyzes postpartum depression (PPD) using a dataset containing various features related to maternal health, psychological well-being, and socio-economic factors. The goal is to identify patterns, trends, and key indicators associated with PPD through **data preprocessing, exploratory data analysis (EDA), visualizations, and machine learning techniques**.  

By leveraging **Python, Pandas, Matplotlib, Seaborn, and Scikit-learn**, we aim to provide insights that could help in early diagnosis and intervention strategies.  

---

## 📊 Dataset Information  
- **Dataset Source:** https://www.kaggle.com/datasets/parvezalmuqtadir2348/postpartum-depression/data 
- **Comprehensive Dataset:** Utilizes a real-world dataset of 1,503 records collected from a medical hospital via a Google Form questionnaire.
- **Focused Analysis:** Examines 9 key attributes related to postpartum depression, with "Feeling Anxious" as the target variable. 

---

## 🔍 Analysis Performed  
1. **Data Preprocessing**  
   - Handled missing values and outliers.  
   - Encoded categorical variables.  
   - Standardized numerical features for better model performance.  

2. **Exploratory Data Analysis (EDA)**  
   - Identified trends and correlations between features.  
   - Examined distribution of depression scores.  
   - Visualized relationships using histograms, box plots, and scatter plots.  

3. **Feature Engineering & Selection**  
   - Identified key predictors contributing to postpartum depression.  
   - Applied correlation analysis to reduce multicollinearity.  

4. **Model Implementation**  
   - Trained machine learning models (e.g., Logistic Regression, Decision Tree, Random Forest).  
   - Evaluated models using accuracy, precision, recall, and F1-score.  

5. **Results & Insights**  
   - Discovered key risk factors for postpartum depression.  
   - Developed a predictive model to assess depression risk.  

---

## 🛠 Technologies Used  
- **Programming Language:** Python 🐍  
- **Libraries & Frameworks:**  
  - `pandas` - Data manipulation  
  - `numpy` - Numerical computations  
  - `matplotlib` & `seaborn` - Data visualization  
  - `scikit-learn` - Machine learning models  
  - `statsmodels` - Statistical analysis  
---
## Key Findings
- Developed a **Random Forest model with 99.34% accuracy** to predict postpartum depression based on key symptoms.

- Deployed the model on Streamlit Cloud. Try the live app: Try the live app: [Postpartum Health Analysis App](https://postpartum-health-analysis.streamlit.app/)

- Age & Emotional States: A strong correlation was found between younger age groups and higher levels of anxiety.

- Behavioral Patterns: Symptoms like trouble sleeping and appetite changes were strong indicators of postpartum depression.
---

## 🚀 Installation & Setup  

To run this project on your local machine:  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/Postpartum-Depression-Analysis.git
   cd Postpartum-Depression-Analysis
   
2. **Install required dependencies:**
```bash
  pip install -r requirements.txt
```

3. **Run the Jupyter Notebook:**
```bash
jupyter notebook
```

4. Open the notebook (Postpartum_Depression_Analysis.ipynb) and follow the analysis.
