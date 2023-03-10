from django.shortcuts import render, redirect
from .models import DietModel
from .forms import DietForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    return render(request, 'html_files/Home.html')


def results(request):
    return render(request, 'html_files/results.html')


def New_DietForm(request):
    if request.method == 'POST':
        form = DietForm(request.POST, request.FILES)

        sample_file = request.FILES['Fecal_sample']
        fs = FileSystemStorage()
        sample_filename = fs.save(sample_file.name, sample_file)
        uploaded_file_path = fs.path(sample_filename)

        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form = DietForm()
            return redirect('results.html')

    else:
        form = DietForm()

    return render(request, 'html_files/form.html', {'form': form})
