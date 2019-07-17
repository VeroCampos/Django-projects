from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shows

# Create your views here.
def index(request):
  
    context={
        "show": Shows.objects.all()
    }
    return render(request, "TVshows/index.html", context)

def new(request):

    return render(request, 'TVShows/new.html')

def create(request):
    #pass data to the method we wrote in models.py
    errors = Shows.objects.validator(request.POST)
    if len(errors)>0:
        for key, error in errors.items():
            messages.error(request, error)
        return render(request,'TVShows/new.html')

    else:
        #request.method == "POST":
        the_show=Shows.objects.create(title=request.POST["title"], netw=request.POST["netw"], release=request.POST["release"], 
        desc=request.POST["desc"])
        print(request.POST)
        Shows_id=the_show.id
    return redirect(f'/shows/{Shows_id}')

def shows(request, Shows_id):
    #dm.author.all()
    context = {
        "show": Shows.objects.get(id=Shows_id),  
    }
    return render(request,'TVShows/shows.html', context)

def shows_edit(request, Shows_id):
    context = {
        "show": Shows.objects.get(id=Shows_id),  
    }
    return render(request, "TVshows/edit.html", context)

def updating(request, Shows_id):
    errors = Shows.objects.validator(request.POST)
    if len(errors)>0:
        for key, error in errors.items():
            messages.error(request, error)
        return render(request,'TVshows/edit.html')
        
    else:
        the_show=Shows.objects.get(id=Shows_id)
        the_show.title=request.POST["title"]
        the_show.netw=request.POST["netw"]
        the_show.release=request.POST["release"]
        the_show.desc=request.POST["desc"]
        the_show.save()
       
        Shows_id=the_show.id

        return redirect(f'/shows/{Shows_id}')

def destroy(request, Shows_id):
    the_show=Shows.objects.get(id=Shows_id)
    the_show.delete()
    
    return redirect('/shows')

# Create your views here.
