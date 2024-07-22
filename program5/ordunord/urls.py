from django.urls import path
from .import views
urlpatterns=[
    path('',views.display_lists,name='display_lists')
]