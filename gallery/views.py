from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from .models import image
from .forms import *
from django.views.generic import ListView,DetailView
from PIL import Image as PilImage
# Create your views here.
def index(request):
	context = {
		'images': image.objects.all()
	}
	return render(request, 'gallery/index.html',context)

def imageForm(request):
	shows = image.objects.all()

	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = Form()
	return render(request, 'gallery/form.html',{
		'shows' : shows,
		'form' : form
	})

class imageListView(ListView):
	model = image
	template_name = 'gallery/index.html'
	context_object_name = 'images'
	paginate_by = 6

class imageDetailView(DetailView):
	model = image

class imageFilterView(ListView):
	model = image
	template_name = 'gallery/image_filter.html'
	context_object_name = 'images'
	

	def get_queryset(self):
		obj = self.kwargs.get('tag')
		return image.objects.filter(tag=obj)

def rotateLeft(request,id):
    #getting instance of the model
    item=image.objects.get(pk=id)

    #opening image for PIL to access
    im = PilImage.open(item.img)

    #rotating it by built in PIL command
    rotated_image = im.rotate(90)

    #saving rotated image instead of original. Overwriting is on. 
    rotated_image.save(item.img.file.name, overwrite=True)

    return redirect('/image/'+str(id))

def rotateRight(request,id):
    #getting instance of the model
    item=image.objects.get(pk=id)

    #opening image for PIL to access
    im = PilImage.open(item.img)

    #rotating it by built in PIL command
    rotated_image = im.rotate(270)

    #saving rotated image instead of original. Overwriting is on. 
    rotated_image.save(item.img.file.name, overwrite=True)

    # return HttpResponse(str(rotated_image.show()))
    return redirect('/image/'+str(id))