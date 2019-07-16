from django.urls import path
from .views import review
from .login import login
urlpatterns = (
    path('up_review/', review, name="up_review"),
    path(r"logins/", login, name="login"),
)