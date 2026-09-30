from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'titulo':'Index',
    }
    return render(request,'index.html',data)

def postres(request):
    data ={
            'titulo':'Postres',
    }
    return render(request,'postres.html',data)

def sandwich(request):
    data = {
        'titulo':'Sandwich',
    }
    return render(request,'sandwich.html',data)

