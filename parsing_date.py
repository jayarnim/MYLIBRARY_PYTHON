# 메인함수 :
    # parsing_date(df, date_col, drop = True, year = True, month = True, day = True, hour = True, weekday = True, season = True, holiday = True)
        # df : 함수를 적용할 데이터프레임
        # date_col : 파싱할 칼럼명
        # drop : date_col 삭제 여부 (기본값은 삭제임)
        # year : 연도 칼럼 생성 여부 (기본값은 생성임)
        # month : 월 칼럼 생성 여부 (기본값은 생성임)
        # day : 일 칼럼 생성 여부 (기본값은 생성임)
        # hour : 시 칼럼 생성 여부 (기본값은 생성임)
        # weekday : 요일 칼럼 생성 여부 (기본값은 생성임)
        # season : 계절 칼럼 생성 여부 (기본값은 생성임)
        # holiday : 휴일 칼럼 생성 여부 (기본값은 생성임)
    
# 기능 :
    # 데이터프레임 df에서 날짜 정보가 저장되어 있는 칼럼 date_col을 년/월/일/시/요일/계절/휴일여부로 파싱함

# 반환값 :
    # 년/월/일/시/요일/계절/휴일 컬럼이 추가된 df
        # 년 : YEAR
        # 월 : MONTH
        # 일 : DAY
        # 시 : HOUR
        # 요일 : WEEKDAY; 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
        # 계절 : SEASON; 봄(0), 여름(1), 가을(2), 겨울(3)
        # 휴일 : HOLIDAY; 휴일(1), 휴일아님(0)

# 주의 :
    # 휴일 여부에 관한 정보를 담은 칼럼을 생성 시 다음을 가정함
        # 라이브러리 holidays가 import되었음
        # 해당 라이브러리의 함수 인스턴스를 holidays라고 정의했음
        # 아래는 한국의 휴일을 계산하는 함수 holidays.KR()를 예시로 들었음

    
    
import numpy as np
import pansdas as pd
import holidays
holidays = holidays.KR()

def weekday_label(x) :
    if x == 'Monday' : return 0
    elif x == 'Tuesday' : return 1
    elif x == 'Wednesday' : return 2
    elif x == 'Thursday' : return 3
    elif x == 'Friday' : return 4
    elif x == 'Saturday' : return 5
    elif x == 'Sunday' : return 6

def season_label(x) :
    if x in [3, 4, 5] : return 0
    elif x in [6, 7, 8] : return 1
    elif x in [9, 10, 11] : return 2
    elif x in [12, 1, 2] : return 3

def parsing_date(df, date_col, drop = True, year = True, month = True, day = True, hour = True, weekday = True, season = True, holiday = True) :
    df[date_col] = df[date_col].apply(pd.to_datetime)
    
    if year == True : df['YEAR'] = df[date_col].apply(lambda x : x.year)
    df['MONTH'] = df[date_col].apply(lambda x : x.month)
    if season == True : df['SEASON'] = df['MONTH'].apply(season_label)    
    if month != True : df.drop(['MONTH'], axis = 1)
    if day == True : df['DAY'] = df[date_col].apply(lambda x : x.day)    
    if hour == True : df['HOUR'] = df[date_col].apply(lambda x : x.hour)    
    if weekday == True : df['WEEKDAY'] = df[date_col].apply(lambda x : x.day_name()).apply(weekday_label)
    if holiday == True : df['HOLIDAY'] = df[date_col].apply(lambda x : 1 if x in holidays else 0)
    
    if drop == True : df = df.drop([date_col], axis = 1)

    return df
