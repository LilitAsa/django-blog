from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from unicodedata import category

from blog.models import Article, Category, ArticleTags

data_from_db = [
	{
		"id": 1,
		"title": "CSTO should not have fought for Yerevan in Karabakh, Putin says",
		"is_published": True,
		"content": """
			The <span style = "color:red"> Collective </span> Security 
			
			Treaty Organization (CSTO) should not have fought for Yerevan in Karabakh; in this case,
			there was no external aggression against Armenia, Russian President Vladimir Putin said, TASS reports. Also,
			the Russian president did not rule out that Armenia will return to full-time work within the CSTO.
			He added that Armenia has not yet announced its withdrawal from the CSTO and supports all the
			documents of the summit of this organization.
		"""
	},
	{
		"id": 2,
		"title": "US dollar still rising in Armenia",
		"is_published": False,
		"content": """
			The American dollar’s (USD) exchange rate against the Armenian dram (AMD) comprised AMD 392.97/$1 in Armenia
			on Thursday;
		"""
	},
	{
		"id": 3,
		"title": "Ameriabank Named Armenia’s Best Bank for Real Estate by Euromoney",
		"is_published": True,
		"content": """
			Ameriabank has been recognized as Armenia’s best bank for real estate by an international financial publication
			Euromoney, becoming the first-ever recipient of this award in Armenia. The Real Estate Awards honor excellence in
			the commercial real estate sector, acknowledging not only financial success and client service, but also a
			commitment to improving the sector through technological advances and sustainability initiatives
		"""
	}
]

def index(request):
	# articles = Article.objects.filter(is_published=1)
	articles = Article.published.all()

	return render(request, "blog/index.html",{"articles": articles})


def about(request):
	return render(request, "blog/about.html", {"title": "About Page"})


def show_article(request, article_slug):
	article = get_object_or_404(Article, slug = article_slug)

	data = {
		"title": article.title,
		"content": article.content,
		"time_create": article.time_create,
		"time_update": article.time_update,
		"is_published": article.is_published,
		"tags": article.tags.all()
	}
	return render(request, "blog/show-article.html", data)


def show_category(request,cat_slug):
	category = get_object_or_404(Category, slug = cat_slug)
	articles = Article.published.filter(category_id=category.pk)
	data = {
		"name": category.name,
		"slug": category.slug,
		"id": category.id,
		"items": category.items.all(),
		"articles": articles,
		"cat_selected": category.id
	}

	return render(request,"blog/category.html", data)


def show_tags(request, tag_slug):
	tag = get_object_or_404(ArticleTags, slug=tag_slug)
	articles = tag.tags.filter(is_published=Article.Status.PUBLISHED)

	data = {
		"title": f"Tag: {tag.tag}",
		"articles": articles,
	}

	return render(request, "blog/show-tags.html", data)


def add_post(request):
	return render(request, "blog/add-post.html", {"title": "Add Post"})


def contacts(request):
	return render(request, "blog/contacts.html", {"title": "Contacts"})


def login(request):
	return render(request, "blog/login.html", {"title": "Login"})


def page_not_found(request, exception):
	return HttpResponseNotFound(f"<h1> Page Not Found 404 </h1>")
