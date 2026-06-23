# Cancer Gene Expression Classification from Salivary Biomarker Data

This project implements an advanced machine learning framework capable of detecting four specific cancers (Pancreatic, Lung, Gastric, and Breast) from salivary transcriptomic data (GPL570 microarray platform). 

By extracting biological signals from over 21,000 genes, this pipeline builds specialized binary "Expert" models to differentiate specific cancer profiles from a massive, consolidated healthy control group.

---

## Project Goal

To build a robust diagnostic pipeline that overcomes extreme class imbalances (hundreds of healthy controls vs. rare cancer patient samples) to accurately flag early transcriptomic indicators of malignancy using non-invasive liquid biopsies.

---

## Advanced Pipeline Architecture

The workflow has evolved into a highly automated, leakage-protected pipeline using `imbalanced-learn` and `scikit-learn`:

### 1. Data Preprocessing & Consolidation
- Raw microarray expression matrices are parsed and probe IDs are mapped to high-quality gene symbols.
- A **1-vs-All Master Control Pool** is constructed by aggregating healthy controls across multiple datasets into a unified background cohort (~250+ samples).

### 2. Algorithmic Feature Selection (LASSO)
- To prevent overfitting on high-dimensional noise, `LassoCV` regularizes the 21,000+ gene feature space down to minimal, mathematically stable, and clinically viable signatures (e.g., 7 targeted genes for the Pancreatic panel).

### 3. Missing Value & Scale Isolation
- **Median Imputation (`SimpleImputer`)**: Outliers or missing entries caused by multi-study array merging are safely resolved without destroying rare rows.
- **Z-Score Normalization (`StandardScaler`)**: Features are centered and scaled to preserve relative variance.

### 4. Synthetic Over-sampling (SMOTE)
- To combat the "Small N Pool" issue (e.g., 5–7 rare pancreatic samples), **SMOTE** is embedded directly into the cross-validation loop. 
- It dynamically synthesizes rare clinical profiles along minority class feature vectors using localized spatial parameters (`k_neighbors=2`), forcing the models to learn geometric boundaries instead of guessing the majority class.

---

## Workflow & Optimization Strategy

The pipeline optimizes hyperparameters dynamically across all expert panels using a parallelized loop structure:

```
[ Raw Train Data ] ──> [ Median Imputer ] ──> [ StandardScaler ] ──> [ SMOTE (k=2) ] ──> [ Optimized Model ] │ [ Untouched Raw Test Data ] <────────────┘
```

- **Cross-Validation**: 5-Fold Repeated Stratified Cross-Validation (`RepeatedStratifiedKFold`, 3 repeats) ensures every genuine patient profile serves as both a training and validation anchor.
- **Scoring Priority**: Tuned via `RandomizedSearchCV` maximizing for **Recall** to minimize the clinical risk of false negatives.
- **Data Leakage Prevention**: By utilizing `imblearn.pipeline.Pipeline`, SMOTE is strictly applied *only* to training folds, leaving validation and hold-out test sets completely un-synthesized and pure.

---

## Model Selection & Evaluation Paradigms

The framework evaluates two distinct algorithmic behaviors per cancer type:

1. **Logistic Regression**: Utilizes aggressive L1/L2 penalties (`C` regularizers) to draw broad decision boundaries. Tends toward hyper-sensitivity (100% Recall) but accepts higher false-alarm rates.
2. **Random Forest**: Constructs complex, non-linear decision trees. Demonstrates balanced, honest diagnostic capabilities—maintaining exceptionally high Specificity alongside strong Recall.

---

## Technical Stack

- **Core Engine**: Python 3
- **Data Wrangling**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn (`sklearn`)
- **Imbalance Analytics**: Imbalanced-Learn (`imblearn`)
- **Visualization**: Matplotlib (Feature Importance Mapping)

---

## Current Status

✔ Data cleaning, probe mapping, and Master Control consolidation complete.  
✔ LASSO feature selection successfully reduced features to optimal target counts.  
✔ Cross-validation engine with integrated internal SMOTE pipeline fully operational.  
✔ Multi-cancer automated hyperparameter loop implemented with unique tracking indices.  
✔ Real-world hold-out test evaluation completed on completely raw patient profiles.  

---

## Key Research Insight

Standard machine learning models completely collapse when confronted with rare-disease datasets, defaulting to a 0% Recall rate by guessing the healthy majority. Introducing cross-validation-isolated SMOTE with localized neighborhood constraints unlocks genuine predictive power, allowing ensemble models like Random Forests to identify true salivary cancer biomarkers with high specificity.

---

## Active Horizons & Next Steps

- **Serialized Compression**: Implement `joblib` object serialization to dump optimized `best_estimator_` pipelines directly to disk, removing training overhead.
- **SHAP Integration**: Transition basic feature importance charts to SHAP (SHapley Additive exPlanations) values to visualize exactly how individual genes drive specific patient predictions.
- **Cross-Diagnostic Screening**: Test individual expert models against *other* cancer test pools to evaluate true cross-disease diagnostic specificity.

---

## Author

Student researcher exploring the intersection of Genomics, Computational Biology, and Imbalanced Machine Learning Paradigms.

---

## License

For educational and research use only.
