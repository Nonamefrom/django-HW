from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        # Считаем количество основных тегов
        main_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))

        # Проверяем, что ровно один основной тег
        if main_count == 0:
            raise ValidationError("Укажите основной раздел.")
        if main_count > 1:
            raise ValidationError("Основным может быть только один раздел.")

        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag  # Связующая модель
    extra = 1  # Количество пустых строк для добавления
    formset = ArticleTagInlineFormset  # Указываем наш кастомный formset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]  # Добавляем inline редактор для тегов

    fieldsets = (
        (None, {
            'fields': ('title', 'published_at'),
        }),
        ('Content', {
            'fields': ('text', 'image'),
            'classes': ['collapse'],
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['article', 'tag', 'is_main']
