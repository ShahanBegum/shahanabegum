import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler

def main():
    # Load cleaned obesity dataset
    data = pd.read_csv("data/clean-Obesity_data.csv")

    # Print column names to check if this working 
    print(data.columns)
    # features
    features = ['Year', 'YearEnd', 'State_Abbr', 'State', 'Value_Type',
                'Sample_Size', 'Age(years)', 'Education', 'Sex', 'Income',
                'Race/Ethnicity', 'ClassID', 'TopicID', 'QuestionID',
                'DataValueTypeID', 'LocationID', 'StratificationCategoryId1',
                'StratificationID1']

    # I choose obese to predict if the person 30 or higher considered obese  
    # 1 if person less then 30 not considered obese 0
    data['Obese'] = (data['Value'] >= 30).astype(int)  
    # Convert  catogorical values into numeric format
    X = pd.get_dummies(data[features], drop_first=True)
    # choose target value obese to predict
    y = data['Obese']

    # Step 1 - Split the data into traning and testing 30% data  will be use  for the  testing 
    # 70% will be use for training
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.3,
                                                        random_state=123)

    # Scale the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # logistic regression model make 1000 iterations 
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)

    # Make Predict on test data
    y_pred = model.predict(X_test_scaled)

    # Evaluate performance
    # correct predictions / total predictions
    #True Positives) / (True Positives + False Positives)
    #(True Positives) / (True Positives + False Negatives)
    #2 * (Precision * Recall) / (Precision + Recall)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))

    # Confusion matrix show how many times combination of actual and predicated occured 
    conf_matrix = pd.DataFrame({"truth": y_test, "prediction": y_pred})
    print(conf_matrix.value_counts().reset_index())

    # Cross-validation scores 10 fold cross validation trains on 9 test on 1 
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=10)
    print("Cross-validation scores:", cv_scores)
    print("Average CV score:", np.mean(cv_scores))


main()