import great_expectations as ge
import pandas as pd

# Example: Validate a CSV file against a set of expectations
def run_validation():
    # Load sample data into a Pandas DataFrame
    df = pd.read_csv('/data/sample_data.csv')
    
    # Convert to a Great Expectations DataFrame
    ge_df = ge.from_pandas(df)
    
    # Define a simple expectation: no null values in a specific column (e.g., 'id')
    result = ge_df.expect_column_values_to_not_be_null('id')
    
    # Print the validation results
    print(result)

if __name__ == "__main__":
    run_validation()
