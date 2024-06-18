import os
import pandas as pd


def find_and_replace_in_files(root_dir, criteria, search_value, replace_value):
    total_changes = 0
    modified_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:
                    df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)  # specify the correct encoding if known
                    changes = 0

                    # Check if the file meets the criteria
                    criteria_met = all(df[col].isin(vals).any() for col, vals in criteria.items())

                    if not criteria_met:
                        continue

                    # Ensure columns to check are present in the dataframe
                    missing_columns = [col for col in criteria.keys() if col not in df.columns]
                    if missing_columns:
                        print(f"File {filename} is missing columns: {missing_columns}")
                        continue

                    # Perform find and replace
                    for column in criteria.keys():
                        if column in df.columns:
                            changes_in_col = df[column].apply(lambda x: isinstance(x, str) and x == search_value).sum()
                           # df[column] = df[column].replace(search_value, replace_value)
                            changes += changes_in_col

                    # If any changes were made, save the modified file
                    if changes > 0:
                        df.to_csv(filepath, index=False, encoding='utf-8')
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
    root_directory = "C:\\Users\\FRE\\Documents\\Python CSV files testing\\"  # Change this to the root directory you want to search
    criteria = {
        "DistributorID": ["15582315", "15582314", 155823121],  # Columns and values to filter files
    }
    search_value = "OldValue"  # Value to search for
    replace_value = "NewValue"  # Value to replace with

    find_and_replace_in_files(root_directory, criteria, search_value, replace_value)
