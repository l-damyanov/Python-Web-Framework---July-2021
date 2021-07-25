from django import forms

from templates_advanced.pythons_app.models import Python


# def __init__(self, *args, **kwargs):
#     super(PythonCreateForm, self).__init__(*args, **kwargs)
#     self.fields['description'].strip = False

class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        fields = '__all__'
