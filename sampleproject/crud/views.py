from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from django.http import HttpResponse
import sys
from crud.models import Employee

# Create your views here.

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','age','gender','designation','department']


def employee_list(request, template_name = 'employee_list.html'):
    employee = Employee.objects.all()
    data = dict()
    data['object_list'] = employee
    return render(request,template_name,data)

def employee_create(request, template_name = 'employee_form.html'):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.INFO,'employee added successfully')
        messages.debug(request,'a debug information')
        messages.warning(request,'a note of information')
        messages.success(request,'adding successfully')
        messages.error(request,'a error message')

        return redirect('crud:employee_list')
    return render(request,template_name,{'form':form})

def employee_update(request,pk, template_name = 'employee_form.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('crud:employee_list')
    return render(request,template_name,{'form':form})

def employee_delete(request,pk,template_name = 'employee_confirmation_delete.html'):
    employee = get_object_or_404(Employee, pk = pk)
    if request.method=='POST':
        if request.POST['h1'] == 'yes':
            employee.delete()
        return redirect('crud:employee_list')
    return render(request, template_name, {'object': employee})

def employee_show(request,pk, template_name = 'employee_show.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.GET or None,instance=employee)
    return render(request,template_name,{'form':form})
