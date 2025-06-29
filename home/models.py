<<<<<<< HEAD
=======
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from wagtail.blocks import CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
>>>>>>> d8e5f0d (havoc)
from django.db import models

from wagtail.models import Page


class HomePage(Page):
<<<<<<< HEAD
    pass
=======
    intro = RichTextField(blank=True)
    content = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', TextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('content'),
    ]


class AboutPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['posts'] = BlogPage.objects.live().descendant_of(
            self).order_by('-first_published_at')
        return context


class BlogPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField([
        ('heading', CharBlock()),
        ('paragraph', TextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
>>>>>>> d8e5f0d (havoc)
