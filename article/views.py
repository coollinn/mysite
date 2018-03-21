from django.shortcuts import render
from django.shortcuts import render_to_response
from block.models import Block
from article.models import Article


# Create your views here.
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render_to_response("article_list.html", {"articles":articles_objs, "b":block})

def article_create(request):
    #block_id = int(block_id)
    #block = Block.objects.get(id=block_id)
    #articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render(request, "article_create.html")
    #return render_to_response("article_create.html", {"articles":articles_objs, "b":block})
