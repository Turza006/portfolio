from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})


def create(request):
    
    if request.method == 'POST':

        if request.POST['summary'] and request.POST['name'] :
            job = Job()
            job.image = request.FILES['image']
            job.summary = request.POST['summary']
            job.name = request.POST['name']
            job.save()
            return render(request, 'jobs/create.html',{'error':'Image Added'})
        else:
            return render(request, 'jobs/create.html',{'error':'All field are required'})
    else:
        return render(request, 'jobs/create.html')



