# 메인함수 :
    # pre_real(df, real_col)
    # df : 함수를 적용할 데이터프레임
    # real_col : 전처리할 실질변수 칼럼명이 기입된 리스트

# 기능 :
    # 데이터프레임 df의 실질변수 이상치를 상한값 및 하한값으로 치환함; Tukey Fences 기법 적용
    # 데이터프레임 df의 실질변수를 표준화함; StanardScaler 적용
    # 데이터프레임 df의 실질변수를 정규화함; MinMaxScaler 적용

# 반환값 :
    # 실질변수가 전처리된 df
    
    

import numpy as np
import pandas as pd

def pre_real(df, real_col) :
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
   
    for col in real_col :
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_value = Q1 - IQR * 1.5
        upper_value = Q3 + IQR * 1.5
        df[col] = df[col].clip(lower = lower_value, upper = upper_value)
        
        scaler = StandardScaler()
        df[col] = scaler.fit_transform(df[[col]])
        
        scaler = MinMaxScaler()
        df[col] = scaler.fit_transform(df[[col]])

    return df
