from django.urls import path
from auths.accounts.views import admin

app_name = 'accounts'
urlpatterns = [
    path('login/', admin.AdminLoginView.as_view(), name='admin_login')
]
