from django.contrib import admin
from dblog.models import Article
from dblog.models import Author
from dblog.models import Bio
from dblog.models import Blog
from dblog.models import FavoriteLink
from dblog.models import Update

admin.site.register(Author)

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Main Info',		{'fields':	['articleID', 'title', 'subtitle', 'authorID', 'blogID']}),
		('Content',			{'fields':	['articleType','body', 'sources']}),
		('Date',			{'fields':	['timestamp']})
	] 	

admin.site.register(Article, ArticleAdmin)
admin.site.register(Bio)
admin.site.register(Blog)
admin.site.register(FavoriteLink)
admin.site.register(Update)
