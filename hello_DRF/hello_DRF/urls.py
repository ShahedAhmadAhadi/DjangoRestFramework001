"""hello_DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .begin import views
from car import views as carView
from student import views as studentViews
from rest_framework import renderers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'cars', carView.CarViewSet)

car_list = carView.CarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
car_detail = carView.CarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
car_highlight = carView.CarViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list =views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('car/', carView.CarList.as_view(), name='car-list'),
#     path('car/<int:pk>', carView.car_details, name='car-detail'),
#     path('person/', carView.person_list),
#     path('person/<int:pk>', carView.person_details),
#     path('student/', studentViews.student_list),
#     path('student/<int:pk>/', studentViews.student_detail),
#     path('students/', studentViews.StudentName.as_view()),
#     path('users/', carView.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', carView.UserDetail.as_view(), name='user-detail'),
#     path('', carView.api_root),
#     path('car/<int:pk>/highlight', carView.CarHighlight.as_view(), name='car-highlight'),

# ]

urlpatterns = format_suffix_patterns([
    path('', carView.api_root),
    path('cars/', car_list, name='car-list'),
    path('cars/<int:pk>/', car_detail, name='car-detail'),
    path('cars/<int:pk>/highlight/', car_highlight, name='car-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('', include(router.urls)),
])
