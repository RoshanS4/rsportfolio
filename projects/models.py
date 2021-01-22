from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape('img/')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True