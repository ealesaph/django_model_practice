from django.shortcuts import render

# Create your views here.
def index(request):
    data={
        'titulo':'Index',
    }
    return render(request, 'index.html', data)


def personal(request):
    data={
        'titulo':'Personal',
        'empleados': ['Elvi Kingo','Elba Lazo', 'Elmo Thor', 'Elmar Tillo'],

    }    
    return render(request, 'personal.html', data)

def egresados(request):
    data={
        'titulo':'Egresados',
    }    
    return render(request, 'egresados.html', data)

def clientes(request):
    data={
        'titulo':'Clientes',
    }    
    return render(request, 'clientes.html', data)