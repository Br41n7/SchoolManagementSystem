from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail import blocks
from wagtail.blocks import CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from django.db import models


class HomePage(Page):

    intro = RichTextField(blank=True)
    content = StreamField(
        [
            ("heading", CharBlock(classname="full title")),
            ("paragraph", TextBlock()),
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("content"),
    ]


class AboutPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class BlogIndexPage(Page):

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["posts"] = (
            BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")
        )
        return context


class BlogPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", TextBlock()),
            ("image", ImageChooserBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]


class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text='Bootstrap icon class or similar')

    def _str_(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    quote = models.TextField()

    def _str_(self):
        return f"{self.name} - {self.position}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')
    website = models.URLField(blank=True)

    def _str_(self):
        return self.name
