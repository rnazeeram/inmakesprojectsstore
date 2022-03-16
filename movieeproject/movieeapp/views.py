from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import moviee
from .forms import movieForm
# Create your views here.
def details(request,movie_id):
   movie=moviee.objects.get(id=movie_id)
   return render(request,'details.html',{'movie':movie})

def index(request):
   movie= moviee.objects.all()
   context={'movielist':movie}
   return render(request,'index.html',context)

def add_movie(request):

   if request.method=="POST":
       Mname=request.POST.get('name')
       Mdesc = request.POST.get('desc')
       Myear = request.POST.get('year')
       Mimg= request.FILES['image']
       movie=moviee(name=Mname,desc=Mdesc,year=Myear,img=Mimg)
       movie.save()
       return redirect('/')
   return render(request,'add.html')
def update(request,id):
    movie=moviee.objects.get(id=id)
    form=movieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form ,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=moviee.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


