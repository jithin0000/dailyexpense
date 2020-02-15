from django import forms


from .models import MyUser

class RegistrationFrom(forms.ModelForm):
    """ form for registrations """

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user
