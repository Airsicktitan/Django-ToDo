from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import toDoList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class EditToDo(forms.ModelForm):
	todo_title = forms.CharField(max_length=100, required= True, widget=forms.TextInput(attrs={
		'class': 'form-control', 'placeholder':'Title'
	}))
	todo_description = forms.CharField(max_length=250, required= True, widget=forms.Textarea(attrs={
		'class': 'form-control', 'placeholder':'Description'
	}))
	todo_is_completed = forms.BooleanField(required= False, widget=forms.CheckboxInput())

	class Meta:
			model = toDoList
			fields = ("todo_title", "todo_description", "todo_is_completed", "todo_created_by") #"todo_created_on", "todo_modified_on"

	def __init__(self, *args, **kwargs):
		super(EditToDo, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'submit_button'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'add_todo'

		self.helper.add_input(Submit('submit', 'Submit'))