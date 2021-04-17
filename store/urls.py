from django.urls import path
from .views import ProductList, ProductDetail, CreateProduct, UpdateProduct, DeleteProduct, LoginView, RegisterPage, index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', index, name='homepage'),
    path('details/<int:pk>/', ProductDetail.as_view(), name='details'),
    path('createProduct/', CreateProduct.as_view(), name='createProduct'),
    path('updateProduct/<int:pk>/', UpdateProduct.as_view(), name='updateProduct'),
    path('deleteProduct/<int:pk>/', DeleteProduct.as_view(), name='deleteProduct'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
