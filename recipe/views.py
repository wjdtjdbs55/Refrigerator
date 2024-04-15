from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import Recipe



class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


    def recipe_create(self, serializer):
        serializer.save(user=self.request.user)