from django.contrib import admin
from django.urls import path, re_path
from .views import query_commidty, check_commodity, emu_commodity
urlpatterns = (
    # path('', review),
    path('commodity/<hash_code>', query_commidty, name="query_commodity"),
    re_path(r'commodity_check/.*', check_commodity, name="check_commodity"),
    path('all_commodity/', emu_commodity, name="emu_commodity")
)