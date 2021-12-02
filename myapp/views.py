from django.shortcuts import render, redirect
from .forms import SnippetForm

# Create your views here.


def contact(request):
    return render(request, 'home.html')

def link_one(request):
    return render(request, 'link_one.html')

# def subform(request):
#     return render(request, 'form.html' )

def drop_one(request):
    return render(request, 'drop_one.html')

def drop_two(request):
    return render(request, 'drop_two.html')

def drop_three(request):
    return render(request, 'drop_three.html')

def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(snippet_detail)              #################### redirect

    form = SnippetForm()
    return render(request, 'form.html',{'form': form})