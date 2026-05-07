# 🛡️ FraudGuard AI: Financial Intelligence Dashboard

A high-performance machine learning system designed to detect fraudulent transactions in real-time. This project leverages advanced tree-based algorithms to achieve **99.9% accuracy** on a dataset of 6.36 million financial records, specifically optimized to handle extreme class imbalance.

## 🚀 Key Features
- **Premium UI:** Midnight Dark Glassmorphism theme with modern typography and real-time security signals.
- **Advanced Model Suite:** Comparative analysis across Logistic Regression, LDA, Decision Trees, and Random Forests.
- **Bias Mitigation:** Implements stratified sampling and focuses on **Recall** to minimize false-negative rates in fraud detection.
- **Persistence:** Models are serialized using `pickle` for instant deployment in the live dashboard.

## 🛠️ Tech Stack
- **Languages:** Python (3.8+)
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Dashboard:** Streamlit

## 📁 Project Structure
- `app.py`: The main interactive Streamlit dashboard for real-time security scans.
- `original analysis.ipynb`: **[FULL PROJECT CODE]** Comprehensive end-to-end analysis, including data acquisition, preprocessing, cross-validation, and model building.
- `final_project.ipynb`: Supporting research and exploratory data analysis.
- `Project_Report.md`: Technical documentation and deep-dive into model findings.
- `model_data.pkl`: Serialized Random Forest model and Scaler for production use.

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Fraud_Detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis:**
   Open `original analysis.ipynb` in Jupyter and run all cells to view model comparisons and generate the latest model file.

4. **Launch the Dashboard:**
   ```bash
   streamlit run app.py
   ```

---
*Developed for ML & Pattern Recognition*
