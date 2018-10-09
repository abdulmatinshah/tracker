from django.urls import path
from .views import (IndexView, TrackView, TrackDetail, TrackUpdate,
                    OverdueListView, SenderWiseListView, AssigneeWiseListView)
app_name = 'tracks'
urlpatterns = [
    path('', TrackView.as_view(), name='list'),
    path('<int:pk>/', TrackDetail.as_view(), name='detail'),
    path('<int:pk>/update/', TrackUpdate.as_view(), name='update'),
    path('overdue/', OverdueListView.as_view(), name='overdue'),
    path('sender/<int:sender_pk>/', SenderWiseListView.as_view(), name='list-by-sender'),
    path('assignee/<int:assignee_pk>/', AssigneeWiseListView.as_view(), name='list-by-assignee'),
]
