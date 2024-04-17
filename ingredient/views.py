from rest_framework import viewsets
from .serializers import IngredientSerializer
from .models import Ingredient


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


    def ingredient_create(self, serializer):
        serializer.save(user=self.request.user)


