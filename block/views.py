from django.shortcuts import render
from django.shortcuts import render_to_response
from block.models import Block

# Create your views here.
def block_list(request):
   #blocks=Block.objects.all().order_by("-id")
    blocks=Block.objects.filter(status=0).order_by("-id")
   #block_infos=[{"name": "运维专区","desc":"运维学习论坛区","manager":"admin"},{"name": "运维专区2","desc":"运维学习论坛区2","manager":"admin"},{"name": "运维专区3","desc":"运维学习论坛区3","manager":"admin"}]
    return render_to_response("block_list.html",{"blocks":blocks})
   #return render(request,"block_list.html",{"blocks":block_infos})

