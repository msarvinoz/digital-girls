from django import urls
from django.urls import path, include
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Digital Girls API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('main-page/', main_page),
    path('about/', about, name='about-title'),
    path('about-items/', about_items, name='about-items'),
    path('direction/', direction),
    path('direction-items/', direction_items),
    path('tasks/', tasks),
    path('task-items/', task_items),
    path('result/', result),
    path('result-items/', results_items),
    path("info/", info),
    path('register/', register)
]
