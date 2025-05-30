from django.urls import path
from .views import RegistrationView, ProfileView, PasswordResetWithRecoveryView, EmailVerificationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-reset/', PasswordResetWithRecoveryView.as_view(), name='password_reset'),
    path('auth/verify-email/', EmailVerificationView.as_view(), name='verify-email'),
]