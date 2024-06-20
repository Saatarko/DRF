"""
URL configuration for DRF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import ExchangeViewSet

# from main.views import ExchangeAPIList, ExchangeAPIUpdate, ExchangeAPIDetailView
router = routers.SimpleRouter()  # если используем DefaultRouter то он содержит в себе и те
# маршруты что мы регистрируем (с учетом url) т.е в нашем случае http://127.0.0.1:8000/api/v1/
router.register(r'exchange',ExchangeViewSet)
# есть паарметр basename - исползуется для изменения названий маршрутов
# (по умолчанию используется название таблицы-основателя. И обяязательно нужно указывать
# во вьюхе нет указания на таблицу


urlpatterns = [
    path('admin/', admin.site.urls),

    # если используем роутеры инклюдим их что ранвосильно  http://127.0.0.1:8000/api/v1/exchange
    # где exchange - префикс роутера
    path('api/v1/', include(router.urls)),


    # path('api/v1/exchangelist/', ExchangeViewSet.as_view({'get':'list'})),
    # # плохой вариант для работы в вьюсетами (ибо етсь роутеры)
    # path('api/v1/exchangelist/<int:pk>/', ExchangeViewSet.as_view({'put':'update'})),

       # тут {'get':'list'} и {'put':'update'} - методы которые будут вызываться и какой
    # внутренней функцией они будут обрабатываться


    # тут api/v1/exchangelist/   api -простообнзначение api, v1 -версия, exchangelist -slug
    # path('api/v1/exchangelist/<int:pk>/', ExchangeAPIUpdate.as_view()),
    # path('api/v1/exchangelist/', ExchangeAPIList.as_view()),
    # path('api/v1/exchangedetail/<int:pk>/', ExchangeAPIDetailView.as_view())
]
