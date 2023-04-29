import pandas as pd 
import numpy as np
# import csv
# from scipy import stats
# from scipy.stats import boxcox

filename = "data.csv"
df = pd.read_csv(filename)

# check for missing values
if df.isnull().values.any():
    print("There are missing values in the DataFrame.")

    # replace missing values with mean or median
    for col in df.columns:
        if df[col].isnull().values.any():
            if df[col].dtype != 'object':
                median = df[col].median()
                df[col].fillna(median, inplace=True)
            else:
                mode = df[col].mode().iloc[0]
                df[col].fillna(mode, inplace=True)

# check for inconsistencies
for col in df.columns:
    if df[col].dtype == 'object':
        unique_vals = df[col].unique()
        if len(unique_vals) > 2:
            print(f"Inconsistent values found in {col}: {unique_vals}")
            # replace inconsistent values with mode
            mode = df[col].mode().iloc[0]
            df[col].replace(unique_vals, mode, inplace=True)

# # detect and deal with outliers in numeric variables
# for col in df.select_dtypes(include=[np.number]).columns:
#     q1 = df[col].quantile(0.25)
#     q3 = df[col].quantile(0.75)
#     iqr = q3 - q1
#     lower_bound = q1 - 1.5 * iqr
#     upper_bound = q3 + 1.5 * iqr
#     outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
#     if not outliers.empty:
#         print(f"Outliers found in {col}: {outliers.values}")
#         # replace outliers with the median
#         median = df[col].median()
#         df.loc[(df[col] < lower_bound) | (df[col] > upper_bound), col] = median

# # apply Box-Cox transformation on income variable to reduce skewness
# transformed_income, lambda_value = boxcox(df['income'])
# df['income_transformed'] = transformed_income


# print the cleaned DataFrame
print(df)