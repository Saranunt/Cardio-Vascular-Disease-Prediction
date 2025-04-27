# use this code for One-Hot Encoding
from sklearn.preprocessing import OneHotEncoder
import pandas as pd 

categorical_features = ["gender", "chestpain", "restingBP", "exerciseangia", "slope"]
encoder = OneHotEncoder(sparse_output=False, drop=None)
encoded_data = encoder.fit_transform(df[categorical_features])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_features))

processed_data = pd.concat([df.drop(columns=categorical_features), encoded_df], axis=1)
processed_data.head()