from django.shortcuts import render
from .models import DietModel
from .forms import DietForm
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
def home(request):
    return render(request, 'html_files/Home.html')


def New_DietForm(request):
    if request.method == 'POST':
        form = DietForm(request.POST, request.FILES)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form = DietForm()

    else:
        form = DietForm()

    return render(request, 'html_files/form.html', {'form': form})
