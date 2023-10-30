from django.urls import path, include
import cart.views as v
urlpatterns = [
    path('', v.cart, name="carted"),
]
