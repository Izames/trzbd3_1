from django.urls import path, include
import cart.views as v
urlpatterns = [
    path('cart/', v.cart, name="carted"),
]
