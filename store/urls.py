from django.urls import path
from .views import ProductList, ProductDetail, CreateProduct, UpdateProduct, DeleteProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('details/<int:pk>/', ProductDetail.as_view(), name='details'),
    path('createProduct/', CreateProduct.as_view(), name='createProduct'),
    path('updateProduct/<int:pk>/', UpdateProduct.as_view(), name='updateProduct'),
    path('deleteProduct/<int:pk>/', DeleteProduct.as_view(), name='deleteProduct'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
