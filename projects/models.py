from django.db import models
from datetime import datetime, timedelta
from profiles.models import UserProfile
from ckeditor.fields import RichTextField


def one_month_from_today():
    return datetime.now() + timedelta(days=30)


class Category(models.Model):
    """
    Content Project
    """
    class Meta:
        verbose_name_plural = "Categories"
    category = models.CharField(max_length=11)

    def __str__(self):
        return self.category


class Project(models.Model):
    """
    Content Project
    """

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET("deleted_user"), null=True, blank=True, related_name='projects')
    title = models.CharField(max_length=90, blank=False, null=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    category = models.ForeignKey('Category', blank=False, null=True, on_delete=models.SET_NULL)
    description = RichTextField(blank=False, null=False)
    backers_story_option1 = RichTextField(null=False, blank=False)
    backers_story_option2 = RichTextField(null=False, blank=False)
    backers_story_option3 = RichTextField(null=False, blank=False)
    created_date = models.DateField(default=datetime.now, editable=False)  # datetime instead of timezone else trouble with calculation of num_days
    views = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    end_date = models.DateField(default=one_month_from_today)
    num_days = models.IntegerField(default=0)
    raised = models.IntegerField(default=0)
    conditions = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.title
