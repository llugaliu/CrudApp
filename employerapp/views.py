from django.shortcuts import render, redirect
from .models import Employer
from .forms import EmployerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def employer(request):
    employer = Employer.objects.all()
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employer added successfuly')
            return redirect('employer')
    else:
        form = EmployerForm()
    context = {
        'employer': employer,
        'form': form
    }
    return render(request, 'employer/employer.html', context)


@login_required()
def edit_employer(request, pk):
    employer = Employer.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employer was edited with success')
            return redirect('employer')
    else:
        form = EmployerForm(instance=employer)
    context = {
        'form': form,
        'employer': employer
    }
    return render(request, 'employer/edit.html', context)


@login_required
def delete_employer(request, pk):
    Employer.objects.filter(pk=pk).delete()
    messages.success(request, 'Employer was deleted with success')
    return redirect('employer')

