from django.urls import path, include
from . import views
from . import api_views

# REST
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'nordics', api_views.NordicViewSet)


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:pk>/', views.blog_post),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
