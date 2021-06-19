# Customer Churn Prediction

As a business analyst I am interested in developing analytics skills that reveal important KPIs and strategies for retaining customers. Understanding what drives customer churn is a good way to find these important business metrics and insights. That is why for this project I decided to analyze why customers at a Telecom company were churning. In this project I build a logistic regression model and use it as a lens to understand what drives customers to cancel their subscription. The data set is from a Kaggle competition called "Customer Churn Prediction 2020" (https://www.kaggle.com/c/customer-churn-prediction-2020/overview)

### Data

-The dataset has 4250 observations. Each observaton contains 19 features and 1 boolean variable "churn" which indicates whether or not that particular user churned.

-Below are the features I decided to include in my final model.


"total_day_charge", numerical. Total charge of day calls.

"total_eve_charge", numerical. Total charge of evening calls.

"total_night_charge", numerical. Total charge of night calls.

"total_intl_charge", numerical. Total charge of international calls

"number_customer_service_calls", numerical. Number of calls to customer service

"churn", 𝑦𝑒𝑠/𝑛𝑜. Customer churn - target variable.

