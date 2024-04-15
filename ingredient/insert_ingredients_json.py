import os
import json
import sqlite3

# 파일 경로 설정
file = os.path.abspath('./ingredient/ingredients/ingredient.json')
with open(file, encoding='UTF-8') as file:
    json_obj = json.load(file)

# 데이터베이스 연결
conn = sqlite3.connect('/Users/jungseoyun/PycharmProjects/test/db.sqlite3')
cur = conn.cursor()

for data in json_obj:
    ID = data.get("ID")
    Scategory = data.get("Scategory")
    Mcategory = data.get("Mcategory")
    Expiration_date = data.get("Expiration_date")
    Date_of_registration = data.get("Date_of_registration") or None  # JSON에서 비어있으면 None으로 처리

    # 레코드의 존재 여부 확인
    cur.execute("SELECT ID FROM ingredient_ingredient WHERE ID = ?", (ID,))
    if cur.fetchone():
        # 레코드가 존재하면 업데이트
        query = """
        UPDATE ingredient_ingredient 
        SET Scategory = ?, Mcategory = ?, Expiration_date = ?, Date_of_registration = ?
        WHERE ID = ?
        """
        cur.execute(query, (Scategory, Mcategory, Expiration_date, Date_of_registration, ID))
    else:
        # 레코드가 존재하지 않으면 삽입
        query = "INSERT INTO ingredient_ingredient (ID, Scategory, Mcategory, Expiration_date, Date_of_registration) VALUES (?,?,?,?,?)"
        cur.execute(query, (ID, Scategory, Mcategory, Expiration_date, Date_of_registration))
    conn.commit()

conn.close()
