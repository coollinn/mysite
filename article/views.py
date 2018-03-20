from django.shortcuts import render
from block.models import Block
from article.models import Article

# Create your views here.
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_jobs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render(request, "article_list.html", {"article": article_jobs, "b": block})

