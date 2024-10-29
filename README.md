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

fully_processed_ED.csv is the result dataset.

## Generate full features train and test set
This split fully_processed_ED.csv into train-test set (80-20).

```bash
python3 get_train_test.py
```

## Perform feature selections on the train set
I did this using Weka, but it could also be done via code.

## Generate the balanced train sets using SMOTE-NC or SMOTE-N
SMOTE-NC for datasets containing both nominal and continuous features
SMOTE-N for datasets containing only nominal features

```bash
python3 apply_smotenc.py
python3 apply_smoten.py
```


## Next step
.
