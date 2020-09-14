from django.form import forms
from .models import Csv
# create form here
class CsvModelForm(forms.ModelForm):
	model=Csv
	fields=('file_name')
