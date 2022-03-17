from django.shortcuts import render
from .models import Nordic

# Create your views here.

def index(request):
    fw_list = Nordic.objects.all().order_by('-pk')

    return render(request,
            'fw_storage/index.html',
            {
                'fw_list': fw_list,
            }
    )

def detail_page(request, pk):
    fw = Nordic.objects.get(pk=pk)

    return render(request,
            'fw_storage/detail_page.html',
            {
                'fw': fw,
            }
    )
