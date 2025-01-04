from app1.forms import PersonForm
from django.shortcuts import render
from app1.models import Person
from django.http import HttpResponse


# Create your views here.
def home(request):
    form=PersonForm()
    return render(request, "app1/index.html",{'form':form})

def data_send(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Data send")
    else:
        form=PersonForm()
    return render(request, "app1/index.html",{'form':form})

def data_view(request):
    if request.method =='GET':
        form=Person.objects.all()
        return render(request, "app1/view.html",{'form':form}) 
