from django import forms


class RegisterForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control", "id": "username", "aria-describedby": "emailHelp", "name": "username"
			}))

	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"type": "password", "class": "form-control", "id": "password1", "name": "password1"
			}))

	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"type": "password", "class": "form-control", "id": "password2", "name": "password2"
			}))

	code = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control", "id": "xcode", "name": "code"
			}))


class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control", "id": "username", "aria-describedby": "emailHelp", "name": "username"
			}))

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control", "id": "password", "name": "username"
			}))


class TelegramAuth(forms.Form):
	id_ = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control", "id": "id", "aria-describedby": "emailHelp", "name": "id"
			}))
	code = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control", "id": "code", "aria-describedby": "emailHelp", "name": "code"
			}
		)
	)
