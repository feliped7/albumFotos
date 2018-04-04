from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

# Create your views here.

def first_view(request):
    return HttpResponse('Esta es mi primera vista!')

def category(request):
    category_list = Category.objects.all()
    context = {'object_list': category_list}
    return render(request, 'album/category.html', context)

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'object': category}
    return render(request, 'album/category_detail.html', context)

def base(request):
	return render(request, 'base.html')

class PhotoListView(ListView):
    model = Photo
class PhotoDetailView(DetailView):
    model = Photo

    '''def get_object(self):
        return get_object_or_404(Category, pk=request.session['user_id'])'''

class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__'

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model = Photo
    fields = '__all__'
    success_url = reverse_lazy('photo-list')