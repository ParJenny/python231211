import openpyxl
from openpyxl import Workbook
import random

# 엑셀 파일 생성
workbook = Workbook()
sheet = workbook.active

# 엑셀 헤더 추가
sheet.append(["제품ID", "제품명", "수량", "가격"])

# 제품 데이터 생성 및 추가
for _ in range(100):
    product_id = random.randint(1000, 9999)
    product_name = f"제품_{product_id}"
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 1000), 2)

    sheet.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
file_path = r"C:\work\products.xlsx"
workbook.save(file_path)

print(f"데이터가 {file_path}에 저장되었습니다.")
