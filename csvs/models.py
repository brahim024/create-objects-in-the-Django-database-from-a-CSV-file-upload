from django.db import models

# Create your models here.
class Csvs(models,Model):
	file_name=models.FileField(upload_to='csvs')
	upload_date-models.DateTimeField(auto_now=True)
	activated=models.BooleanField(default=False)
	def __str__(self):
		return f"File id: {self.id}"
		
