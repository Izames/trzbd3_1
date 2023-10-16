from django.urls import path, include
import api.views as v
urlpatterns = [
    path('', v.api, name="apied"),
    path('create/', v.apiCr, name="apiedCr"),
    path('delete/', v.apiDe, name="apiedDe"),
    path('edit/', v.apiEd, name="apiedEd"),
    path('check/', v.apiCh, name="apiedCh"),
]
