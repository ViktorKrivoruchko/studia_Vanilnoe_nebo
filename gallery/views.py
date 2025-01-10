from django.shortcuts import render, redirect
from .models import Album, Photo 
from .forms import AlbumForm, PhotoForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'gallery/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'gallery/album_detail.html', {'album': album})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = PhotoForm()
    return render(request, 'gallery/upload_photo.html', {'form': form})
