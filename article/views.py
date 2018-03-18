from django.shortcuts import render

# Create your views here.
def artical_list(request, block_id):
    block_id = int(block_id)
    return render(request, "artical_list.html")

