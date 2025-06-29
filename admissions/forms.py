from django import forms
from .models import AdmissionApplication, UploadedDocument


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['full_name', 'email', 'phone',
                  'date_of_birth', 'address', 'program']


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['doc_type', 'file']
