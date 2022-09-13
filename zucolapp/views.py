from django.shortcuts import render 
from zucolapp.models import registration
from  django.http import  HttpResponseRedirect

def submit(request):
    if request.method == "POST":
        name = request.POST['username']
        date = request.POST['date']
        number = request.POST['phone_number']

        users = registration(user=name,Travel_date=date,Phone_number=number)
        users.save()
        return HttpResponseRedirect('secondpage')
    return render(request, "index.html")


def secondpage(request):
    return render(request, "secondpage.html")
        