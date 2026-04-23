from django import forms
from .models import Specialty, Doctor

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields =('name', 'description')
        labels = {
            'name':' Nombre',
            'description':'Descripción'
        }
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe un nombre'
                }
            ),
            'description': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe la descripción'
                }
            )
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'first_name','last_name', 'email',
            'document', 'phone_number', 'license_number',
            'date_of_birth', 'years_of_experience','gender', 'specialty'
            )
        labels = {
            'first_name':' Nombre',
            'last_name':'Apellido',
            'email':' Correo',
            'document':'Documento',
            'phone_number':' N.o de teléfono',
            'license_number':'No. Licencia',
            'date_of_birth':'Fecha de nacimiento',
            'years_of_experience':'Años de experiencia',
            'gender':' Genero',
            'specialty':' Especialidad',
        }
        widgets ={
            'first_name': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el nombre'
                }
            ),
            'last_name': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el apellido'
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el correo'
                }
            ),
            'document': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el No. de documento'
                }
            ),
            'phone_number': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el número de teléfono'
                }
            ),
            'license_number': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el número de la licencia'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD'
                }
            ),
            'years_of_experience': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe los años de experiencia'
                }
            ),
            'gender': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Escribe el genero'
                }
            ),
            'specialty': forms.Select(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'selecciona'
                }
            ),
        }