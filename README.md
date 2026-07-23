# Student Sleep & Mental Health Prediction (2026)

An end-to-end Machine Learning classification project designed to analyze student sleep patterns, lifestyle factors, and predict mental health outcomes. Multiple algorithms were evaluated alongside Grid/Randomized Search hyperparameter tuning to achieve an optimized predictive accuracy of **~82.34%**.

---

## 🎨 Project UI Preview & Live Demo

![Streamlit Web App Preview](https://via.placeholder.com/800x400.png?text=Streamlit+App+UI+Screenshot)

🚀 **[Click Here to Access Live Streamlit App](https://your-streamlit-app-link.streamlit.app)**

---

## 📁 Repository Structure

```
Student-Sleep-Mental-Health-Prediction/
├── student_sleep_mental_health_2026.csv   # Dataset containing student sleep & mental health metrics
├── model.ipynb                             # Jupyter Notebook with EDA, Hyperparameter Tuning & Evaluation
├── model.pkl                               # Best performing trained classification model
├── scaler.pkl                              # Feature scaling object for normalization
├── columns.pkl                             # Saved column structure to ensure input alignment
└── README.md                               # Project documentation
```

---

## 🛠️ Hyperparameter Tuning Details (XGBoost)

Systematic hyperparameter search was conducted across 5-fold cross-validation (`split0` to `split4`) to optimize regularizations and sampling parameters (`colsample_bytree`, `subsample`, `reg_lambda`, `reg_alpha`):

- **Best Mean Test Score**: **0.823383 (~82.34%)**
- **Standard Deviation (std_test_score)**: **0.006858** _(high model stability across folds)_

---

End-to-end Machine Learning project predicting student mental health from sleep &amp; lifestyle metrics. Features EDA, 5-fold CV hyperparameter tuning (XGBoost/Logistic Regression ~83% accuracy), and an interactive Streamlit UI web app.
