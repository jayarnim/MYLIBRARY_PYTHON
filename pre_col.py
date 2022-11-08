# 실질변수 전처리하기
# 비파괴적 함수
# 기능 :
    # 1/ 실질변수의 이상치를 상한값 및 하한값으로 치환함; Tukey Fences 기법 적용
    # 2/ 실질변수를 표준화(Stanard) 및 정규화(MinMax)함
    # 3/ 명목변수를 Label Encoding함
    # 4/ 명목변수를 One-Hot Encoding함

# 메인함수 : pre_real(df, real_col = False, label_col = False, onehot_col = False)
# 반환값 : 실질변수가 전처리된 df

# 매개변수
    # df : 함수를 적용할 데이터프레임
    # real_col : 전처리할 실질변수 칼럼명이 기입된 리스트 (전처리할 칼럼이 없으면 생략함)
    # label_col : Label Encoding할 명목변수 칼럼명이 기입된 리스트 (Label Encoding할 칼럼이 없으면 생략함)
    # onehot_col : One-Hot Encoding할 명목변수 칼럼명이 기입된 리스트 (One-Hot Encoding할 칼럼이 없으면 생략함)

    
    
import numpy as np
import pandas as pd

def pre_col(df, real_col = False, label_col = False, onehot_col = False) :
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder
    
    if real_col != False :
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

    if label_col != False :
        for col in label_col :
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[[col]])
            label_dict[col] = list(encoder.classes_)
 
    if onehot_col != False :
        df = pd.get_dummies(df, columns = onehot_col)
   
    return df
