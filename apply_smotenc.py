import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTENC
from ED_preprocessing import generate_csv


def apply_smotenc(original_train_file, out_path):
    # Load dataset
    df = pd.read_csv(original_train_file)
    # df = df.head(5000)

    X = df.drop(columns='revisited')
    y = df['revisited']


    # For Full Feature Dataset
    categorical_features = ['gender', 'separation_mode', 'race', 'arrival_mode', 'diagnosis_category', 'age', 'presentation_time', 'ED_LOS',
                        'triage_category', 'triage_pain']
    
    chiefcom_columns = [col for col in X.columns if "chiefcom" in col]
    categorical_features.extend(chiefcom_columns)
   
    categorical_features1 = []
    for col in categorical_features:
        if col in X.columns:
            categorical_features1.append(col)

    categorical_features = categorical_features1

    # Print the sizes of the splits
    print(f"Training set before applying SMOTE_NC size: {X.shape}\n")

    print("Class distribution in training set before SMOTENC:")
    print(y.value_counts())

    # Get categorical feature indices for SMOTENC
    categorical_features_indices = [list(X.columns).index(col) for col in categorical_features]

    # Apply SMOTENC to training set
    print("\nApplying SMOTENC to training set.....\n")
    smote_nc = SMOTENC(categorical_features=categorical_features_indices, random_state=42)
    X_train_resampled, y_train_resampled = smote_nc.fit_resample(X, y)

    print("\nClass distribution in trainning set after SMOTENC:")
    print(y_train_resampled.value_counts())

    # merge X and y
    X_train_resampled['revisited'] = y_train_resampled
    generate_csv(X_train_resampled, out_path + 'train_SMOTE.csv')

def main():
    # Change these varibles to generate smote for a different file.
	# original_train_file = 'TrainTestData/NO_FS/train.csv'
	# out_path = 'TrainTestData/NO_FS/'
	
    # CFS dataset
    # original_train_file = 'TrainTestData/CFS/train.csv'
    # out_path = 'TrainTestData/CFS/'

    # Information Gain dataset
    original_train_file = 'TrainTestData/InfoGain/train.csv'
    out_path = 'TrainTestData/InfoGain/'
    
    apply_smotenc(original_train_file, out_path)

if __name__ == "__main__":
	main()