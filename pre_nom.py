# 메인함수 :
    # pre_nom(df, label_col = False, onehot_col = False)
    # df : 함수를 적용할 데이터프레임
    # label_col : Label Encoding할 명목변수 칼럼명이 기입된 리스트 (Label Encoding할 칼럼이 없으면 생략함)
    # onehot_col : One-Hot Encoding할 명목변수 칼럼명이 기입된 리스트 (One-Hot Encoding할 칼럼이 없으면 생략함)

# 기능 :
    # 데이터프레임 df의 명목변수를 Label Encoding함
    # 데이터프레임 df의 명목변수를 One-Hot Encoding함

# 반환값 :
    # 명목변수가 전처리된 df


    
import numpy as np
import pandas as pd

def pre_nom(df, label_col = False, onehot_col = False) :
    from sklearn.preprocessing import LabelEncoder
    
    if label_col != False :
        for col in label_col :
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[[col]])
 
    if onehot_col != False :
        df = pd.get_dummies(df, columns = onehot_col)
   
    return df
