import os
import pandas as pd


def find_and_replace_in_files(root_dir, columns, search_value, replace_value):
    total_changes = 0
    modified_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:
                    # specify the correct encoding if known
                    df = pd.read_csv(filepath, encoding='latin1', low_memory=False)
                    changes = 0

                    # Ensure columns to check are present in the dataframe
                    missing_columns = [col for col in columns if col not in df.columns]
                    if missing_columns:
                        print(f"File {filename} is missing: {missing_columns}")
                        continue

                    # Perform find and replace
                    for column in columns:
                        if column in df.columns:
                            changes_in_col = df[column].apply(lambda x: isinstance(x, str) and x == search_value).sum()
                            df[column] = df[column].replace(search_value, replace_value)
                            changes += changes_in_col

                    # If any changes were made, save the modified file
                    if changes > 0:
                        df.to_csv(filepath, index=False, encoding='latin1')
                        modified_files.append(filepath)
                        total_changes += changes
                        print(f"Modified {changes} occurrences in file: {filename}")

                except Exception as e:
                    print(f"Error processing file {filename}: {e}")

    print(f"\nTotal changes made: {total_changes}")
    print("Modified files:")
    for file in modified_files:
        print(file)


if __name__ == "__main__":
    root_directory = "C:\\Users\\Administrator\\Documents\\PBI Data Test"  # Change this to the root directory you want to search
    columns_to_check = ["OutletID"]  # Columns to search in
    search_value = 'ID-'  # Value to search for
    replace_value = 'ID -'  # Value to replace with

    find_and_replace_in_files(root_directory, columns_to_check, search_value, replace_value)
