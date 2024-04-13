from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cooking_time = models.IntegerField(blank=True, null=True)
    spiciness_level = models.CharField(
        max_length=10,
        choices=[
            ('1단계', '1단계'),
            ('2단계', '2단계'),
            ('3단계', '3단계'),
            ('4단계', '4단계'),
            ('5단계', '5단계')
        ],
        blank=True, null=True
    )
    calories = models.IntegerField(blank=True, null=True)
    cuisine_type = models.CharField(
        max_length=20,
        choices=[
            ('한식', '한식'),
            ('양식', '양식'),
            ('중식', '중식'),
            ('일식', '일식'),
            ('퓨전', '퓨전'),
            ('기타', '기타')
        ],
        blank=True, null=True
    )