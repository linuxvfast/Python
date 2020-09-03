from django.db import models


# Create your models here.
class UserType(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return self.caption


class UserGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType', to_field='id', on_delete=models.CASCADE)
    u2g = models.ManyToManyField(UserGroup)

    def __str__(self):
        return self.username


class Category(models.Model):
    caption = models.CharField(max_length=16)


class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # article_type = models.ForeignKey(ArticleType)

    type_choice = (
        (1, 'Python'),
        (2, 'OpenStack'),
        (3, 'Linux'),
    )
    article_type_id = models.IntegerField(choices=type_choice)
