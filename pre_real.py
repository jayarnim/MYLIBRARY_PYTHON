# 실질변수 전처리하기
# 비파괴적 함수
# 기능 :
    # 1/ 실질변수의 이상치를 상한값 및 하한값으로 치환함; Tukey Fences 기법 적용
    # 2/ 실질변수를 표준화(Stanard) 및 정규화(MinMax)함

# 메인함수 : pre_real(df, col_list)
# 반환값 : 실질변수가 전처리된 df

# 매개변수
    # df : 함수를 적용할 데이터프레임
    # col : 전처리할 칼럼명이 기입된 리스트



import numpy as np
import pandas as pd

def pre_real(df, col_list) :
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    
    for col in col_list :
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_value = Q1 - IQR * 1.5
        upper_value = Q3 + IQR * 1.5
        df[col] = df[col].clip(lower = lower_value, upper = upper_value)
        
        scaler = StandardScaler()
        scaler.fit_transform(df[[col]])
        scaled = scaler.transform(df[[col]])
        df[col] = scaled
        
        scaler = MinMaxScaler()
        scaler.fit_transform(df[[col]])
        df[col] = scaled

    return df
