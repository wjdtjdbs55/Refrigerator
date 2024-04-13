from django.db import models

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)  # 재료의 고유 식별자
    ingredient_name = models.CharField(max_length=100, null=False)  # 재료 이름
    avg_expiry_date = models.IntegerField(null=False )  # 평균 유통 기한
    purchase_date = models.DateField(null=True, blank=True)  # 구매 날짜
    food_type = models.CharField(max_length=50, null=False)  # 식품 유형
    fridge_location = models.CharField(max_length=50, null=True, blank=True)  # 냉장고 위치
    notes = models.TextField(null=True, blank=True)  # 추가 정보

    def __str__(self):
        return self.ingredient_name
