# 🧬 Cancer Gene Expression Classification from Saliva Data

This project explores whether gene expression profiles extracted from saliva samples can be used to distinguish between different types of cancer using machine learning.

The dataset is processed from raw microarray-style gene expression data, cleaned, transformed, and prepared for ML model training.

---

## 🎯 Project Goal

To build a machine learning pipeline that can classify cancer types (and healthy controls) using gene expression signals.

In particular, this project focuses on:

- Pancreatic cancer
- Lung cancer
- Breast cancer
- Gastric cancer
- Healthy controls

---

## ⚙️ Pipeline Overview

The workflow follows these stages:

### 1. Data Preprocessing
- Raw gene expression data loaded
- Probe IDs mapped to gene symbols using annotation file
- Missing values removed
- Duplicate gene symbols handled

### 2. Feature Engineering
- Gene-level filtering using top combined gene sets
- Removal of ambiguous multi-mapped gene entries
- Filtering based on gene name quality constraints
- Final transformation into sample × gene matrix

### 3. Data Transformation
- Transposition of dataset to ensure:
  - Rows = samples
  - Columns = gene features
- Final dataset prepared for ML input

### 4. Label Construction
- Samples labeled as:
  - `1` → Cancer
  - `0` → Healthy control

---

## 📊 Dataset Structure

After preprocessing:

- Rows: ~24–N samples per cancer type
- Columns: Gene expression features (~reduced set of high-quality genes)

Example structure:

| Sample | KRAS | TRIM14 | ZNF503 | PAPPA | ... |
|--------|------|--------|--------|--------|-----|
| Sample-1 | 0.0 | 24.9 | 0.28 | 344.1 | ... |
| Sample-2 | 0.0 | 0.12 | 1.91 | 426.8 | ... |

---

## 🧠 Machine Learning Objective

The cleaned dataset is designed for:

- Binary classification (Cancer vs Healthy)
- Potential extension to multi-class cancer classification
- Feature importance analysis for biological insight

---

## 🧪 Methods Used

- Pandas (data manipulation)
- NumPy (numerical operations)
- Gene symbol mapping via annotation merge
- Feature filtering and thresholding
- Data normalization-ready structure (future step)

---


---

## 🚧 Current Status

✔ Data cleaning pipeline complete  
✔ Gene mapping integrated  
✔ Feature filtering implemented  
✔ Dataset successfully structured for ML  

⏳ Next steps:
- Train/test split
- Feature scaling
- Model training (Logistic Regression / Random Forest / SVM)
- Evaluation and interpretation

---

## 🧬 Key Insight

This project investigates whether **saliva-based gene expression signatures** contain enough biological signal to differentiate cancer states — potentially contributing to non-invasive diagnostic approaches.

---

## ⚠️ Notes

- Gene expression data is high-dimensional and noisy
- Feature selection significantly impacts model performance
- Biological interpretability is prioritized alongside accuracy

---

## 🚀 Future Improvements

- Multi-class cancer classification
- Deep learning models (MLPs / Transformers for tabular data)
- SHAP-based feature importance analysis
- Expansion to larger public datasets (GEO / TCGA)

---

## 👨‍💻 Author

Student researcher exploring the intersection of:
- Machine Learning
- Genomics
- Computational Biology

---

## 📌 License

For educational and research use only.
```

---