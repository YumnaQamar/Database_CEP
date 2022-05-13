from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Books,Reader,Reports,Publisher
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
   Bookss = Books.objects.all()
   return render(request, 'index.html', {'Books':Bookss})
# Create your views here.


def loginop(request):
   return render(request, 'loginop.html')


def login_page(request):
   return render(request, 'login_page.html')



def signup(request):
    return render(request, 'signup.html')


def index_two(request):
   Bookss = Books.objects.all()
   reader=Reader.objects.all()
   reports=Reports.objects.all()
   publisher=Publisher.objects.all()
   return render(request, 'index_two.html' , {'Books':Bookss,'Reader':reader,'Reports':reports,'Publisher':publisher})

def index(request):
   return render(request, 'index.html')

def user_login(request):
   return render(request, 'login_page.html')

def admin_login(request):
   return render(request, 'login_page2.html')

def book(request):
   Bookss = Books.objects.all()
   return render(request, 'book.html', {'Books':Bookss})

