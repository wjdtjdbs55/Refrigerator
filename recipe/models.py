from django.db import models

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=20, primary_key=True, default='1')  # RCP_SNO를 기본 키로 사용
    name = models.CharField(max_length=100)  # 요리 이름 (CKG_NM)
    method = models.CharField(max_length=50, blank=True, null=True)  # 조리 방법 (CKG_MTH)
    status = models.CharField(max_length=50, blank=True, null=True)  # 요리 상태 (CKG_STA)
    material = models.CharField(max_length=50, blank=True, null=True)  # 주재료 분류 (CKG_MTRL)
    kind = models.CharField(max_length=50, blank=True, null=True)  # 요리 종류 (CKG_KND)
    ingredients = models.TextField(blank=True, null=True)  # 재료들을 하나의 필드에 문자열로 저장
    seasonings = models.TextField(blank=True, null=True)  # 양념들을 하나의 필드에 문자열로 저장
    difficulty = models.CharField(max_length=50, blank=True, null=True)  # 요리 난이도 (CKG_DODF_NM)
    cooking_time = models.CharField(max_length=50, blank=True, null=True)  # 조리 시간 (CKG_TIME_NM)
    calories = models.IntegerField(blank=True, null=True)  # 칼로리 (Calorie)

    def __str__(self):
        return self.name
