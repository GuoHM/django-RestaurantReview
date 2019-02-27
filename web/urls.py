from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('list',views.list),
    path('login',views.login_page),
    path('loginAction',views.login_action),
    path('logout',views.logout),
    path('/detail/<name>', views.detail, name='detail'),
]