from django.shortcuts import render
from .forms import ProjetoForm

# Create your views here.
def projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjetoForm()
    else:
        form = ProjetoForm()

    return render(request, 'form3/form.html', {'form': form})
