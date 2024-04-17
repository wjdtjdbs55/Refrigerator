from django.db import models

class Ingredient(models.Model):
    ID = models.AutoField(primary_key=True)  # ID
    Scategory = models.CharField(max_length=100, null=False)  # 재료 이름
    Mcategory = models.CharField(
        max_length=10,
        choices=[
            ('채소', '채소'),
            ('과일', '과일'),
            ('고기', '고기'),
            ('유제품', '유제품')
        ],
        null=False, default='채소'
    )  # 식품 유형
    Expiration_date = models.IntegerField(null=False)  # 평균 유통 기한

    def __str__(self):
        return self.Scategory


