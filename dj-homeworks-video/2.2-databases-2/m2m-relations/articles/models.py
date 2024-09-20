from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Tag, through='ArticleTag', related_name='articles')

    def __str__(self):
        return self.title

    def sorted_tags(self):
        # Сортировка: сначала основной тег, потом остальные по алфавиту
        return self.article_tags.order_by('-is_main', 'tag__name')


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='article_tags')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.article} - {self.tag}"
