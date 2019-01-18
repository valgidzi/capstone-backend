from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from materials import views

urlpatterns = [
    path('materials/', views.MaterialList.as_view()),
    path('materials/<int:pk>/', views.MaterialDetail.as_view()),
    path('texts/', views.TextList.as_view()),
    path('handouts/', views.HandoutList.as_view()),
    path('handouts/<int:pk>/', views.HandoutDetail.as_view()),
    re_path(r'^definitions/$', views.Definitions.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
