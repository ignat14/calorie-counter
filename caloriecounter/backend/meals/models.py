from django.db import models
from accounts.models import User

# Create your models here.
class Meal(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=250, null=False, blank=False)
	date = models.DateField(null=False, blank=False)
	time = models.TimeField(null=False, blank=False)
	calories = models.IntegerField(null=False, blank=False)

	def __str__(self):
		return f"{self.description} / {self.calories} Calories"
