from django.db import models



class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Category(models.Model):
    languages = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='categories')
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class News(models.Model):
    categories = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, related_name='news')
    languages = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='news')
    title = models.CharField(max_length=100)
    header_title = models.CharField(max_length=300)
    text = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Image(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.DO_NOTHING, related_name='images')
    url = models.URLField("ссылка на картинку")
    order_num = models.IntegerField("порядковый номер картинки")
    active = models.BooleanField(default=True)
