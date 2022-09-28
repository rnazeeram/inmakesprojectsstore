
from django.contrib import messages, auth
from .models import Invoice,District,City,Author,Book
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def branches(request):
    return render(request,'districts.html')
def order(request):
    if request.method=='POST':
        iname=request.POST['custname']
        iphnmbr=request.POST['phnumber']
        iemail = request.POST['email']
        iaddress= request.POST['address']
        idistrict = request.POST['Districts']
        icity = request.POST['City']
        iauthor=request.POST['Authors']
        ibook = request.POST['Books']
        customer= Invoice.objects.create_user(name=iname, district=idistrict, city=icity, author=iauthor, book=ibook)
        customer.save();
        messages.info(request, 'Your Order Taken Place. Thanks for shopping, please keep shop with us')
        return redirect('/')
    return render(request,'order.html')
# AJAX
# def load_cities(request):
#     district_id = request.GET.get('districts_id')
#     cities = City.objects.filter(district_id=district_id).all()
#     return render(request, 'order.html', {'cities': cities})
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)
# def load_book(request):
#     author_id = request.GET.get('Author')
#     books = Book.objects.filter(author_id=author_id).all()
#     return render(request,'order.html', {'books': books})