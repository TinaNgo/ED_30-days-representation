import pandas as pd
import argparse
from sklearn.model_selection import StratifiedKFold
from imblearn.over_sampling import SMOTENC


def main(input_file_path):
    # Load dataset
    df = pd.read_csv(input_file_path)
    # df = df.head(100)
    print(df.shape[0])
    df = df.dropna()
    print(df.shape[0])


    # Fill all missing values with NaN
    # df = df.fillna('NaN')

#     # Define your feature set (X) and target (y)
#     X = df.drop('revisited', axis=1)  # Replace 'target_column' with your actual target column name
#     y = df['revisited']

#     # Replace categorical_features_indices with the index positions of your categorical columns
#     categorical_col = ['gender', 'separation_mode', 'race', 'arrival_mode', 'diagnosis_category', 'age', 'presentation_time', 'ED_LOS',
#                        'triage_category', 'triage_pain', 'last_pain']
#     categorical_features_indices = [list(X.columns).index(col) for col in categorical_col]  # Modify with your actual categorical column names

#     smote_nc = SMOTENC(categorical_features=categorical_features_indices, random_state=42)
#     skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

#     for fold, (train_index, test_index) in enumerate(skf.split(X, y), 1):
#         # Separate training and test sets
#         X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#         y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
#         # Apply SMOTENC to the training data
#         X_resampled, y_resampled = smote_nc.fit_resample(X_train, y_train)
#         print(f"Original X_train size for fold {fold}: {X_train.shape}")
#         print(f"Resampled X_train size for fold {fold}: {X_resampled.shape}")
        
#         # Save the resampled training data to CSV
#         train_data = pd.DataFrame(X_resampled, columns=X.columns)
#         train_data['revisited'] = y_resampled  # Add the target column
#         train_data.to_csv(f'TrainFolds/train_fold_{fold}.csv', index=False)
        
#         # # Save the test data (no resampling applied to test set)
#         test_data = X_test.copy()
#         test_data['revisited'] = y_test  # Add the target column
#         test_data.to_csv(f'TestFolds/test_fold_{fold}.csv', index=False)
        
#         print(f"Fold {fold} resampled training and test data saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some parameters.")
    parser.add_argument('param1', type=str, help='The first parameter')

    args = parser.parse_args()
    main(args.param1)