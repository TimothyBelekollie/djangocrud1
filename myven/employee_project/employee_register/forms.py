from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"
    class Meta:
        model = Employee
        fields = ('fullName','mobileNumb', 'emp_code',  'position')
        
        labels={
            "fullName":'Full Name','mobileNumb':'Mobile Number','emp_code':'Employee Code','position':'Position'
        }
        


       
    
    