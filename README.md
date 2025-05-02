# shahanabegum
Dataset Description: This dataset is from Data.gov it is about Behavioral Risk Factor Surveillance System focused on obesity rate across to the us. The dataset include YearStart,	YearEnd,	LocationAbbr,	LocationDesc,	Datasource, Class,	Topic,	Question,	Data_Value_Unit,	Data_Value_Type,	Data_Value,	Data_Value_Alt,	Data_Value_Footnote_Symbol,	Data_Value_Footnote,	Low_Confidence_Limit,	High_Confidence_Limit ,	Sample_Size,	Total,	Age(years),	Education	,Sex,	Income,	Race/Ethnicity,	GeoLocation,	ClassID,	TopicID,	QuestionID,	,	LocationID,	StratificationCategory1,	Stratification1,	StratificationCategoryId1, StratificationID1. 
Variable: After cleaning and rename the columns this columns left to work with 'Year', 'YearEnd', 'State_Abbr', 'State', 'Value_Type', 'Value',  'Data_Value_Alt', 'Low_Confidence_Limit', 'High_Confidence_Limit ', 'Sample_Size', 'Total', 'Age(years)', 'Education', 'Sex', 'Income','Race/Ethnicity', 'ClassID', 'TopicID', 'QuestionID', 'DataValueTypeID'  'LocationID', 'StratificationCategoryId1', 'StratificationID1'

Visualization: Create two plots: one bar plot and another a line plot.
A bar plot shows the average rate by the year. A line plot shows obesity trends between males and females 

Modeling Approach: I use two approaches, linear regression and logistic regression. For linear regression, I wanted to find out the predicted percentage of people who are obese and see patterns and make predictions based on the data. First, I convert categorical values into a numeric format. Then I split the data into 70 percent training and 30 percent testing. I found out the Mean squared error is  13.87 and R2 is 0.75 . Overall, the results indicate that the model predicts a strong percentage of obesity and how other factors influence obesity.

Linear regression: I wanted to find out to predict if the person 30 years or higher considered obese 1 if the person less than 30 years not considered obese 0. First, I convert categorical values into numeric format. Then I split the data into 70 percent training and 30 percent testing. I found out that Accuracy: 0.8613674891693351
Precision: 0.8704615384615385
Recall: 0.8998091603053435
F1 Score: 0.8848920863309353
   truth  prediction  count
0      1           1   2829
1      0           0   1744
2      0           1    421
3      1           0    315
Cross-validation scores: [0.86279257 0.86682809 0.86763519 0.86440678 0.85956416 0.85783522 0.87479806 0.86914378 0.84975767 0.86672052]
Average CV score: 0.8639482046206945. 86% correctly predicted if the person obese or not. 87.0% of people were obese 90% of people are actually obese. The F1 score indicates that it has balanced precision and recall. Overall, the results indicate that people are highly obese.



