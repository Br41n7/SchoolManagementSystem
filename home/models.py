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
    hero_image=StreamField([
        ('image',
         ImageChooserBlock())
    ], blank=True,use_json_field=True)
    button_text=models.CharField(max_length=20,
                                            blank=True)
    button_link=models.URLField(blank=True)
    sections = StreamField([
        ('feature', blocks.StructBlock([
            ('icon', blocks.CharBlock(required=True, help_text="Bootstrap Icon class, e.g., bi-person")),
            ('title', blocks.CharBlock(required=True)),
            ('text', blocks.TextBlock(required=True)),
        ])),
        ('testimonial', blocks.StructBlock([
            ('quote', blocks.TextBlock()),
            ('author', blocks.CharBlock()),
        ])),
        ('image_gallery', ImageChooserBlock(required=False)),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('sections'),
        FieldPanel('hero_image'),
        FieldPanel('button_text'),
        FieldPanel('button_link'),
    ]


    # content = StreamField(
    #     [
    #         ("heading", CharBlock(classname="full title")),
    #         ("paragraph", TextBlock()),
    #         ("image", ImageChooserBlock()),
    #     ],
    #     use_json_field=True,
    #     blank=True,
    # )
    #
    # content_panels = Page.content_panels + [
    #     FieldPanel("intro"),
    #     FieldPanel("content"),
    # ]
    #



# class BlogIndexPage(Page):
#
#     intro = RichTextField(blank=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel("intro"),
#     ]
#
#     def get_context(self, request):
#         context = super().get_context(request)
#         context["posts"] = (
#             BlogPage.objects.live().descendant_of(self).order_by("-first_published_at")
#         )
#         return context
#
#
# class BlogPage(Page):
#     intro = RichTextField(blank=True)
#     body = StreamField(
#         [
#             ("heading", CharBlock()),
#             ("paragraph", TextBlock()),
#             ("image", ImageChooserBlock()),
#         ],
#         use_json_field=True,
#     )
#
#     content_panels = Page.content_panels + [
#         FieldPanel("intro"),
#         FieldPanel("body"),
#     ]
#
#
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
