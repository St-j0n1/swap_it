from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemTypeChoiceView, TechnicCategoryChoiceView, TechnicSubcategoryChoiceView,
    ItemCreateView, TechnicItemCreateView, UserItemsViewSet
)

router = DefaultRouter()
router.register(r'my-items', UserItemsViewSet, basename='my-items')

urlpatterns = [
    # API endpoints for item type selection
    path('api/item-types/', ItemTypeChoiceView.as_view(), name='item-type-choice'),

    # API endpoints for technic category selection
    path('api/technic/categories/', TechnicCategoryChoiceView.as_view(), name='technic-category-choice'),
    path('api/technic/categories/<str:category>/subcategories/', TechnicSubcategoryChoiceView.as_view(),
         name='technic-subcategory-choice'),

    # API endpoints for item creation
    path('api/items/<str:item_type>/', ItemCreateView.as_view(), name='item-create'),

    # API endpoints for technic item creation
    path('api/technic/<str:category>/', TechnicItemCreateView.as_view(), name='technic-item-create'),
    path('api/technic/<str:category>/<str:subcategory>/', TechnicItemCreateView.as_view(),
         name='technic-item-create-subcategory'),

    # API endpoints for user items
    path('api/', include(router.urls)),
]
