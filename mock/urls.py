from django.urls import path, re_path

from . import views
"""
set unfinished path's default as index
"""
app_name = 'mock'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'logout', views.index, name='logout'),
    path(r'test', views.test, name='test'),
    path('forget', views.test, name='forgetPassword'),
    path('search', views.index, name='search'),
    path('not_found', views.not_found, name='not_found'),
    path('latest_reviews', views.latest_reviews, name='latest_reviews'),
    path('follow_reviews', views.follow_reviews, name='follow_reviews'),
    path('course', views.index, name='course_index'),
    path('course/popular', views.popular, name='course_popular'),
    path('course/view_course', views.index, name='view_course'),
    path('course/public', views.index, name='course_public'),
    path('user/view_profile', views.index, name='user_view_profile'),
    path('user/notice', views.index, name='user_notice'),
    path('user/account_settings', views.index, name='user_account_settings'),
]
