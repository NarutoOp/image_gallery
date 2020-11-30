from django.db import models

# Create your models here.
class image(models.Model):
	options = [
        ('Unknown', 'Unknown'),
        ('Sketch', 'Sketch'),
        ('Nature', 'Nature'),
        ('Portrait', 'Portrait'),
        ('Cars', 'Cars'),
        ('Wildlife', 'Wildlife'),
    ]
	tag = models.CharField(max_length=255,choices=options,default='Unknown')
	img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.img

	def delete(self,*args,**kwargs):
		self.img.delete()
		super().delete(*args,**kwargs)