from django.urls import path
from .views import home, login, contact

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('login', login.Login.as_view(), name='login'),
    path('contact', contact.Contact.as_view(), name='contact'),
    path('logout', login.logout, name='logout'),
]