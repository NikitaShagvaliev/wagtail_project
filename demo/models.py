# home/models.py
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class MyCustomPage(Page):
    # Поля для вашей страницы
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # Панель редактирования в административной панели
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]