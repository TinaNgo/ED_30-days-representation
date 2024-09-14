# Predicting 30-day ED representation using Machine Learning
# Dataset: MIMIC-IV

## Process 
```bash
python3 diagnosis_processing.py
```

```bash
python3 ED_proprocessing.py
```

```bash
python3 discretise.py
```

```bash
python3 apply_smote.py <path to config.ini>
```


python3 weka_evaluate.py <path to config.ini>
