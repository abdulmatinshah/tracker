from django.urls import path
from .views import (IndexView, TrackView, TrackDetail, TrackUpdate)
app_name = 'tracks'
urlpatterns = [
    path('', TrackView.as_view(), name='list'),
    path('<int:pk>/', TrackDetail.as_view(), name='detail'),
    path('<int:pk>/update/', TrackUpdate.as_view(), name='update'),
    path('index/', IndexView.as_view(), name='index'),
]
