import pandas as pd

def main():
    # Load the dataset
    data = pd.read_csv("data/Obesity_data.csv")
    print(data.columns)

    
    # Drop unnecessary columns because I don't need those
    columns_to_drop = [
        'Datasource', 'Class', 'Topic', 'Question', 'Data_Value_Unit',
        'Data_Value_Footnote_Symbol', 'Data_Value_Footnote',
        'StratificationCategory1', 'Stratification1',
        'GeoLocation'
    ]
    data = data.drop(columns=columns_to_drop, errors='ignore')

    
    # Rename columns which will make easier for me 
    data = data.rename(columns={
        'YearStart': 'Year',
        'LocationAbbr': 'State_Abbr',
        'LocationDesc': 'State',
        'Data_Value_Type': 'Value_Type',
        'Data_Value': 'Value'
    })
    # Drop the missing value from the value column because I am gonna use this for the target 
    data = data.dropna(subset=["Value"])

    # Save the cleaned data
    data.to_csv("data/clean-Obesity_data.csv", index=False)
    
    

main()