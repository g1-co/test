from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'Bs.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return render(request,'product.html')

