from django.urls import path
from api.views import CategoryListAPIView, CategoryDetailsAPIView, ProductListAPIView, ProductDetailsAPIView
from api.views.views_cbv_user import AdminListAPIView, AdminDetailsAPIView, ClientListAPIView, ClientDetailsAPIView
from api.views.views_Serializer import category_list_ser, category_detail_ser, admin_list_ser, admin_detail_ser
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import include, path
from rest_framework import routers

from api.views import views_cbv
router = routers.DefaultRouter()
router.register(r'users', views_cbv.UserViewSet)
urlpatterns = [
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_details),             # Function Based
    # path('products/', product_list),
    # path('products/<int:product_id>/', product_details),
    path('login/', obtain_jwt_token),
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

    path('products/<int:product_id>/', ProductDetailsAPIView.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]





