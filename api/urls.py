from django.urls import path,include
from . import views
urlpatterns=[
    path('api/staff',views.StaffAPI.as_view(),name='staff'),
    path('api/partner',views.PartnerAPI.as_view(),name='partner'),
    path('api/order',views.OrderAPI.as_view(),name='order'),
    path('api/basket',views.BasketAPI.as_view(),name='basket')
]