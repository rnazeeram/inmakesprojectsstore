from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import team
# Create your views here




def demo(request):
    obj= place.objects.all()
    obj2=team.objects.all()
    return render(request,'index1.html',{'result':obj,'result2':obj2})
#def show(request):
 #  val1="ameen"
 #  val2="fahmi"
  # val3="asma"
  # return render(request,"index.html",{'obj1':val1,'obj2':val2,'obj3':val3})
# about(request):
   #return HttpResponse("hii pls submit your name ")
#def contact(request):
  # return render(request,"contact.html")
#def details(request):
 #  return HttpResponse("submit your dtails")
#def thanks(request):
#   return render(request,"thanks.html")
 #def addition(request):
  # x=int(request.GET['num1'])
  # y=int(request.GET['num2'])
   #res=x+y
  # res2=x-y
  # res3=x*y
  # res4=x/y
  # return render(request,"result.html",{'n1':x,'n2':y,'result':res,'result2':res2,'result3':res3,'result4':res4})
#def addform(request):
   #return render(request,"addform.html")