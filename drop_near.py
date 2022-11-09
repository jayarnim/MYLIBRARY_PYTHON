# 메인함수 :
    # drop_near(df, target = False, i = 10, print = False)
    # df : 함수를 적용할 데이터프레임
    # target : 종속변수 칼럼명 (df에 종속변수가 존재하지 않을 경우 생략함)
    # i : 분산팽창계수가 얼마를 초과한 칼럼을 삭제할 것인가 (기본값은 10임)
    # print : 잔존한 독립변수의 분산팽창계수에 관한 정보를 담은 데이터프레임을 출력할 것인가 (기본값은 출력하지 않음임)

# 기능 :
    # 데이터프레임 df의 독립변수 중 다중공선성이 높은 변수를 삭제함
    # 다중공선성은 분산팽창계수 VIF로 계산하였음

# 반환값 :
    # 다중공선성이 높은 독립변수가 삭제된 df



import numpy as np
import pandas as pd

def drop_near(df, target = False, i = 10, print = False) :
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    if target != False :
        target_series = df[target]
        df = df.drop([target], axis = 1)

    while True :
        vif = pd.DataFrame()
        vif['feature'] = df.columns
        vif['VIF'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        vif_max = vif['VIF'].max()
        vif_max_col = vif[vif['VIF'] == vif_max].loc[:, 'feature']
        
        if vif_max > i :
            df = df.drop(vif_max_col, axis = 1)        
        else :
            if print == True :
                print(vif)
                break
            elif print == False :
                break

    if target != False :
        df[target] = target_series

    return df
