from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User,Reports,Treatment,Doctor,Patient
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['email',]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email']

class LoginUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password'] 

class RegisterUserForm(forms.ModelForm):
    # password1 = forms.CharField(widget=forms.PasswordInput(),validators=[validate_password]) #uncomment when using password validation
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password1','password2']

class Forgot_email_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class Forgot_Password_Form(forms.ModelForm):
    # password1 = forms.CharField(widget=forms.PasswordInput(),validators=[validate_password]) # to use django validation
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['password1','password2']
        

class FileForm(forms.ModelForm):
    class Meta:
        model= Reports
        fields= ["name", "filepath","Description"]
    
    def save(self,user):
        data = self.cleaned_data
        report = Reports(name=data['name'], filepath=data['filepath'],
            Description=data['Description'], Patient=user.Patient)
        report.save()

class send_to_doc_Form(forms.ModelForm):
    class Meta:
        model= Reports
        fields = ["Doctors"]
    
    def __init__ (self,Patient, *args, **kwargs):
        super(send_to_doc_Form, self).__init__(*args, **kwargs)
        self.fields["Doctors"].widget = forms.widgets.CheckboxSelectMultiple()
        choices = []
        # choices = [(d.Doctor.id,d.Doctor.Name) for d in Patient.Treatments.all()]
        for treat in Patient.Treatments.all():
            if treat.is_active:
                choices.append((treat.Doctor.id,treat.Doctor.Name))
        self.fields["Doctors"].choices = choices

        

# class Treatment_Form(forms.ModelForm):
#     class Meta:
#         model= Treatment
#         fields = ["Doctor","Disease"]
    

class Register_Doc(forms.ModelForm):
    class Meta:
        model=Doctor
        exclude = ['user']


class Register_Patient(forms.ModelForm):
    class Meta:
        model=Patient
        exclude = ['user']

class Prescription(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['Prescription']