from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment
# Create your views here.

def newsfeed(request):
    articles = Article.objects.all()
    return render(request,'article_list.html',{'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request,'article_detail.html',{'feed':article})

def article_new(request):
    if request.method == 'POST': # 게시를 눌렀을때만 실행됨
        new_article = Article.objects.create(
            author=request.POST.get('author'),
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )

        return redirect(f'/article/{ new_article.pk }')

    return render(request, 'articl_new.html')

def detail_article(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST': #new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )

        return redirect(f'/article/{ article.pk }')

    return render(request, 'article_detail.html', {'feed': article})

def new_article(request):
    if request.methond == 'POST' :
        new_article = Article.objects.create(
            author=request.POST.get('author'),
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )

        return redirect(f'/article/{ new_article.pk }')
    return render(request,'articl_new.html')


def remove_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        password = request.POST.get('password')

        if password == comment.password:
            comment.delete()
            return redirect(f'/article/{ comment.article.pk }')
        else:
            return redirect('/fail/')

    return render(request, 'article_remove.html', { 'show_message': comment.text })