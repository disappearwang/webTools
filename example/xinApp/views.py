from django.shortcuts import render

# Create your views here.
from .scripts.toto import correction
from .forms import xinForm


def hello(request):
    if request.method == 'POST':
        # submit form
        print(request)
        form = xinForm(request.POST)

        name = form.data['name']
        print(name)
        correction(name)
    else:
        form = xinForm()


    return render(request, 'xinApp/hello-world.html', {'form':form})
