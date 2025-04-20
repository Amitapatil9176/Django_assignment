from django.shortcuts import render, redirect, get_object_or_404
from .models import Office
from .forms import OfficeForm

def office_list(request):
    offices = Office.objects.all()
    return render(request, 'emp/office_list.html', {'offices': offices})

def add_office(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_list')
    else:
        form = OfficeForm()
    return render(request, 'emp/add_office.html', {'form': form})

def office_detail(request, pk):
    office = get_object_or_404(Office, pk=pk)
    return render(request, 'emp/office_detail.html', {'office': office})

def edit_office(request, pk):
    office = get_object_or_404(Office, pk=pk)
    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('office_list')
    else:
        form = OfficeForm(instance=office)
    return render(request, 'emp/edit_office.html', {'form': form})

def delete_office(request, pk):
    office = get_object_or_404(Office, pk=pk)
    if request.method == 'POST':
        office.delete()
        return redirect('office_list')
    return render(request, 'emp/delete_confirm.html', {'office': office})
