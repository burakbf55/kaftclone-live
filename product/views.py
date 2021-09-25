from page.views import STATUS
from product.models import Category, Product
from django.shortcuts import get_object_or_404, render

# Create your views here.

def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)

    # Nav:
    #context['categories'] = Category.objects.filter(
    #    status = STATUS
    #).order_by('title')
    context['items'] = Product.objects.filter(
        category=context['category'],
        status = STATUS,
        stock__gte =1,
    )
    return render(request, 'product/category_show.html', context)