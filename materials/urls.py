from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from materials import views

urlpatterns = [
    path('textscore/', views.TextScore.as_view()),
    path('handouts/', views.HandoutList.as_view()),
    path('handouts/<int:pk>/', views.HandoutDetail.as_view()),
    re_path(r'^definitions/$', views.Definitions.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
