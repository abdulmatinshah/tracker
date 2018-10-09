from django import forms

from tracks.models import Track


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['remarks', 'complete']

        widgets = {
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
            # 'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
