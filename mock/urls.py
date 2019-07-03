from django.urls import path

from . import views, api
"""
set unfinished path's default as index
"""
app_name = 'mock'
urlpatterns = [
    path(r'<int:page>', views.index, name='index'),
    path(r'logout', views.not_found, name='logout'),
    path(r'test', views.test, name='test'),
    path('forget', views.test, name='forgetPassword'),
    path('search/', views.not_found, name='search'),
    path('not_found', views.not_found, name='not_found'),
    path('about/', views.about, name='about'),
    path('community-rules/', views.community_rules, name='about'),
    path('latest_reviews/<int:page>', views.latest_reviews, name='latest_reviews'),
    path('follow_reviews/<int:page>', views.follow_reviews, name='follow_reviews'),
    path('catalog/<int:page>', views.catalog, name='catalog'),
    path('course', views.index, name='course_index'),
    path('course/popular/<int:page>', views.popular, name='course_popular'),
    path('course/<str:course_id>', views.view_course, name='view_course'),
    path('course/<int:course_id>/review', views.new_review, name='course_new_review'),
    path('course/public', views.index, name='course_public'),
    path('user/<int:user_id>', views.view_profile, name='user_view_profile'),
    path('user/notice', views.index, name='user_notice'),
    path('teacher/<int:teacher_id>', views.view_teacher_profile, name='view_teacher_profile'),
    path('user/account_settings', views.index, name='user_account_settings'),
    path('api/follow_course', api.follow_course, name='api_course_follow'),
    path('api/review/upvote', api.review_upvote, name='api_review_upvote'),
    path('api/review/downvote', api.review_downvote, name='api_review_downvote'),
    path('api/review/cancel_vote', api.review_cancel_vote, name='api_review_cancel_vote'),
    path('api/submit_review', api.submit_review, name='api_submit_review')
]
