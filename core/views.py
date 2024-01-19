from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from product.models import Product,Color,Size

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = Product.objects.all()
        color_slug = self.kwargs.get('color_slug')
        size_slug = self.kwargs.get('size_slug')
        sort_option = self.request.GET.get('sort')

        if color_slug:
            color = get_object_or_404(Color, slug=color_slug)
            product = Product.objects.filter(color=color)

        if size_slug:
            size = get_object_or_404(Size, slug=size_slug)
            product = Product.objects.filter(size=size)

        if sort_option == 'price_Ascending':
            product = product.order_by('price')
        elif sort_option == 'price_Descending':
            product = product.order_by('-price')
        
        colors = Color.objects.all()
        sizes = Size.objects.all()
        # product = product.order_by('price')

        context['colors'] = colors
        context['sizes'] = sizes
        context['product'] = product
        context['sort_option'] = sort_option
        return context