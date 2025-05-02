import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Load cleaned obesity dataset
    data = pd.read_csv("data/clean-Obesity_data.csv")

    #  features
    features =['Year', 'YearEnd', 'State_Abbr', 'State', 'Value_Type',
                'Sample_Size', 'Age(years)', 'Education', 'Sex', 'Income',
                'Race/Ethnicity', 'ClassID', 'TopicID', 'QuestionID',
                'DataValueTypeID', 'LocationID', 'StratificationCategoryId1',
                'StratificationID1']

    #  target
    target ="Value"

    # Convert  catogorical values into numeric format
    X = pd.get_dummies(data[features], drop_first=True)
    # define the which is value
    y = data[target]

    # Step 1 - Split the data into traning and testing 30% data  will be use  for the  testing 
    # 70% will be use for training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Fit model - linear regression training the data
    model = LinearRegression()
    model.fit(X_train, y_train)

    #  Make Predict on test data
    y_pred = model.predict(X_test)

    # Measure how good my predication were 
    #average of the squared differences between predicted and actual values
    #the proportion of variance in the dependent variable explained by the model – 
    # ranges from 0 to 1, where 1 indicates a perfect fit.
    print(mean_squared_error(y_test, y_pred))
    print(r2_score(y_test, y_pred))
main()