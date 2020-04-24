from django.urls import path
from api.views import CategoryListAPIView, CategoryDetailsAPIView, ProductListAPIView, ProductDetailsAPIView

urlpatterns = [
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_details),  Function Based
    # path('products/', product_list),
    # path('products/<int:product_id>/', product_details),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailsAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailsAPIView.as_view()),
]
