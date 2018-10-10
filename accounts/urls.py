from django.urls import path, include
from .views import (LoginView, DashboardView, CustomLoginView, UserDashboardView,
                    OverdueListView, SenderWiseListView)
app_name = 'accounts'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('user_dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('overdue/', OverdueListView.as_view(), name='overdue'),
    path('sender/<int:sender_pk>/', SenderWiseListView.as_view(), name='by-sender'),
    path('', include('django.contrib.auth.urls')),
]
