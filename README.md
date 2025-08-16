# 🛡️ Anti-Phishing Detection Pipeline

This repository contains an end-to-end machine learning pipeline for detecting phishing attacks using real-world data stored in MongoDB Atlas. The pipeline automates data ingestion, validation, transformation, model training, and deployment using FastAPI. It also integrates MLflow and DagsHub for experiment tracking.

---

## 📦 Pipeline Components

### 1. 📥 Data Ingestion
- Connects to **MongoDB Atlas** (cloud-based NoSQL database).
- Fetches anti-phishing data into the local working directory.
- Automatically splits the dataset into **training** and **testing** sets.

### 2. ✅ Data Validation
- Ensures data quality by validating:
  - Number of columns
  - Data types
  - Schema consistency
- Detects **data drift** between training and testing datasets.

### 3. 🔄 Data Transformation
- Applies preprocessing steps including:
  - **KNNImputer** to handle missing values
  - Scaling and feature preparation
- Saves the transformation pipeline as a `.pkl` file for inference.

### 4. 🤖 Model Training
- Trains multiple classifiers using **GridSearchCV**:
  - Random Forest, Gradient Boosting, Logistic Regression, AdaBoost, etc.
- Selects the best model based on **accuracy**.
- Saves the trained model to a specified directory.
- Uses **MLflow** for local tracking and **DagsHub** for remote experiment tracking.

### 5. 🚀 Model Serving with FastAPI
- Exposes API endpoints for:
  - **Automated model training**
  - **Batch predictions**
- Loads saved preprocessor and model for inference.

---

## 🧠 Problem Context: Anti-Phishing Detection

Phishing is a form of cybercrime where attackers impersonate trusted entities to deceive individuals into revealing sensitive information such as passwords, credit card numbers, or bank account details.

This system aims to detect such phishing attempts based on behavioral and structural features extracted from emails, URLs, or web content—helping organizations defend against these threats.

---

## 🗃️ Dataset

- Stored in **MongoDB Atlas**
- Contains a variety of phishing-related features:
  - URL-based features
  - HTTPS and SSL certificate flags
  - Anchor tag and redirection behavior
  - Domain-based metrics
- Binary classification: **phishing** or **legitimate**

---

## 🛠️ Tech Stack

| Task              | Tool/Library             |
|-------------------|--------------------------|
| Data Storage      | MongoDB Atlas            |
| Experiment Tracking | MLflow + DagsHub      |
| Data Processing   | Pandas, NumPy, Scikit-learn |
| Modeling          | Scikit-learn, GridSearchCV |
| Serving           | FastAPI                  |
| Deployment Ready  | Uvicorn                  |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/anti-phishing-pipeline.git
cd anti-phishing-pipeline
```

### 2. Install dependencies 
```bash
pip install -r requirements.txt
```

### 3. GitHub Actions 
--> used for github actions to automate the deployment of the model to the cloud AWS EC2 instance