from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name='index'),
    path('list',views.list,name='list'),
    path('login',views.login_page, name='login'),
    path('loginAction',views.login_action, name='loginAction'),
    path('logout',views.logout, name='logout'),
    path('restaurant/<name>', views.restaurant, name='restaurant'),
    path('review/<name>', views.review_page, name='review'),
    path('detail/<int:review_id>',views.reveiw_detail, name='detail'),
    path('like/<int:comment_id>',views.like, name='like'),
    path('comment/<int:review_id>',views.comment, name='comment'),
    path('subcomment/<int:comment_id>',views.subcomment, name='subcomment'),
    path('submitReview/<int:restaurant_id>',views.submit_review, name='submitReview')
]