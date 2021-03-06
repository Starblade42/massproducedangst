from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from dblog.models import Article
from dblog.models import Author
from dblog.models import Bio
from dblog.models import Blog
from dblog.models import FavoriteLink
from dblog.models import Update

def index(request):
	#The author we want to load on the Index
	author_ID = 'zarcos'
	#The blog we want to load on the Index
	blog_ID = 'MassProducedAngst'
	author = get_object_or_404(Author, authorID__exact=author_ID)
	blog = get_object_or_404(Blog, blogID__exact=blog_ID)
	article_list = Article.objects.order_by('title')
	return render(request, 'dblog/main.html', {'author': author, 'blog':blog, 'article_list': article_list})

def detail(request, author_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	blog_list = Blog.objects.order_by('title')
	link_list = FavoriteLink.objects.order_by('authorID')
	bio_list = Bio.objects.order_by('authorID')
	return render(request, 'dblog/detail.html', {'author': author, 'blog_list': blog_list, 'link_list': link_list, 'bio_list': bio_list}) 

def blog(request, author_ID, blog_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	blog = get_object_or_404(Blog, blogID__exact=blog_ID)
	article_list = Article.objects.order_by('title')
    	return render(request, 'dblog/blog.html', {'author': author, 'blog':blog, 'article_list': article_list})

def favorites(request, author_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	#favorites = get_object_or_404(FavoriteLink, authorID__exact=author_ID)
	favorites = FavoriteLink.objects.get(authorID=author.id)
    	return render(request, 'dblog/main.html', {'author': author, 'favorites':favorites})