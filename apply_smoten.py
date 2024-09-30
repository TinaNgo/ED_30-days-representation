import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTEN
from ED_preprocessing import generate_csv

def apply_smoten(original_train_file, out_path):
    # Load dataset
    df = pd.read_csv(original_train_file)
    # df = df.head(5000)

    X = df.drop(columns='revisited')
    y = df['revisited']

    # For Full Feature Dataset (categorical features)
    # categorical_features = ['gender', 'separation_mode', 'race', 'arrival_mode', 'diagnosis_category', 'age', 'presentation_time', 'ED_LOS',
    #                     'triage_category', 'triage_pain']
    
    # chiefcom_columns = [col for col in X.columns if "chiefcom" in col]
    # categorical_features.extend(chiefcom_columns)
   
    # # Only keep the categorical features that exist in the dataset
    # categorical_features = [col for col in categorical_features if col in X.columns]

    # Print the sizes of the splits
    print(f"Training set before applying SMOTEN size: {X.shape}\n")

    print("Class distribution in training set before SMOTEN:")
    print(y.value_counts())

    # Apply SMOTEN to the training set
    print("\nApplying SMOTEN to training set.....\n")
    smote_en = SMOTEN(random_state=42)
    X_train_resampled, y_train_resampled = smote_en.fit_resample(X, y)

    print("\nClass distribution in training set after SMOTEN:")
    print(y_train_resampled.value_counts())

    # Merge X and y
    X_train_resampled['revisited'] = y_train_resampled
    generate_csv(X_train_resampled, out_path + 'train_SMOTE.csv')

def main():
    # Change these variables to generate SMOTE for a different file.
    original_train_file = 'TrainTestData/Manual_FS/train.csv'
    out_path = 'TrainTestData/Manual_FS/'
    
    apply_smoten(original_train_file, out_path)

if __name__ == "__main__":
    main()
