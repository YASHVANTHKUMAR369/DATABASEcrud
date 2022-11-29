from django import forms
from crudApp.models import Student
class StudentForm(forms.ModelForm):
   class Meta:
        model = Student
        fields = '__all__'
        
        
#Data --> information
#Meta data --> Data about Data
