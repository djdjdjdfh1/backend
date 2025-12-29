from django.shortcuts import render, redirect
from django.conf import settings
import httpx
from .forms import ProductForm
from django.contrib import messages
# Create your views here.

FASTAPI_URL = settings.FASTAPI_BASE_URL

async def get_products():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{FASTAPI_URL}/api/products")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"Error fetching products: {e}")
            return []
    
async def product_list(request):
    products = await get_products()
    return render(request, "products/product_list.html", {"products": products})

async def product_create(request):
    if request.method == 'GET':
        form = ProductForm()
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_data = form.cleaned_data
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(f"{FASTAPI_URL}/api/products", json=product_data)
                    response.raise_for_status()
                    return render(request, "products/product_success.html", {"message": "Product created successfully!"})
                except httpx.HTTPError as e:
                    form.add_error(None, f"Error creating product: {e}")
