# Predicting 30-day ED representation using Machine Learning
# Dataset: MIMIC-IV

## Process diagnosis.csv file
Run the diagnosis_processing.py script to convert all diagnosis coded to ICD-10 (the raw data include a mixture of both ICD-9 and ICD-10), and classify all diagnoses into categories.

```bash
python3 diagnosis_processing.py
```

## Generate the ED dataset using mainly the files from MIMIC-IV-ED
```bash
python3 ED_preprocessing.py
```

## Discretise and normalise the dataset
```bash
python3 discretise_normalised.py
```

## Next step
fully_processed_ED.csv is the final dataset.
