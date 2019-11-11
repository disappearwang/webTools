from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .scripts.correction import do_correction
from .forms import CorrectionForm, AnotherForm


def thanks(request):
    print(request)
    return HttpResponse('<h1>Thanks for using</h1>')


def another(request):
    if request.method == 'POST':
        form = AnotherForm(request.POST)
        print(form)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = AnotherForm()

    return render(request, 'correctionApp/anotherForm.html', {'form': form})


# Create your views here.
def hello_world(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CorrectionForm(request.POST)
        value = form.data['something1']
        print(value)
        do_correction(value)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CorrectionForm()

    return render(request, 'correctionApp/correctionForm.html', {'form': form})
