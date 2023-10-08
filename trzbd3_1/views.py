from django.shortcuts import render, HttpResponse
from django.urls import reverse

def main(request):
    return render(request, 'start_page.html')
def api(request):
    return render(request, 'api.html')
def personal(request):
    return render(request, 'personal.html')
def cart(request):
    return render(request, 'cart.html')
