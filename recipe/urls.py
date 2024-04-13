from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipeView


recipe_list = RecipeView.as_view({
    'post': 'create',
    'get': 'list'
})

recipe_detail = RecipeView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('recipe/', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
])
