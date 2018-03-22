from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from block.models import Block
from article.models import Article


# Create your views here.
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render_to_response("article_list.html", {"articles":articles_objs, "b":block})

def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    title = request.POST["title"].strip()
    content = request.POST["content"].strip()
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        if not title or not content:
            return render(request, "article_create.html",
                    {"b":block, "error":"标题和内容都不能为空", "title":title, "content":content})
        if len(title) > 1000 or len(content) > 10000:
            return render(request, "article_create.html",
                    {"b":block, "error":"标题和内容不能太长", "title":title, "content":content})
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" %block_id)