import pandas as pd
from ED_preprocessing import generate_csv

def load_and_filter_dataframe(directory_in, directory_out, col_list):
    """
    Loads a DataFrame from a CSV file and keeps only the specified columns.
    
    :param csv_filepath: Path to the CSV file.
    :param col_list: List of columns to keep.
    :return: Filtered DataFrame containing only the specified columns.
    """
    # Load the CSV into a DataFrame
    test_df = pd.read_csv(directory_in + 'test.csv')
    train_df = pd.read_csv(directory_in + 'train.csv')
    
    # Keep only the specified columns
    filtered_test_df = test_df[col_list]
    filtered_train_df = train_df[col_list]
    
    generate_csv(filtered_test_df, directory_out + 'test.csv')
    generate_csv(filtered_train_df, directory_out + 'train.csv')

def main():
    # Define the file path and the columns to keep
    directory_in = "TrainTestData/NO_FS/"
    
	# Manual Feature Selection by Michael
    directory_out = "TrainTestData/Manual_FS/"
    col_list = ["gender", "separation_mode", "diagnosis_category", "age", "triage_category", "revisited"]
   
    # Load and filter the DataFrame
    filtered_df = load_and_filter_dataframe(directory_in, directory_out, col_list)
    

if __name__ == "__main__":
    main()
