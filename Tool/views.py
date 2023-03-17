from django.shortcuts import render, redirect
from .forms import DietForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    return render(request, 'html_files/Home.html')


def New_DietForm(request):
    global file_path
    if request.method == 'POST':
        form = DietForm(request.POST, request.FILES)

        sample_file = request.FILES['Fecal_sample']
        file_path = sample_file.name

        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.save()
            form = DietForm()
            return redirect('results.html')

    else:
        form = DietForm()

    return render(request, 'html_files/form.html', {'form': form})


def bracken():
    files = open('PATH.txt', 'a')
    files.write("/home/heba/Faculty/Graduation project/Auto_Diet/media/" + file_path)
    files.write("\n")
    files.close()
    return "Your Form Uploaded Successfully"


def results(request):
    return render(request, 'html_files/results.html', {'bracken': bracken})
