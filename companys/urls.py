from django.urls import path
from .views import up_commodity_cate, up_commodity, gen_hash
from .login import login

urlpatterns = (
    path('', up_commodity_cate),
    path("add_commodity/", up_commodity, name="add_commodity"),
    path("hashgen/", gen_hash, name="gen_hash"),
    path("logins/", login, name="login")
)