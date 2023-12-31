from django.urls import path, include

import api.routing
import cabinet.routing
import cart.routing
import shop.views as v
urlpatterns2 = [
    path('', v.check, name="cheked"),
    path('edit/', v.edit, name="edited")
]
urlpatterns = [
    path('', v.main, name="main"),
    path('shop/', v.shop, name="shoped"),
    path('catalog2/', v.shop2, name="shoped2"),
    path('catalog2/add', v.add, name="added"),
    path('check/<int:a>/', include(urlpatterns2)),
    path('feedback/', v.feedback, name="fb"),
    path('api/', include(api.routing.urlpatterns)),
    path('cart/', include(cart.routing.urlpatterns)),
    path('', include(cabinet.routing.urlpatterns)),
]
