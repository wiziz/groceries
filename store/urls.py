from django.urls import path
from .views import ProductList, ProductDetail, createProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('details/<int:pk>/', ProductDetail.as_view(), name='details'),
    path('createProduct/', createProduct.as_view(), name='createProduct'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
