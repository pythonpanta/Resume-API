from django.urls import path
from . import views
urlpatterns = [
    path('',views.ResumeClass.as_view(),name='resume'),
]
