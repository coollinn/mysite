from django import forms

#简化下面的代码，直接从models中提取来生存校验器
"""
class ArticleForm(forms.Form):
    title=forms.CharField(label="标题", max_length=1000)
    content=forms.CharField(label="内容", max_length=10000)
"""

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
