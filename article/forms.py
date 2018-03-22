from django import forms
class ArticleForm(forms.Form):
    title=forms.CharField(lable="标题", max_length=1000)
    content=forms.CharField(lable="内容", max_length=10000)