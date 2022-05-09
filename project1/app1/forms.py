from django import forms
from.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'sid':'Student Id',
            'name':'Student Name',
            'marks': 'Marks',
            'sdept': 'Student Department',
            'address': 'Address'
        }

        widgets ={
            'sid': forms.NumberInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Enter Student ID',
            })
        }