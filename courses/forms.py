from django import forms
from .models import Course, CourseRegistration


class CourseRegistrationForm(forms.Form):
    semester = forms.ChoiceField(choices=[("first", "First"), ("second", "Second")])
    session = forms.CharField(max_length=9)

    def _init_(self, *args, **kwargs):
        student = kwargs.pop("student")
        super()._init_(*args, **kwargs)
        self.fields["courses"] = forms.ModelMultipleChoiceField(
            queryset=Course.objects.fiter(level=student.level),
            widget=forms.CheckboxSelectMultiple,
        )
