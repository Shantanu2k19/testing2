from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context = {
        'count':32,
    }
    return render(request, "app/index.html", context)
