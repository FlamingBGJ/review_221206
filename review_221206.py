# 221206 복습 
## Time Series
import pandas as pd
import numpy as np

np.random.seed(252) # 동일한 결과를 내기 위해서는 동일한 시드를 고정시켜서 적용해야한다.

# "timeseries" 데이터는 `DatetimeIndex` 또는 `PeriodIndex`로 구성된 데이터 셋

data_1 = pd.to_datetime("20221206")
print(data_1)
type(data_1)

data_2 = pd.to_datetime("2022-12-06")
data_2

# smaple 데이터 생성
def random_series(dts):
    res = pd.Series(np.random.randn(len(dts)), index=dts)
    return res

# `Timestamp` 를 이용해 시간 객체 생성
ts = pd.Timestamp("2022-01-01 00:00")
s_1 = pd.Series(100, index = [ts])
random_series(s_1)

# 1년동안 평일 생성
dts = pd.date_range("2023-01-01", "2023-12-31", freq="B")

# 시계열 데이터에서의 indexing 과 slicing
df_dts = random_series(dts)
df_dts.head() # indexing
df_dts.head() # slicing
df_dts.loc["2023-01-02"] 

df_dts["2023-01":"2023-02"] # 달별 선택
df_dts["2023"] # 연별 선택

# 시계열 데이터의 이동 : shift 사용
df_dts_log = df_dts["2023-01"].copy()
df_dts_log.shift(1) # 아래로 1칸 - 후행
df_dts_log.shift(-2) # 위로 2칸 - 선행

## 간격 재조정 : resample을 통해
dts_1 = pd.date_range("2022-01-01", "2022-03-31", freq="D") # 해당 범위에서 일별 데이터
ts_1 = random_series(dts_1)
ts_1.resample("M") # 월별데이터로 리셈플링

ts_1.resample("M").mean() # groupby처럼도 쓸 수 있다.
ts_1.resample("M").agg(["mean","std"])

# dt 접근자의 사용
dts_1.strftime("%y년 %m월 %d일") # 각 시계열 변수는 고정 ex) y는 년, m은 달, d는 일