from django.db import models
from grapple.models import GraphQLStreamfield, GraphQLString
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         StreamFieldPanel)
from wagtail.api import APIField
from wagtail.api.v2.serializers import StreamField as StreamFieldSerializer
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtailcloudinary.blocks import CloudinaryImageBlock
from wagtailcloudinary.fields import CloudinaryField, CloudinaryWidget

from .serializers import ImageSerializer


class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return ImageSerializer(context=context).to_representation(value)


class SecureStreamField(StreamFieldSerializer):
    """
    Used to restrict private fields from being rendered via API
    """
    def to_representation(self, value):
        if self.context['request'].user.is_authenticated:
            return super().to_representation(value)
        return ''


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    """
    A model to extend wagtail page for a BlogPost object
    """
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    extra = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', CloudinaryImageBlock()),
    ], null=True)

    graphql_fields = [
        GraphQLString("date"),
        GraphQLString("body"),
        GraphQLStreamfield("extra"),
    ]

    api_fields = [
        APIField('body'),
        APIField('extra'),
        APIField('restricted'),
        APIField('extra', serializer=SecureStreamField()),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
        StreamFieldPanel('extra'),
    ]

    @property
    def restricted(self):
        return [r.restriction_type for r in self.get_view_restrictions()]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
