from django.shortcuts import render
from .models import Nordic

# Create your views here.

def blog_home(request):
    fw_list = Nordic.objects.all().order_by('-pk')

    return render(request, 'fw_storage/blog_home.html',
            {
                'fw_list': fw_list,
            }
    )

def blog_post(request, pk):
    fw = Nordic.objects.get(pk=pk)

    return render(request, 'fw_storage/blog_post.html',
            {
                'fw': fw,
            }
    )
