from django.urls import path
from .views import *

urlpatterns = [
    path('', signin_view, name='sign-in'),
    path('user-detail/<int:pk>/', user_detail, name='user-detail'),
    path('user-update/<int:pk>/', user_update, name='user-update'),
    path('user-password-update/<int:pk>/', user_password_update, name='user-password-update'),
    path('log-out/<int:pk>/', logout_view, name='log-out'),
    path("admin-page/", home_view, name="dashboard"),
    path('search-applicants/', search_applicants, name='search-applicants'),
    path("banner/", banner_view, name="banner"),
    path('direction-title/', direction_title, name='direction-title'),
    path('create-direction-title/', create_direction_title, name='create-direction-title'),
    path('update-direction-title/<int:pk>/', update_direction_title, name='update-direction-title'),
    path('direction-courses/', direction_courses, name='direction-courses'),
    path('create-direction/', create_direction, name='create-direction'),
    path('update-direction/<int:pk>/', update_direction, name='update-approach'),
    path('delete-direction/<int:pk>/', delete_direction, name='delete-approach'),
    path("create-banner/", create_banner_view, name="create-banner"),
    path('update-banner/<int:pk>/', update_banner_view, name='update-banner'),
    path('delete-banner/<int:pk>/', delete_banner, name='delete-banner'),
    path('about-title/', about_title_view, name='about-title'),
    path('modal-about/<int:pk>/', modal_about, name='modal-about'),
    path('create-about-title/', create_about_title, name='create-ab-tit'),
    path('upd-abo-tit/<int:pk>/', update_about_title, name='upd-ab-tit'),
    path('del-ab-title/<int:pk>/', delete_about_title, name='del-ab-tit'),
    path('about-project/', about_project, name='about-project'),
    path('cre-abt-item/', create_about_item, name='cre-abt-item'),
    path('upd-abo-item/<int:pk>/', update_about_items, name='update-about-item'),
    path('del-abt-item/<int:pk>/', delete_about_item, name='delete-about-item'),
    path('info/', info_view, name='info'),
    path('all-info/', all_info, name='all-info'),
    path('create-info/', create_info, name='create-info'),
    path('update-info/<int:pk>/', update_info, name='update-info'),
    path('task-titles/', task_title, name='task-title'),
    path('create-task-title/', create_task_title, name='create-task-title'),
    path('update-task-title/<int:pk>/', update_task_title, name='update-task-title'),
    path('task-page/', tasks_view, name='task-page'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:pk>/', update_tasks, name='update-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
    path('result-title/', result_title, name='result-title'),
    path('create-result-title/', create_result_title, name='create-result-title'),
    path('update-result-title/<int:pk>/', update_result_title, name='update-result-title'),
    path('result-page/', result_view, name='result-page'),
    path('create-result/', create_result, name='create-result'),
    path('update-result/<int:pk>/', update_result, name='update-result'),
    path('delete-result/<int:pk>/', delete_result, name='delete-result'),
    path('approach-paginator/', approach_item_paginator, name='approach-item-paginator'),

]
