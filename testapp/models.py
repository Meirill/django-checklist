from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

# from groups.models import  Group

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class CheckList(models.Model):
    #related_name replaces the something_set
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=False)
    title_html = models.CharField(max_length=255, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title_html = misaka.html(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("testapp:all")

    # def get_absolute_url(self):
    #     return reverse("testapp:all", kwargs={"username": self.user.username, "pk": self.pk})

        # return reverse("testapp:single",
        # kwargs={"username": self.user.username, "pk": self.pk})

class CheckListItem(models.Model):
    # check_list = ForeignKey(CheckList, related_name="???")
    check_list = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    ##########################
    title = models.CharField(max_length=255)
    title_html = models.CharField(max_length=255, editable=False)
    message = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title_html = misaka.html(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("testapp:all")

    # def get_absolute_url(self):
    #     return reverse("testapp:single",
    #     kwargs={"username": self.user.username, "pk": self.pk})



















# class CheckListSubItem(models.Model):
#     pass
