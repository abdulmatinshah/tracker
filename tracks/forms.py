from django import forms

from tracks.models import Track


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['remarks']

        widgets = {
            'remarks': forms.Textarea(attrs={'class': 'form-control'})
        }
