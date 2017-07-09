from django import forms
from django.contrib.auth.models import User
from helper.models import Document, Order
from translator.models import Translator_C2E,Translator_E2C
import random

C2E_assignee_choice = []
for e in Translator_C2E.objects.all():
    C2E_assignee_choice.append((e.id,e.get_name()))

E2C_assignee_choice = []
for e in Translator_E2C.objects.all():
    E2C_assignee_choice.append((e.id,e.get_name()))

class AssignForm(forms.ModelForm):
    C2E_new_assignee = forms.ChoiceField(choices=C2E_assignee_choice)
    E2C_new_assignee = forms.ChoiceField(choices=C2E_assignee_choice)
    class Meta:
        model = Order
        fields = ['C2E_new_assignee','E2C_new_assignee']

class ApproveForm(forms.ModelForm):
    approval = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((False, 'DISAPPROVE'), (True, 'APRROVE')),
        widget=forms.RadioSelect,
        required=False
    )
    class Meta:
        model = Order
        fields = ['approval']

class ResetPasswordForm(forms.Form):
    password = forms.PasswordInput()




class TransSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm your password",
        required=True)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        
	def __init__(self, *args, **kwargs):
		
		super(TransSignUpForm, self).__init__(*args, **kwargs)
		self.field_order = ['username','password','confirm_password','first_name','last_name','email']
		self.order_fields(self.field_order)
		self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'},required = True)

    def clean(self):
    	super(TransSignUpForm, self).clean()
    	password = self.cleaned_data.get('password')
    	confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match']
            )
            self._errors['confirm_password'] = self.error_class(
                ['Passwords don\'t match']
            )

        return self.cleaned_data
