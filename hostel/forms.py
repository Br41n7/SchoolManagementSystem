from .models import HostelApplication, Hostel
from django import forms


class HostelApplicationForm(forms.ModelForm):
    class Meta:
        model = HostelApplication
        fields = ['hostel']
        widgets = {
            'hostel': forms.Select(attrs={'class': 'form-control'}),
        }

    def _init_(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super()._init_(*args, **kwargs)
        self.fields['hostel'].queryset = Hostel.objects.all()
