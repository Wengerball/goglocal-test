from django.urls import path
from .views import LoginView, UserDetailsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('user/', UserDetailsView.as_view(), name='user-details')
]
