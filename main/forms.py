from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Image


class RegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta():
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
  characteristics = forms.CharField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Product
    fields = ['name', 'price', 'characteristics']


class CharacteristicsForm(forms.Form):
  key_1 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'ex. Brand:'}))
  value_1 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_2 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'ex. Model number:'}))
  value_2 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_3 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'ex. Screen/display size:'}))
  value_3 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_4 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'ex. Memory:'}))
  value_4 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_5 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'ex. Color:'}))
  value_5 = forms.CharField(max_length=255, required=False, empty_value='n/a')

  # pre-fill the existing values with the data if it exists
  def __init__(self, *args, **kwargs):
    initial = kwargs.get('initial', {})
    self.base_fields['value_1'].initial = initial.get('', '')
    self.base_fields['value_2'].initial = initial.get('', '')
    self.base_fields['value_3'].initial = initial.get('', '')
    self.base_fields['value_4'].initial = initial.get('', '')
    self.base_fields['value_5'].initial = initial.get('', '')
    super().__init__(*args, **kwargs)


class ImageForm(forms.ModelForm):
  image = forms.ImageField(
    label='Image',
    widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
  )  
  class Meta:
    model = Image
    fields = ('image',)