from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from ldap3 import Server, Connection, ALL

def login_view(request):
    contex = {
        'title': 'Simple Links'
    }
    if request.method == 'POST':
        # s = Server('ldap://192.168.1.11')
        # c = Connection(s, user=request.POST['username'] + "@sd.zain.com", password=request.POST['password'])	
        # c.bind()
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home/')
        else:
            contex['error'] = 'Wrong username or password'
            return render(request, 'login.html', contex)
    return render(request, 'login.html', contex)
