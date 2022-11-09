import numpy as np
import pandas as pd

def pre_col(df, label_col = False, onehot_col = False) :
    from sklearn.preprocessing import LabelEncoder
    
    if label_col != False :
    for col in label_col :
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[[col]])
 
    if onehot_col != False :
        df = pd.get_dummies(df, columns = onehot_col)
   
    return df
