# date 칼럼 파싱하기
# 비파괴적 함수
# 기능 : date 칼럼을 년/월/일/시/요일/계절로 파싱함

# 메인함수 : parsing_date(df, date_col, drop = True)
# 반환값 : 년/월/일/시/요일/계절 컬럼이 추가된 df

# df : 함수를 적용할 데이터프레임
# date_col : 파싱할 칼럼명
# drop : date_col 삭제 여부 (기본값은 삭제임)



import numpy as np
import pansdas as pd
import holidays
holidays = holidays.KR()

def weekday(x) :
    if x == 'Monday' : return '0_Monday'
    elif x == 'Tuesday' : return '1_Tuesday'
    elif x == 'Wednesday' : return '2_Wednesday'
    elif x == 'Thursday' : return '3_Thursday'
    elif x == 'Friday' : return '4_Friday'
    elif x == 'Saturday' : return '5_Saturday'
    elif x == 'Sunday' : return '6_Sunday'

def season(x) :
    if x in range(3,6) : return '0_spring'
    elif x in range(6,9) : return '1_summer'
    elif x in range(9,12) : return '2_autumn'
    else : return '3_winter'

def parsing_date(df, date_col, drop = True) :
    df[date_col] = df[date_col].apply(pd.to_datetime)
    df['YEAR'] = df[date_col].apply(lambda x : x.year)
    df['MONTH'] = df[date_col].apply(lambda x : x.month)
    df['DAY'] = df[date_col].apply(lambda x : x.day)
    df['HOUR'] = df[date_col].apply(lambda x : x.hour)
    df['WEEKDAY'] = df[date_col].apply(lambda x : x.day_name())
    df['WEEKDAY'] = df['WEEKDAY'].apply(weekday)
    df['SEASON'] = df['MONTH'].apply(season)
    df['HOLIDAY'] = df[date_col].apply(lambda x : 1 if x in holidays else 0)
    
    if drop == True :
        df = df.drop([date_col], axis = 1)

    return df
