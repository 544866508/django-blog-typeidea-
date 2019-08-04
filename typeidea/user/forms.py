from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, widget=forms.TextInput(attrs={'onblur': 'loginform_ajax()'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'onblur': 'loginform_ajax()'}))
    email = forms.EmailField(label='电子邮件', widget=forms.EmailInput(attrs={'onblur': 'loginform_ajax()'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, widget=forms.TextInput(attrs={'onblur': 'loginform_ajax()'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'onblur': 'loginform_ajax()'}))