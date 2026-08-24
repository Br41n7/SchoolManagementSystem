from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit
from .models import AdmissionApplication


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ["full_name", "email", "phone", "gender", "date_of_birth", "address", "program",
                  "olevel_result", "jamb_reg_number", "jamb_score", "passport_photo"]
        exclude = ['status', 'submitted_at']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Apply for Admission',
                Field('full_name'),
                Field('email'),
                Field('phone'),
                Field('gender'),
                Field('date_of_birth'),
                Field('address'),
                Field('program'),
                Field('olevel_result'),
                Field('jamb_reg_number'),
                Field('jamb_score'),
                Field('passport_photo'),
            ),
            ButtonHolder(
                Submit('submit', 'Next', css_class='btn-primary')
            )
        )
