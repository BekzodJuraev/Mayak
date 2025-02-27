from django.urls import path,include
from . import views
urlpatterns=[
    path('api/staff',views.StaffAPI.as_view(),name='staff'),
    path('api/partner',views.PartnerAPI.as_view(),name='partner')
]