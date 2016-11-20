from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# from django.contrib import messages
# from .forms import RegistrationForm
from .models import User
#CONTROLLER
#Create your views here.
def index(request):
    # User.objects.create(firstName="Evan", lastName="Callia", email="soccer_evan4@hotmail.com")
    # User.objects.create(firstName="asdf", lastName="Callfdsaia", email="soccer_evan4@hotmail.com")
    # User.objects.create(firstName="Joe", lastName="Depew", email="depew@hotmail.com")
    # User.objects.create(firstName="Jeff", lastName="Kwok", email="jeff@hotmail.com")
    # User.objects.create(firstName="Laurel", lastName="Rice", email="rice@hotmail.com")
    # User.objects.create(firstName="Fran", lastName="L", email="Fran@hotmail.com")
    if(request.method == 'POST'):
        return render(request, 'paginationApp/index.html', User.objects.getUsers(request.POST))
    return render(request, 'paginationApp/index.html', User.objects.getUsers(None))
