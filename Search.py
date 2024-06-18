import os
import pandas as pd

def extract_rows_with_value(root_dir, column, search_value):
    extracted_rows = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:
                    # Attempt to read the file with 'latin1' encoding
                    df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)

                    # Ensure the column to check is present in the dataframe
                    if column not in df.columns:
                        print(f"File {filename} is missing column: {column}")
                        continue

                    # Apply search criteria
                    matching_rows = df[df[column] == search_value]

                    # Print matching rows
                    if not matching_rows.empty:
                        print(f"\nMatching rows in file: {filename}")
                        print(matching_rows)

                except Exception as e:
                    print(f"Error processing file {filename}: {e}")

if __name__ == "__main__":
    root_directory = "C:\\Users\\Administrator\\Documents\\PBI Data Test"  # Change this to the root directory you want to search
    column_to_search = "DistributorID"  # Column to search in
    search_value = 15582315  # Value to search for
    extract_rows_with_value(root_directory, column_to_search, search_value)
