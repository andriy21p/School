from django.shortcuts import render
from items.models import Items


# Create your views here.
def index(request):
    return render(request, 'items/index.html', {
        'items': Items.objects.all(),
    })
