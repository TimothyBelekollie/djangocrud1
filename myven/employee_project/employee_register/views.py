from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    data=Employee.objects.all()
    context={"data":data}
    return render(request,'employee_register/employee_list.html',context)
    

# def add(request):
#     form=EmployeeForm()
#     if request.method=='POST':
#         form=EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index_employee')
#     return render(request,'employee_register/employee_form.html',{'form':form})

def add(request, id=0):
    if request.method=="GET":
        if id==0:
           form =EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:
        if id==0:
           form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST, instance= employee)
            form.save()
    if form.is_valid():
            form.save()
            return redirect('index_employee')
     
    
def destroy(request,id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('index_employee')
    