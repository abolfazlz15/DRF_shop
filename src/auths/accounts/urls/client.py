from django.urls import path
from auths.accounts.views import client

urlpatterns = [
    path('regiser/', client.CreateUserView.as_view(), name='user_register'),
    path('vrify-otp/', client.VerifyOTPCodeView.as_view(), name='vrify_OTP_code'),
]