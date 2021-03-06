from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.paginator import Paginator

from block.models import Block
from article.models import Article
from article.forms import ArticleForm


# Create your views here.
def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    ARTICLE_CNT_1PAGE = 3
    page_no = int (request.GET.get("page_no", "1"))
    #articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    all_articles = Article.objects.filter(block=block, status=0).order_by("-id")
    p = Paginator(all_articles, ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    articles_objs = page.object_list
    return render_to_response("article_list.html", {"articles":articles_objs, "b":block})

def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        """ 这段检查代码用校验器forms.py来替代
        title = request.POST["title"].strip()
        content = request.POST["content"].strip()
        if not title or not content:
            return render(request, "article_create.html",
                    {"b":block, "error":"标题和内容都不能为空", "title":title, "content":content})
        if len(title) > 1000 or len(content) > 10000:
            return render(request, "article_create.html",
                    {"b":block, "error":"标题和内容不能太长", "title":title, "content":content})
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" %block_id)
        """
        form=ArticleForm(request.POST)
        if form.is_valid():
            #article = Article(block=block, title=form.cleaned_data["title"], content=form.cleaned_data["content"], status=0) 可用下面3行替代，字段多的时候很明显优化
            article = form.save(commit=False)
            article.block = block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" %block_id)
        else:
            return render(request, "article_create.html", {"b":block, "form":form})


def article_detail(request, block_id, aid):
    aid = int(aid)
    #article = Article.objects.filter(id=aid)
    #return render ("article_detail.html", {"a":article})
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.get(id=aid)
    return render_to_response("article_detail.html", {"a":article_objs, "b":block})

