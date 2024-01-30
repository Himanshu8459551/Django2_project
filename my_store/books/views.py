from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .forms import MemberForm

# Create your views here.
def hello(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())

def book(request):
    book_list = Book.objects.all().values()
    context ={
       'book_list':book_list
      }
    template = loader.get_template('book.html')
    return HttpResponse(template.render(context,request))

def detail(request, id):
    mybook = Book.objects.get(id=id)
    template = loader.get_template('detail.html')
    context ={ 
        'mybook': mybook
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def new(request):
    if request.method =='POST':
        title =request.POST.get('titel',)
        description =request.POST.get('description',)
        price =request.POST.get('price',)
        image = request.FILES['image']
        b1=Book(title=title,description=description,price=price)
        b1.save()
    template = loader.get_template('new.html')
    return HttpResponse(template.render())

def update(request,id):
    b1 = Book.objects.get(id=id)
    form = MemberForm(request.POST,instance=b1)
    if form.is_valid():
        form.save()
        t1 = loader.get_template('new.html')
        return HttpResponse(t1.render())
    return render(request, 'update.html',{'form':form,'Book':b1})

@csrf_exempt
def delete(request,id):
    if request.method == 'POST':
        b1 = Book.objects.get(id=id)
        b1.delete()
        t1 = loader.get_template('book.html')
        return HttpResponse(t1.render())
    return render(request, 'delete.html')
