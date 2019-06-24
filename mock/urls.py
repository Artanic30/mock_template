from django.urls import path

from . import views, api
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
    path('about/', views.about, name='about'),
    path('community-rules/', views.community_rules, name='about'),
    path('latest_reviews', views.latest_reviews, name='latest_reviews'),
    path('follow_reviews', views.follow_reviews, name='follow_reviews'),
    path('catalog', views.catalog, name='catalog'),
    path('course', views.index, name='course_index'),
    path('course/popular', views.popular, name='course_popular'),
    path('course/<int:course_id>', views.view_course, name='view_course'),
    path('course/<int:course_id>/review', views.new_review, name='course_new_review'),
    path('course/public', views.index, name='course_public'),
    path('user/<int:user_id>', views.view_profile, name='user_view_profile'),
    path('user/notice', views.index, name='user_notice'),
    path('teacher/<int:teacher_id>', views.view_teacher_profile, name='view_teacher_profile'),
    path('user/account_settings', views.index, name='user_account_settings'),
    path('api/follow_course', api.follow_course, name='api_course_follow'),
    path('api/like_course', api.vote_thread, name='api_course_like'),
    path('api/review/upvote', api.review_upvote, name='api_review_upvote'),
    path('api/review/cancel_upvote', api.review_cancel_upvote, name='api_review_cancel_upvote'),
]
