from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class Create_User(UserCreationForm):
    firstname = forms.CharField(label='Firstname', widget=forms.TextInput)
    lastname = forms.CharField(label='Lastame', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    gender = forms.CharField(label='Gender', widget=forms.TextInput)
    city = forms.CharField(label='City', widget=forms.TextInput)
    state = forms.CharField(label='State', widget=forms.TextInput)
    date_born = forms.DateField(label='Date_born', widget=forms.DateInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['firstname', 'lastname', 'email', 'gender', 'city',
                  'state', 'date_born', 'password1', 'password2'  
        ]
    
class Create_User_Admin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'gender', 'city',
                  'state', 'date_born', 'password', 'admin'  
        ]

# campos editaveis de um usuario
class Edit_User_Admin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'admin',
                  'password', 'gender', 'city', 'state', 'date_born']

# verifica se o usuario esta ativo e gera uma hash para alterar a senha
class User_Password_Reset_Form(PasswordResetForm):
    def get_users(self, email):
        active_users = User._default_manager.filter(**{
            '%s__iexact' % User.get_email_field_name(): email,
        })
        return (u for u in active_users if u.has_usable_password())
