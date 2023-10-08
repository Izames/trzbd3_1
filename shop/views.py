from django.shortcuts import render, HttpResponse

def shop(request):
    return render(request, 'shop/catalogPage1.html')
def shop2(request):
    return render(request, 'shop/catalogPage2.html')
def add(request):
    return render(request, 'shop/addPage.html')
def check(request, a):
    return render(request, 'shop/showPage.html', {'a': a})
def edit(request, a):
    return render(request, 'shop/editPage.html', {'a': a})
def feedback(request):
    return render(request, 'shop/feedbackPage.html')