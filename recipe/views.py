from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework import permissions


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permisson_classes = (permissions.IsAuthenticated, )

    def recipe_create(self, serializer):
        serializer.save(user=self.request.user)