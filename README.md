# 📚 Data Science Projects

A collection of my data science projects.

## Projects
- [Breast Cancer Analysis](BreastCancer/) — Tumor classification using ML.
- # Breast Cancer Project
- # 🩺 Breast Cancer Data Science Project

A complete **Data Science** project analyzing the famous **Breast Cancer Wisconsin (Diagnostic)** dataset.  
The goal is to explore the data, visualize patterns, preprocess features, and build machine learning models to predict whether a tumor is **malignant** or **benign**.

---

## 📂 Dataset Information
- **Rows:** 569
- **Columns:** 32 (after cleaning)
- **Target column:** `diagnosis`  
  - `M` = Malignant (cancerous)  
  - `B` = Benign (non-cancerous)  
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)

---

## 🔍 Project Workflow
1. **Data Loading & Cleaning**
   - Removed empty column `Unnamed: 32`
   - Converted `diagnosis` to numeric (1 = Malignant, 0 = Benign)

2. **Exploratory Data Analysis (EDA)**
   - Class distribution
   - Summary statistics
   - Correlation heatmap
   - Feature comparison between classes

3. **Data Preprocessing**
   - Dropped `id` column
   - Standardized features

4. **Modeling**
   - Logistic Regression
   - Random Forest Classifier
   - Support Vector Machine (SVM)

5. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix
   - ROC Curve and AUC score

---

## 📊 Example Visualizations
### Correlation Heatmap
![heatmap](images/heatmap.png)

### Class Distribution
![class_distribution](images/class_distribution.png)

---

## 🧠 Model Performance (Test Set)

| Model                | Accuracy | Precision | Recall | F1-score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 0.96     | 0.95      | 0.96   | 0.95     |
| Random Forest        | 0.97     | 0.96      | 0.97   | 0.96     |
| SVM                  | 0.97     | 0.96      | 0.97   | 0.96     |

*(Numbers are for example — update after running your notebook)*

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/USERNAME/breast-cancer-analysis.git

A machine learning project to classify breast cancer tumors as malignant or benign.
Dataset: Breast Cancer Wisconsin (Diagnostic) from UCI Repository.
- [IMDB Review Analysis](IMDBReview/) — Sentiment analysis on IMDB movie reviews.
- [Student Performance Analysis](StudentPerformanceAnalysis/) — Predicting student scores.
