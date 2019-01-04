from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from materials import views

urlpatterns = [
    path('materials/', views.material_list),
    path('materials/<int:pk>/', views.material_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
