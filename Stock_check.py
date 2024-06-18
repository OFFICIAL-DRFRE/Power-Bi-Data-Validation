import os
import pandas as pd
import numpy as np


def find_non_int64_values(root_dir, columns):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.csv'):
                filepath = os.path.join(dirpath, filename)
                try:
                    # specify the correct encoding if known
                    df = pd.read_csv(filepath, encoding='latin1', low_memory=False)

                    # Ensure columns to check are present in the dataframe
                    missing_columns = [col for col in columns if col not in df.columns]
                    if missing_columns:
                        print(f"File {filename} is missing: {missing_columns}")
                        continue

                    for column in columns:
                        # Check for non-Int64 values in the specified column
                        def is_int64(value):
                            try:
                                if pd.isna(value):
                                    return False
                                int_value = np.int64(value)
                                return True
                            except (ValueError, OverflowError, TypeError):
                                return False

                        non_int64_rows = df[~df[column].apply(is_int64)]

                        if not non_int64_rows.empty:
                            print(f"File: {filename} - Non-Int64 values in column '{column}':")
                            print(non_int64_rows[[column]])
                            print("\n")  # Add a newline for better readability

                except Exception as e:
                    print(f"Error processing file {filename}: {e}")


if __name__ == "__main__":
    root_directory = "C:\\Users\\FRE\\Unilever\\Ethiopia Business Dashboard - Documents\\" \
                     "General\\Ethiopia Dashboard\\Monthly data dumps\\Secondary\\2022"
    columns_to_check = ["Material", "DistributorID"]
    find_non_int64_values(root_directory, columns_to_check)
