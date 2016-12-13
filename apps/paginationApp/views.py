from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# from django.contrib import messages
# from .forms import RegistrationForm
from .models import User
#CONTROLLER
#Create your views here.
def index(request):
    # User.objects.create(firstName="Symantha", lastName="Smith", email="sym@hotmail.com")
    # User.objects.create(firstName="Victor", lastName="Gonza", email="victor@hotmail.com")
    # User.objects.create(firstName="Mia", lastName="Shy", email="mia@hotmail.com")
    # User.objects.create(firstName="Lola", lastName="Humphry", email="lola@hotmail.com")
    # User.objects.create(firstName="Jennifer", lastName="Circo", email="jen@hotmail.com")
    # User.objects.create(firstName="Hannah", lastName="Dolph", email="hannah@hotmail.com")
    # User.objects.filter(id=2).delete()
    if(request.method == 'POST'):
        return render(request, 'paginationApp/index.html', User.objects.getUsers(request.POST))
    return render(request, 'paginationApp/index.html', User.objects.getUsers(None))
