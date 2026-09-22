import pandas as pd
import json

# 엑셀 파일 읽기
df = pd.read_excel('FY27 Market Definition.xlsx', sheet_name='FY27 Market Definition', engine='openpyxl')

# 빈 값(NaN) 처리 및 JSON 변환
df.fillna('', inplace=True)
df.to_json('market_data.json', orient='records', force_ascii=False)
