from django.urls import path, include
from .views import CreateUserView, NoteListCreate, NoteDelete, CoinListCreate, CoinDelete
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)



urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name='register'),
    
    path('token/', TokenObtainPairView.as_view(), name='get_token'),

    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),

    path('api-auth', include('rest_framework.urls')),

    path('notes/', NoteListCreate.as_view(), name='note-list'),
    
    path('coins/add/', CoinListCreate.as_view(), name='coin-list'),

    path('coins/delete/<int:pk>/', CoinDelete.as_view(), name='delete-coin'),
    path('notes/delete/<int:pk>/', NoteDelete.as_view(), name='delete-note'),
]
