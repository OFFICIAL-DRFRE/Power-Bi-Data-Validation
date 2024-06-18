import os
import pandas as pd


def extract_and_replace_rows(root_dir, column, search_value, replace_value):
    modified_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:
                    # Attempt to read the file with 'latin1' encoding
                    df = pd.read_csv(filepath, encoding='latin1', low_memory=False)

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

                        # Replace the search value with the replace value
                        df[column] = df[column].replace(search_value, replace_value)

                        # Save the modified file
                        df.to_csv(filepath, index=False, encoding='latin1')
                        modified_files.append(filepath)

                except Exception as e:
                    print(f"Error processing file {filename}: {e}")

    if modified_files:
        print("\nModified files:")
        for file in modified_files:
            print(file)
    else:
        print("No files were modified.")

if __name__ == "__main__":
    # root_directory = "C:\\Users\\Administrator\\Documents\\PBI Data Test"  # Change this to the root directory you want to search
    root_directory = "C:\\Users\\Administrator\\Unilever\\Ethiopia Business Dashboard - Documents\\General\\Ethiopia Dashboard\\Monthly data dumps\\Secondary\\2023\\"

    column_to_search = "OutletID"
    search_value = "ID- T000100701400001969"  # Value to search for
    replace_value = "ID - T000100701400001969"  # Value to replace with

    # search_value = 15582315  # Value to search for
    # replace_value = 15469643  # Value to replace with

    extract_and_replace_rows(root_directory, column_to_search, search_value, replace_value)
