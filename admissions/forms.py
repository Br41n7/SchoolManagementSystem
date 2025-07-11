from django import forms
from .models import AdmissionApplication, UploadedDocument


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ["full_name", "email", "phone", "date_of_birth", "address", "program","olevel_result","jamb_reg_number","jamb_score","passport_photo"]
        exclude = ['status','submitted_at']
        widgets={
            'date_of_birth':
            forms.DateInput(attrs={'type':'date'}),
        }


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ["doc_type", "file"]
