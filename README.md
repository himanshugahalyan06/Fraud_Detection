# 🛡️ FraudGuard AI: Financial Intelligence Dashboard

A high-performance machine learning system designed to detect fraudulent transactions in real-time. Built with a **Balanced Decision Tree** model, this project achieves **99.9% accuracy** on a dataset of 6.36 million financial records.

## 🚀 Key Features
- **Premium UI:** Midnight Dark Glassmorphism theme with modern typography.
- **Real-time Detection:** Instant classification of transactions as `SAFE` or `FRAUD`.
- **Parameter Analysis:** Detailed reasoning for every prediction (e.g., account drain detection).
- **No Bias:** Trained with balanced class weights to handle extreme data skew.

## 🛠️ Tech Stack
- **Engine:** Python, Scikit-learn, Pandas, NumPy
- **Dashboard:** Streamlit
- **Model:** DecisionTreeClassifier (Balanced)

## 📁 Project Structure
- `app.py`: The main Streamlit dashboard.
- `final_project.ipynb`: Exploratory Data Analysis & Model Training logic.
- `Project_Report.md`: Technical documentation and correlation analysis.
- `model_data.pkl`: Serialized model and scaler.

## ⚙️ Installation & Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install streamlit pandas scikit-learn numpy
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

---
*Developed for ML & Pattern Recognition*
