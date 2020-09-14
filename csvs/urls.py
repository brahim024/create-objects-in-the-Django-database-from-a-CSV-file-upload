from django.urls import path
from .import views
app_name='csvs'
urlpatterns = [
	path('',views.upload_file,name="upload_file"),
	#path('csv',views.get_csv,name="csv"),

]