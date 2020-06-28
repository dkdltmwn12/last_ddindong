from django.urls import path
from finish import views

app_name = "finish"

urlpatterns = [
    path("", views.form_test, name="search"),
    path("register/", views.register),
    path("login/", views.login),
    path("logout/", views.logout),
    path("lhome/", views.lform_test, name="lsearch"),
]
