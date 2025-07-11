from django import forms
from .models import Applicant, ResultAppeal, Evaluation,Event
#
#
# class ApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Applicant
#         fields = ['full_name', 'email', 'phone', 'program']
#         widgets = {
#             'full_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'program': forms.Select(attrs={'class': 'form-select'}),
        # }


# class ResultAppealForm(forms.ModelForm):
#     class Meta:
#         model = ResultAppeal
#         fields = ['reason']
#         widgets = {
#             'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }
#
#
# class EvaluationForm(forms.ModelForm):
#     class Meta:
#         model = Evaluation
#         fields = ['rating', 'comment']
#         widgets = {
#             'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
#             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_type', 'description', 'start_time', 'end_time', 'course']
