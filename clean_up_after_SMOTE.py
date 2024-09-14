import pandas as pd
from ED_preprocessing import generate_csv

ED_SMOTE_PATH = "GeneratedData/ED_SMOTE.csv"
OUT_PATH = "GeneratedData/Cleaned_ED_SMOTE.csv"

edstays = pd.read_csv(ED_SMOTE_PATH)

edstays['n_ed_visits'] = edstays['n_ed_visits'].round().astype(int)
edstays['acuity'] = edstays['acuity'].round().astype(int)
edstays['n_ed_admissions'] = edstays['n_ed_admissions'].round().astype(int)

# # List the distinct values
# distinct_values = edstays['n_ed_visits'].unique()
# print("\nDistinct Values n_ed_visits:")
# print(distinct_values)

# distinct_values = edstays['n_ed_admissions'].unique()
# print("\nDistinct Values n_ed_admissions:")
# print(distinct_values)

# distinct_values = edstays['acuity'].unique()
# print("\nDistinct Values acuity:")
# print(distinct_values)

generate_csv(edstays, OUT_PATH)
