from django.urls import path
from SignupApp.views import SignUpView, UserListCreateView, UserRetrieveUpdateDestroyView


app_name = 'SignupApp'

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
     path('api/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]