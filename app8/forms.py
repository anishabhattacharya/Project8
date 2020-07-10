from app8.models import CourseModel,FacultyModel,StudentModel
from django import forms
import re


class CourseForm(forms.ModelForm):
    fee = forms.FloatField(min_value=3000)
    class Meta:
        model= CourseModel
        fields="__all__"

    def clean_name(self):
        name=self.cleaned_data["name"]
        result=re.findall(r'^[A-Z a-z]*$',name)

        if result:
            return name
        else:
            raise forms.ValidationError("Invalid Name..will accepct only alphabets")

