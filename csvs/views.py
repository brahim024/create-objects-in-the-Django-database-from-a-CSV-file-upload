from django.shortcuts import render
from .forms import CsvsModelForm
from .models import Csvs 
from sales.models import Sale
import csv
from django.contrib.auth.models import User
# Create your views here.
def upload_file(request):
	form= CsvsModelForm(request.POST or None , request.FILES or None)
	if form.is_valid():
		form.save()
		form=CsvsModelForm()
		obj=Csvs.objects.get(activated=False)
		with open(obj.file_name.path, 'r') as f:
			reader=csv.reader(f)
			for i, row in enumerate(reader):
				if i==0:
					pass
				else:
					row="".join(row)
					row =row.replace(";","   ")
					row =row.split()
					#print(row)
					product=row[1].upper()
					user=User.objects.all()
					Sale.objects.create(
							product=product,
							quantity=int(row[2]),
							saleman= user,

						)
					


			obj.activated=True
			obj.save()
	return render(request,'upload_file.html',{'form':form})
