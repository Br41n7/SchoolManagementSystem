from .models import StudentCourseRegistration
from django import forms


class StudentCourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentCourseRegistration
        fields = ['course', 'semester', 'session']
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'session': forms.TextInput(attrs={'class': 'form-control'}),
        }
