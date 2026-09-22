import pandas as pd
import json

# 1. header=1 옵션으로 2행을 헤더로 인식하고, dtype=str으로 모든 데이터를 문자열로 가져옵니다.
df = pd.read_excel('FY27 Market Definition.xlsx', sheet_name='FY27 Market Definition', engine='openpyxl', dtype=str, header=1)

# 2. 엑셀 헤더에 숨어있는 줄바꿈과 공백을 정리합니다.
df.columns = [str(col).replace('\n', ' ').replace('\r', '').strip() for col in df.columns]

# 3. 빈 셀(NaN)을 공백('')으로 처리합니다.
df.fillna('', inplace=True)

# 4. JSON 파일로 저장합니다.
df.to_json('market_data.json', orient='records', force_ascii=False)
