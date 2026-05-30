# Water Potability Prediction System

A Machine Learning-powered web application that predicts whether water is safe for drinking based on its physicochemical properties. The system is built using Python and deployed with Streamlit, allowing users to input water quality measurements and receive instant predictions.

## Overview

Water quality is a critical factor for public health. This project uses supervised machine learning algorithms to classify water samples as either:

- **Potable (Safe for Drinking)**
- **Non-Potable (Unsafe for Drinking)**

The prediction is based on several water quality indicators such as pH, hardness, dissolved solids, chloramines, sulfate concentration, conductivity, organic carbon, trihalomethanes, and turbidity.

---

##  Features

- Interactive Streamlit web application
- Real-time water potability prediction
- Multiple Machine Learning models available:
  - K-Nearest Neighbors (KNN)
  - Logistic Regression
  - Decision Tree
  - Support Vector Machine (SVM)
- Data preprocessing and feature scaling
- Class balancing using SMOTE
- Model performance evaluation and accuracy display
- User-friendly interface

---

## Input Parameters

The application uses the following water quality measurements:

| Feature | Description |
|----------|------------|
| pH | Measure of acidity or alkalinity |
| Hardness | Water hardness level |
| Solids | Total dissolved solids |
| Chloramines | Chloramine concentration |
| Sulfate | Sulfate concentration |
| Conductivity | Electrical conductivity |
| Organic Carbon | Organic carbon content |
| Trihalomethanes | Trihalomethane concentration |
| Turbidity | Cloudiness of water |

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Imbalanced-Learn (SMOTE)
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## Project Structure

```text
Water-Potability-Prediction/
│
├── app.py
├── project.ipynb
├── data/
│   └── water_quality.csv
│
├── models/
│   ├── knn_model.pkl
│   ├── logistic_model.pkl
│   ├── decisiontree_model.pkl
│   └── svm_model.pkl
│
├── requirements.txt
└── README.md
```

---

## Installation & Setup

###  Clone the Repository

```bash
git clone https://github.com/zziad11/Water-Potability-Prediction.git
cd water-potability-prediction
```

###  Create a Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn imbalanced-learn matplotlib seaborn joblib
```

---

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After running the command, Streamlit will generate a local URL similar to:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser to access the application.

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Label Encoding
4. Feature Scaling using StandardScaler
5. Handling Class Imbalance using SMOTE
6. Model Training
7. Model Evaluation
8. Deployment with Streamlit

---

## Available Models

The application supports multiple classification models:

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Decision Tree Classifier
- Support Vector Machine (SVM)

Users can select a model from the sidebar and compare prediction results.

---

## How to Use

1. Launch the application.
2. Select a Machine Learning model from the sidebar.
3. Enter the required water quality parameters.
4. Click **"Get the Result"**.
5. View the prediction:
   - Suitable for Drinking
   - Not Suitable for Drinking
6. Review the model accuracy displayed with the result.

---





**Ziad Mohamed**
