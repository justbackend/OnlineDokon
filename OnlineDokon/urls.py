from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahsulot_qidiruv', MahsulotQidiruvApi.as_view()),
    path('mahsulot/<str:pk>/', MahsulotGetApi.as_view()),
    path('mahsulot/<int:pk>/media', MahsulotGetApi.as_view()),
    path('mahsulot/<int:pk>/mahsulot', MahsulotGetApi.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
