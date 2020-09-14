from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRODUCT_CHOICES=(
	('TV','tv'),
	('IPAD','ipad'),
	('PLAYSTATION','playstation'),
	)
class Sale(models.Model):
	product=models.CharField(max_length=20,choices=PRODUCT_CHOICES)
	seleman=models.ForeignKey(User,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField()
	total=models.FloatField(blank=True)
	created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return f"{self.product}-{self.quantity}"

	def save(self,*args,**kwargs):
		price=None
		if self.product=='TV':
			price=558,93
		elif self.product=='IPAD':
			price=298,23
		elif self.product=='PLAYSTATION':
			price=450,83
		else:
			pass
		self.total=price * self.quantity
		super().save(*args,**kwargs)


