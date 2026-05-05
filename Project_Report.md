# Detailed Project Walkthrough: Fraud Detection System

This report provides a step-by-step technical explanation of every action performed in the `final_project.ipynb` notebook to achieve a 99% accuracy fraud detection model.

---

## Phase 0: Feature Correlation Analysis
Before building the model, we analyzed how each column relates to the target variable (`isFraud`) to identify the most important "Red Flags."

| Feature | Correlation Type | Why it matters? |
| :--- | :--- | :--- |
| **amount** | High Positive | Fraudulent transactions are usually much larger than normal ones. |
| **oldbalanceOrg** | High Positive | Accounts with large sums are targeted more often. |
| **newbalanceOrig** | High Negative | Fraud almost always leaves the sender's account with a **$0.00** balance. |
| **type** | Critical | Fraud patterns only exist in `TRANSFER` and `CASH_OUT` transactions. |

---

## Phase 1: Data Exploration (The "Investigation" Phase)

In the first part of your notebook, you focused on understanding the raw data. Here is exactly what those steps achieved:

### 1. Loading the Data (`pd.read_csv`)
We imported the **6.3 million** transactions from the CSV file. This is a massive dataset, which influenced our later choice of a fast model (Decision Tree).

### 2. Initial Inspection (`.head()`, `.shape`, `.columns`)
*   **`.head()`**: You viewed the first 5 rows to understand the features (Step, Type, Amount, etc.).
*   **`.shape`**: This confirmed the scale of the project: **6,362,620 rows** and **11 columns**.
*   **`.columns`**: Listed the headers to identify which are useful (like `amount`) and which are just IDs (like `nameOrig`).

### 3. Data Integrity Check (`.info()`, `.isnull()`)
*   **`.info()`**: This revealed that we have 3 text columns (Object) and 8 number columns (Float/Int).
*   **`.isnull().sum()`**: This was a vital check. It confirmed there were **zero null values**, meaning the dataset was high quality and didn't need any complex data filling.

### 4. Statistical Analysis (`.describe()`)
This cell provided the "Proof of Skewness." 
*   By looking at the **Mean** vs the **Max** in the `amount` column, we saw that the average transaction is ~$180k, but the max is over **$92 million**. 
*   **Conclusion:** This proved the data was not normalized and needed **Standard Scaling**.

### 5. Unique Value Analysis (`.nunique()`, `.unique()`)
Checking the unique values of `amount` showed over **5.3 million unique price points**, confirming that the transaction data is extremely granular and detailed.

### 6. Target Analysis (`.value_counts()`)
By running this on `isFraud`, we found:
*   **Safe Transactions (0):** 6,354,407
*   **Fraud Transactions (1):** 8,213
*   **Insight:** This is a "Highly Imbalanced" problem. Only **0.13%** of data is fraud. This is why we need a powerful classifier like the Decision Tree to "hunt" for these rare cases.

---

## Phase 2: Data Preprocessing (The "Cleaning" Phase)

### 7. Visualization (`distplot`)
We used Seaborn to plot the columns. As identified in the `describe()` step, the graphs showed that the data was bunched up on one side (Skewed). This confirmed that the data was **not normalized** at the start.

### 8. Encoding & Scaling
*   **LabelEncoder**: We turned text like "TRANSFER" and "CASH_OUT" into numbers so the math model could read them.
*   **StandardScaler**: This is what finally **normalized** the data. It brought the millions of dollars and the small step numbers onto the same "Standard Scale" (mean 0, std 1).

---

## Phase 3: Machine Learning (The "Prediction" Phase)

### 9. Why Decision Tree?
We chose the **Decision Tree** over models like SVM or Logistic Regression because:
1.  **Speed**: It can process 6 million rows in seconds.
2.  **Accuracy**: It is excellent at picking out the rare 8,213 fraud cases from the millions of safe ones.
3.  **Human Logic**: It creates a flow-chart of rules that makes it easy to explain why a fraud was caught.

### 10. Final Evaluation
We split the data (80% train / 20% test) to ensure the model could predict **new** data it had never seen before. The result was a **99.9% accuracy rate**, successfully completing the project requirements.



3. WHY WE USE DECISION TREE (VS OTHER MODELS)
---------------------------------------------
We chose a Decision Tree because it is the most effective tool for this specific 6-million-row dataset. Here is how it compares to others:

- VS LOGISTIC REGRESSION: Logistic Regression assumes a straight-line relationship. Fraud is complex and follows "branching" rules, which only a Decision Tree can capture.
- VS SVM (SUPPORT VECTOR MACHINE): SVM is very powerful but extremely slow. With 6.3 million rows, an SVM would take hours or even days to run. A Decision Tree finishes in seconds.
- VS RANDOM FOREST: While Random Forest is great, it is a collection of many trees. For this dataset, a single Decision Tree already hits 99% accuracy. Using a Random Forest would be "overkill"—it would be slower and use more memory without giving much better results.
- HUMAN-LIKE LOGIC: Decision Trees work by asking questions like "Is the amount > 200k?" then "Is the balance 0?". This mimics how a human investigator would check for fraud, making the model very reliable and easy to explain.
