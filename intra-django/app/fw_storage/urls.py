from django.urls import path, include
from . import views
from . import api_views

# REST
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'nordics', api_views.NordicViewSet)


urlpatterns = [
    path('<int:pk>/', views.detail_page),
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
