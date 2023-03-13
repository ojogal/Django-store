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
  key_1 = forms.CharField(max_length=255, required=False, initial='Brand:', widget=forms.TextInput(attrs={'class': 'form-control border-0', 'readonly': True}))
  value_1 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_2 = forms.CharField(max_length=255, required=False, initial='Model number:', widget=forms.TextInput(attrs={'class': 'form-control border-0', 'readonly': True}))
  value_2 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_3 = forms.CharField(max_length=255, required=False, initial='Screen/display size:', widget=forms.TextInput(attrs={'class': 'form-control border-0', 'readonly': True}))
  value_3 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_4 = forms.CharField(max_length=255, required=False, initial='Memory:', widget=forms.TextInput(attrs={'class': 'form-control border-0', 'readonly': True}))
  value_4 = forms.CharField(max_length=255, required=False, empty_value='n/a')
  key_5 = forms.CharField(max_length=255, required=False, initial='Color:', widget=forms.TextInput(attrs={'class': 'form-control border-0', 'readonly': True}))
  value_5 = forms.CharField(max_length=255, required=False, empty_value='n/a')

  # pre-fill the existing values with the data if it exists
  def __init__(self, *args, **kwargs):
    initial = kwargs.get('initial', {})
    self.base_fields['value_1'].initial = initial.get('Brand:', '')
    self.base_fields['value_2'].initial = initial.get('Model number:', '')
    self.base_fields['value_3'].initial = initial.get('Screen/display size:', '')
    self.base_fields['value_4'].initial = initial.get('Memory:', '')
    self.base_fields['value_5'].initial = initial.get('Color:', '')
    super().__init__(*args, **kwargs)


class ImageForm(forms.ModelForm):
  image = forms.ImageField(
    label='Image',
    widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
  )  
  class Meta:
    model = Image
    fields = ('image',)