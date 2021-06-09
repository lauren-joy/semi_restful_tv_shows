
from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, "index.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')

    Show.objects.create(
        title= request.POST['title'],
        network= request.POST['network'],
        release_date=request.POST['release_date'],
        description= request.POST['description'],
    )
    return redirect('/shows/')

def edit(request, show_id):
    single_show= Show.objects.get(id=show_id)
    context = {
        'show': single_show
    }
    return render(request, "edit.html", context)

def info(request, show_id):
    single_show= Show.objects.get(id=show_id)
    context = {
        'show': single_show
    }
    return render(request, "info.html", context)

def update(request, show_id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/shows/{show_id}/edit')

    make_update= Show.objects.get(id=show_id)
    make_update.title= request.POST['title']
    make_update.release_date= request.POST['release_date']
    make_update.network= request.POST['network']
    make_update.description= request.POST['description']
    make_update.save()
    return redirect(f'/shows/{show_id}') 

def delete(request, show_id):
    make_delete= Show.objects.get(id=show_id)
    make_delete.delete()
    return redirect('/shows/')