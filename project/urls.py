from django.contrib import admin
from django.urls import path, include
# from registration import views
from django.views.generic import RedirectView

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.urls'), name='accounts'),
    path('', RedirectView.as_view(pattern_name='registration'), name='home')
]
