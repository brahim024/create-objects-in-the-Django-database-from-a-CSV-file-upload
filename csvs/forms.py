from django import forms
from .models import Csvs
# create form here
class CsvsModelForm(forms.ModelForm):
	class Meta:
		model=Csvs
		fields=("file_name",)
