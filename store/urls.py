from django.urls import path
from .views import ProductList
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('details/<int:pk>/', ProductDetail.as_view(), name='details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
