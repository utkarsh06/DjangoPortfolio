from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea
from captcha.fields import CaptchaField


class ContactForm(forms.Form):

	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	email = forms.EmailField(label='Email')
	subject = forms.CharField(label='Subject')
	message = forms.CharField(label='Message', widget=forms.Textarea(attrs={"rows":10,"cols":20}),max_length = 500)
	captcha = CaptchaField()