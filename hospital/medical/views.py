from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Specialty, Doctor
from django.http import JsonResponse
from .form import SpecialtyForm, DoctorForm

# Create your views here.
def specialty_list(request):
    specialty = Specialty.objects.all()
    form = SpecialtyForm()
    return render(request, 'categorias/especialty_.html', {'specialty': specialty, 'form': form})

def specialty_detail(request, pk):
    detail = Specialty.objects.get(pk=pk)
    data = {
        'id': detail.id,
        'name': detail.name,
        'description': detail.description,
        'status': detail.status
    }
    return JsonResponse(data)

def specialty_create(request ):
    if request.method == 'POST':
        form =SpecialtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialty_list')        
        else:
            return render(request, 'categorias/especialty_.html', {'form': form})

def specialty_edit(request, pk):
    specialty = Specialty.objects.get(pk =pk)
    if request.method == 'POST':
        form = SpecialtyForm(request.POST, instance = specialty)
        if form.is_valid():
            form.save()
            return redirect('specialty_list')
        else:
            return render(request, 'categorias/especialty_.html', {'form': form})
    data = {
        'id': specialty.id,
        'name': specialty.name,
        'description': specialty.description,
        'status': specialty.status
    }
    return JsonResponse(data)

def specialty_delete(request, pk):
    Specialty.objects.get(pk=pk).delete()
    return redirect('specialty_list')

def changeStatus(request, pk):
    if request.method == 'POST':
        specialty = Specialty.objects.get(pk=pk)
        specialty.status = not specialty.status
        specialty.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})




def doctor_list(request):
    doctor = Doctor.objects.all()
    form = DoctorForm()
    return render(request, 'categorias/doctor_.html', {'doctor': doctor, 'form': form})

def doctor_detail(request, pk):
    detail = Doctor.objects.get(pk=pk)
    data = {
        'id': detail.id,
        'first_name': detail.first_name,
        'last_name': detail.last_name,
        'email': detail.email,
        'document': detail.document,
        'phone_number':detail.phone_number,
        'license_number': detail.license_number,
        'date_of_birth': detail.date_of_birth,
        'years_of_experience': detail.years_of_experience,
        'gender':detail.gender,
        'status':detail.status,
        'specialty': detail.specialty.id
    }
    return JsonResponse(data)

def doctor_create(request ):
    if request.method == 'POST':
        form =DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')        
        else:
            return render(request, 'categorias/doctor_.html', {'form': form})

def doctor_edit(request, pk):
    doctor = Doctor.objects.get(pk =pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance = doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
        else:
            return render(request, 'categorias/doctor_.html', {'form': form})
    data = {
        'id': doctor.id,
        'first_name': doctor.first_name,
        'last_name': doctor.last_name,
        'email': doctor.email,
        'document': doctor.document,
        'phone_number':doctor.phone_number,
        'license_number': doctor.license_number,
        'date_of_birth': doctor.date_of_birth,
        'years_of_experience': doctor.years_of_experience,
        'gender':doctor.gender,
        'specialty': doctor.specialty.id
    }
    return JsonResponse(data)

def doctor_delete(request, pk):
    Doctor.objects.get(pk=pk).delete()
    return redirect('doctor_list')

def changeStatusD(request, pk):
    if request.method == 'POST':
        doctor = Doctor.objects.get(pk=pk)
        doctor.status = not doctor.status
        doctor.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})