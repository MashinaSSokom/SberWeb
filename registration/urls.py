from django.contrib.auth.views import LoginView
from django.urls import path


urlpatterns = [
    #path('registration/', views.registr),
    path('login/', LoginView.as_view(), name='login'),
]
