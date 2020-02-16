from django import forms


from .models import MyUser

class RegistrationFrom(forms.ModelForm):
    """ form for registrations """

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'c-form'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'c-form'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'c-form'}))
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    """ login form """
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'c-form'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'c-form'}))


