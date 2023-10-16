from django.urls import path, include
import cabinet.views as v
urlpatterns = [
    path('personal/', v.personal, name="personaled"),
]
