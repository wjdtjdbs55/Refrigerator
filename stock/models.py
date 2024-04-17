from django.db import models

class Stock(models.Model):
    Name = models.CharField(max_length=100)
    Amount = models.IntegerField()
    Date_of_registration = models.DateField(null=True, blank=True)  # 구매 날짜

    def __str__(self):
        return f"{self.name} ({self.count})"


