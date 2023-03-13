from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProductForm, ImageForm, CharacteristicsForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product, Image
from django.contrib import messages


def index(request):
  products = Product.objects.all()
  images = Image.objects.all()
  return render(request, 'main/home.html', {'products': products, 'images': images})

@login_required(login_url='/login')
def show(request, pk):
  product = get_object_or_404(Product, pk=pk)
  images = Image.objects.all()
  return render(request, 'main/show.html', {'product': product, 'images': images})

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        char_form = CharacteristicsForm(request.POST)
        files = request.FILES.getlist('image')
        if form.is_valid() and char_form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.set_characteristics(char_form.cleaned_data)
            product.save()
            for image in files:
                Image.objects.create(product=product, image=image)
            messages.success(request, 'Product created successfully!')
            return redirect('create')
        else:
            print(form.errors)
            print(char_form.errors)
            return redirect('create')
    else:
        form = ProductForm()
        char_form = CharacteristicsForm()
    return render(request, 'main/create.html', {"form": form, "imageform": ImageForm(), "char_form": char_form})

@login_required(login_url='/login')
def update(request, pk):
  product = get_object_or_404(Product, id=pk, user=request.user)
  if request.method == 'POST':
    product_form = ProductForm(request.POST, instance=product)
    characteristics_form = CharacteristicsForm(request.POST)
    files = request.FILES.getlist('image')
    delete_images = request.POST.getlist('delete_image')
    if product_form.is_valid() and characteristics_form.is_valid():
      product = product_form.save(commit=False)
      characteristics_data = {
        characteristics_form.cleaned_data['key_1']: characteristics_form.cleaned_data['value_1'],
        characteristics_form.cleaned_data['key_2']: characteristics_form.cleaned_data['value_2'],
        characteristics_form.cleaned_data['key_3']: characteristics_form.cleaned_data['value_3'],
        characteristics_form.cleaned_data['key_4']: characteristics_form.cleaned_data['value_4'],
        characteristics_form.cleaned_data['key_5']: characteristics_form.cleaned_data['value_5'],
      }
      if characteristics_data:
        product.set_characteristics(characteristics_form.cleaned_data)
        product.save()
      else:
        product.characteristics = None
        product.save()
      for image in files:
          Image.objects.create(product=product, image=image)
      for image_id in delete_images:
          Image.objects.filter(id=image_id).delete()
      return redirect('home')
    else:
      print(product_form.errors)
      print(characteristics_form.errors)
      return redirect('home')
  else:
    product_form = ProductForm(instance=product)
    characteristics_data = product.get_characteristics()
    characteristics_form = CharacteristicsForm(initial=characteristics_data)
    # Filter images related to the product
    image_form = ImageForm(instance=product)
  return render(request, 'main/update.html', {
    'product_form': product_form,
    'characteristics_form': characteristics_form,
    'image_form': image_form,
    'product': product,
  })


@login_required(login_url='/login')
def delete(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if request.method == 'POST':
    product.delete()
    return redirect('home')
  return render(request, 'main/show.html', {'product': product})

def signup(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/home')
  else:
    form = RegisterForm()
  return render(request, 'registration/signup.html', {'form': form})