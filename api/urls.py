from django.urls import path
from api.views import CategoryListAPIView, CategoryDetailsAPIView, ProductListAPIView, ProductDetailsAPIView
from api.views.views_cbv_user import AdminListAPIView, AdminDetailsAPIView, ClientListAPIView, ClientDetailsAPIView
from api.views.views_Serializer import category_list_ser, category_detail_ser, admin_list_ser, admin_detail_ser

urlpatterns = [
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_details),             # Function Based
    # path('products/', product_list),
    # path('products/<int:product_id>/', product_details),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailsAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailsAPIView.as_view()),  # Class Based

    path('clients/', ClientListAPIView.as_view()),
    path('clients/<int:client_id>/', ClientDetailsAPIView.as_view()),
    path('admins', AdminListAPIView.as_view()),
    path('admins/<int:admin_id>/', AdminDetailsAPIView.as_view()),

    # path('categories/', category_list_ser),
    # path('categories/<int:category_id>/', category_detail_ser),           # Serializer
    # path('admins/', admin_list_ser),
    # path('admins/<int:admin_id>', admin_list_ser),

]
