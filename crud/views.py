from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Mahasiswa

# Create your views here.
def index(request):
    mahasiswa_list = Mahasiswa.objects.all()
    context = {'mahasiswa_list': mahasiswa_list}
    return render(request, 'index.html', context)

def detail(request, nrp):
    try:
        detail_list = list(Mahasiswa.objects.values().filter(nrp=nrp))[0].items()
        context = {'detail_list': detail_list, 'nrp': nrp}
    except Exception as e:
        print(e)
    return render(request, 'details.html', context)

def insert(request):
    if(request.method == 'POST'):
        mhs = Mahasiswa(
                nrp=request.POST['nrp'], 
                nama=request.POST['nama'],
                umur=request.POST['umur'],
                gender=request.POST['gender'],
                alamat=request.POST['alamat'])
        mhs.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'insert.html')

def update(request, nrp):
    if(request.method == 'POST'):
        try:
            mhs = Mahasiswa.objects.get(nrp=nrp)
            mhs.nrp = request.POST['nrp']
            mhs.nama = request.POST['nama']
            mhs.umur = request.POST['umur']
            mhs.gender = request.POST['gender']
            mhs.alamat = request.POST['alamat']
            mhs.save()
        except Exception as e:
            print(e)
        return redirect('detail', nrp=request.POST['nrp'])
    else:
        input_dict = list(Mahasiswa.objects.values().filter(nrp=nrp))[0]
        context = {'input_dict': 1, **input_dict}
        return render(request, 'update.html', context)

def delete(request, nrp):
    try:
        Mahasiswa.objects.filter(nrp=nrp).delete()
    except Exception as e:
        print(e)
    return redirect(index)

