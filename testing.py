import pandas as pd
# from datetime import datetime, timedelta

# def get_n_ed_visits(edstays):
# 	print("Calculating number of ED visits within the past year.....")
# 	# Initialize the n_edstays column

# 	edstays['n_edstays'] = 0

# 	# Group by subject_id
# 	grouped = edstays.groupby('subject_id')

# 	# Calculate the rolling count of visits within 365 days
# 	for name, group in grouped:
# 		group['n_edstays'] = group.rolling('365D', on='intime').count()['stay_id'] - 1
# 		edstays.loc[group.index, 'n_edstays'] = group['n_edstays']
# 	return edstays

# # def get_n_ed_admissions(edstays):
# # 	print("Calculating number of admissions via the ED within the past year.....")
# # 	# Initialize the n_edstays column
# # 	edstays['n_ed_admissions'] = 0

# # 	for i, row in edstays.iterrows():
# # 		# Get all entries for the same subject within the past year
# # 		past_year_admissions = edstays[(edstays['subject_id'] == row['subject_id']) &
# # 									(edstays['intime'] < row['intime']) &
# # 									(edstays['intime'] > row['intime'] - pd.Timedelta(days=365)) &
# #             						(edstays['separation_mode'] == 'Admit')]
		
# # 		# Count the number of visits
# # 		edstays.at[i, 'n_ed_admissions'] = len(past_year_admissions)
# # 	return edstays

# def get_n_ed_admissions(edstays):
#     print("Calculating number of admissions via the ED within the past year.....\n")

#     # Initialize the n_ed_admissions column
#     edstays['n_ed_admissions'] = 0

#     # Group by subject_id
#     grouped = edstays.groupby('subject_id')

#     for name, group in grouped:
#         # Sort the group by 'intime' to ensure correct order
#         group = group.sort_values('intime')
        
#         # Loop through each stay in the group
#         for i in range(len(group)):
#             current_intime = group.iloc[i]['intime']
            
#             # Define the time window (365 days before the current stay)
#             start_window = current_intime - pd.Timedelta(days=365)
            
#             # Count the number of admissions in that window
#             admissions_count = group[(group['intime'] > start_window) & 
#                                      (group['intime'] < current_intime) & 
#                                      (group['separation_mode'] == 'admitted')].shape[0]
            
#             # Assign the count to the current stay
#             edstays.loc[group.index[i], 'n_ed_admissions'] = admissions_count

#     return edstays

# # Create a sample dataset with subject_id, intime, and separation_mode
# data = {
#     'subject_id': [1]*7 + [2]*7,
#     'stay_id': list(range(1, 15)),
#     'intime': [
#         '2025-07-30 08:00:00',  # 7 days ago
#         '2024-07-31 08:00:00',  # 8 days ago
#         '2024-07-30 08:00:00',  # 9 days ago
#         '2024-07-29 08:00:00',  # 10 days ago
#         '2024-07-28 08:00:00',  # 11 days ago
#         '2024-07-27 08:00:00',  # 12 days ago
#         '2024-07-26 08:00:00',  # 13 days ago
#         '2024-08-01 08:00:00',  # 7 days ago
#         '2024-07-31 08:00:00',  # 8 days ago
#         '2024-07-30 08:00:00',  # 9 days ago
#         '2024-07-29 08:00:00',  # 10 days ago
#         '2024-07-28 08:00:00',  # 11 days ago
#         '2024-07-27 08:00:00',  # 12 days ago
#         '2024-07-26 08:00:00'   # 13 days ago
#     ],
#     'separation_mode': [
#         'admitted', 'Discharge', 'admitted', 'admitted', 'Discharge', 'admitted', 'Discharge',
#         'admitted', 'Discharge', 'admitted', 'admitted', 'Discharge', 'admitted', 'Discharge'
#     ]
# }

# df = pd.DataFrame(data)

# # Convert the 'intime' column to datetime
# df['intime'] = pd.to_datetime(df['intime'])
# df = df.sort_values(by=['subject_id', 'intime'])

# df = get_n_ed_visits(df)
# df = get_n_ed_admissions(df)
# print(df)

# edstays = pd.read_csv("GeneratedData/ED_SMOTE.csv")
edstays = pd.read_csv("GeneratedData/full_discritised_ED.csv")


distinct_counts = edstays['n_ed_visits'].value_counts()

# List the distinct values
distinct_values = edstays['n_ed_visits'].unique()

print("Distinct Counts:")
print(distinct_counts)
print("\nDistinct Values:")
print(distinct_values)
