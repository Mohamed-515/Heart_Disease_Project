# ❤️ Heart Disease Prediction (UCI Dataset)

## 📖 Project Overview
This project is a **Comprehensive Machine Learning Pipeline** built on the **UCI Heart Disease dataset**.  
It covers data preprocessing, dimensionality reduction, feature selection, supervised & unsupervised learning, model optimization, and deployment with Streamlit & Ngrok.

## 🛠️ Features
- Data preprocessing & cleaning (missing values, encoding, scaling)
- PCA for dimensionality reduction
- Feature selection (Random Forest importance, RFE, Chi-Square)
- Supervised models: Logistic Regression, Decision Tree, Random Forest, SVM
- Unsupervised models: K-Means, Hierarchical Clustering
- Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
- Model export (.pkl) and Streamlit UI for predictions

## ▶️ How to run locally
1. (Optional) clone: `git clone https://github.com/Mohamed-515/Heart_Disease_Project.git`
2. `cd Heart_Disease_Project`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run ui/app.py`
5. App opens at: `http://localhost:8501`

## 🌍 Share with Ngrok
1. Run app: `streamlit run ui/app.py`
2. Start tunnel: `ngrok http 8501`  
3. Share the ngrok public URL.

## 📊 Results
- Best Model: SVM (ROC-AUC ≈ 0.976)
- Accuracy ≈ 93%, Precision ≈ 90%, Recall ≈ 96%

## Dataset
UCI Heart Disease Dataset: https://archive.ics.uci.edu/ml/datasets/heart+Disease

## Author
Developed as part of AI & ML SprintUP Graduation Project
