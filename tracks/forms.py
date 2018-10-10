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

    def __init__(self, **kwargs):
        is_superuser = kwargs.pop('is_superuser')
        super().__init__(**kwargs)
        if not is_superuser:
            self.fields.pop('complete')

    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(user.username)
    #     self.fields.pop('complete')
