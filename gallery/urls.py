from django.urls import path
from .views import (
	imageListView,
	imageDetailView,
	imageForm,
	imageFilterView,
	rotateRight,
	rotateLeft
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', imageListView.as_view(),name='home'),
	path('image/<int:pk>', imageDetailView.as_view(),name='img-detail'),
    path('form', imageForm,name="form"),
    path('tag/<str:tag>', imageFilterView.as_view(), name='tag-img'),
    path('rotateRight/<int:id>', rotateRight,name='rotate-right'),
    path('rotateLeft/<int:id>', rotateLeft,name='rotate-left')

]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)