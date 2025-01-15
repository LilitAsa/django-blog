from django.contrib import admin, messages
from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title", "slug","is_published", "category","brief_info")
    list_display_links = ["id", "title"]
    list_editable = ["is_published"]
    ordering = ["-pk"]
    actions = ["set_published", "set_draft"]
    search_fields = ["title__startswith", "content", "category__name"]
    search_help_text = "You can search only with title or content or category name"
    list_filter = ["title", "category__name"]

    @admin.display(description="Short info", ordering="content")
    def brief_info(self, article: Article):
        return f"Description {len(article.content)} symbols."

    @admin.action(description="Դարձնել published")
    def set_published(self,request,queryset):
        count = queryset.update(is_published=Article.Status.PUBLISHED)
        self.message_user(request,f"Published: {count}", messages.INFO)

    @admin.action(description="Դարձնել draft")
    def set_draft(self,request,queryset):
        count = queryset.update(is_published=Article.Status.DRAFT)
        self.message_user(request, f"Drafted: {count}", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug")
    list_display_links = ("id","name")
    ordering = ["-pk"]