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
    path('user/account_settings', views.index, name='user_account_settings'),
    path('api/<int:course_id>/follow', api.follow, name='api_follow'),
    path('api/<int:course_id>/unfollow', api.unfollow, name='api_unfollow'),
    path('api/<int:course_id>/downvote', api.downvote, name='api_downvote'),
    path('api/<int:course_id>/undo_downvote', api.undo_downvote, name='api_undo_downvote'),
    path('api/<int:course_id>/upvote', api.upvote, name='api_upvote'),
    path('api/<int:course_id>/undo_upvote', api.undo_upvote, name='api_undo_upvote'),
    path('api/review/upvote', api.review_upvote, name='api_review_upvote'),
    path('api/review/cancel_upvote', api.review_cancel_upvote, name='api_review_cancel_upvote'),
    path('api/review/hide', api.hide_review, name='api_hide_review'),
    path('api/review/unhide', api.unhide_review, name='api_unhide_review'),
    path('teacher/<int:teacher_id>', views.view_teacher_profile, name='view_teacher_profile'),
    path('api/delete_comment', api.delete_comment, name='api_delete_comment'),
    path('api/show_comment', api.show_comments, name='api_show_comment'),
]
