import os
import pandas as pd


def find_non_numeric_values(root_dir, columns):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:

                    # specify the correct encoding if known
                    df = pd.read_csv(filepath, encoding='latin1', low_memory=False)
                    print(df.columns)

                    # Ensure columns to check are present in the dataframe
                    missing_columns = [col for col in columns if col not in df.columns]
                    if missing_columns:
                        print(f"File {filename} is missing: {missing_columns}")
                        continue
                    
                    # Check for non-numeric values in specified columns
                    non_numeric_rows = df[
                        ~df[columns].apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().all(axis=1)]
                    if not non_numeric_rows.empty:
                        print(f"File: {filename}")
                        print(non_numeric_rows)
                except Exception as e:
                    print(f"Error processing file: {e}")


if __name__ == "__main__":
    root_directory = "C:\\Users\\Administrator\\Documents\\PBI Data Test" \
                    # "Dashboard\\Monthly data dumps\\Secondary\\2024"  # Change this to the root directory you want
    # to search
    columns_to_check = ["DistributorID"]
    find_non_numeric_values(root_directory, columns_to_check)
