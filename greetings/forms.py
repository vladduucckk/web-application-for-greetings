from django import forms
from .models import Researcher


class GreetingForm(forms.ModelForm):
    name = forms.CharField(label="name", max_length=30, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Vasyan228'}))

    class Meta:
        model = Researcher
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if Researcher.objects.filter(name=name).count() > 0:
            raise forms.ValidationError("This name is already taken")
        elif len(name) < 6:
            raise forms.ValidationError("The minimum length of the name must be 6 characters")
        else:
            return name


class EmailForm(forms.Form):
    email = forms.EmailField(label="email", max_length=254, required=True,
                             error_messages={
                                 'required': "Please enter only an email, do not enter a credit card number))"},
                             widget=forms.EmailInput(attrs={'placeholder': 'vasyan228@gmail.com'}))
