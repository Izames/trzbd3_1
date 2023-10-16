from django.shortcuts import render

# Create your views here.
def api(request):
    return render(request, 'api/api.html')
def apiCr(request):
    return render(request, 'api/apiCr.html')
def apiDe(request):
    return render(request, 'api/apiDe.html')
def apiCh(request):
    return render(request, 'api/apiCh.html')
def apiEd(request):
    return render(request, 'api/apiEd.html')
