# 메인함수 :
    # parsing_date(df, date_col, drop = True)
    # df : 함수를 적용할 데이터프레임
    # date_col : 파싱할 칼럼명
    # drop : date_col 삭제 여부 (기본값은 삭제임)
    
# 기능 :
    # 데이터프레임 df에서 날짜 정보가 저장되어 있는 칼럼 date_col을 년/월/일/시/요일/계절/휴일여부로 파싱함

# 반환값 :
    # 년/월/일/시/요일/계절 컬럼이 추가된 df
    # 연도 : YEAR
    # 월 : MONTH
    # 일 : DAY
    # 시 : HOUR
    # 요일 : WEEKDAY; 월(0_Monday), 화(1_Tuesday), 수(2_Wedensday), 목(3_Thursday), 금(4_Friday), 토(5_Saturday), 일(6_Sunday)
    # 계절 : SEASON; 봄(0_Spring), 여름(1_Summer), 가을(2_Autumn), 겨울(3_Winter)
    # 휴일 : HOLIDAY; 휴일(1), 휴일아님(0)

# 주의 :
    # 라이브러리 holidays가 import되었음을 가정함
    # 해당 라이브러리의 함수 인스턴스를 holidays라고 정의했음을 가정함
    # 아래는 한국의 휴일을 계산하는 함수 holidays.KR()를 예시로 들었음

    
    
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
    if x in range(3,6) : return '0_Spring'
    elif x in range(6,9) : return '1_Summer'
    elif x in range(9,12) : return '2_Autumn'
    else : return '3_Winter'

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
