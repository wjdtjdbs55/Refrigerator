import os
import json
import sqlite3

# 파일 경로 설정
file_path = os.path.abspath('./recipe/recipes/recipe.json')
with open(file_path, encoding='UTF-8') as file:
    recipes = json.load(file)

# 데이터베이스 연결
conn = sqlite3.connect('/Users/jungseoyun/PycharmProjects/test/db.sqlite3')
cur = conn.cursor()

for data in recipes:
    recipe_id = data["RCP_SNO"]
    name = data["CKG_NM"]
    method = data.get("CKG_MTH")
    status = data.get("CKG_STA")
    material = data.get("CKG_MTRL")
    kind = data.get("CKG_KND")
    ingredients = ', '.join(filter(None, [data.get(f'Ingredient{i}') for i in range(1, 6)]))
    seasonings = ', '.join(filter(None, [data.get(f'Seasoning{i}') for i in range(1, 6)]))
    difficulty = data.get("CKG_DODF_NM")
    cooking_time = data.get("CKG_TIME_NM")
    calories = int(data["Calorie"]) if data.get("Calorie") else None

    # 레코드의 존재 여부 확인
    cur.execute("SELECT recipe_id FROM recipe_recipe WHERE recipe_id = ?", (recipe_id,))
    if cur.fetchone():
        # 레코드가 존재하면 업데이트
        query = """
        UPDATE recipe_recipe 
        SET name = ?, method = ?, status = ?, material = ?, kind = ?, ingredients = ?, seasonings = ?, difficulty = ?, cooking_time = ?, calories = ?
        WHERE recipe_id = ?
        """
        cur.execute(query, (name, method, status, material, kind, ingredients, seasonings, difficulty, cooking_time, calories, recipe_id))
    else:
        # 레코드가 존재하지 않으면 삽입
        query = """
        INSERT INTO recipe_recipe (recipe_id, name, method, status, material, kind, ingredients, seasonings, difficulty, cooking_time, calories)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, (recipe_id, name, method, status, material, kind, ingredients, seasonings, difficulty, cooking_time, calories))
    conn.commit()

conn.close()
