from rest_framework import serializers
from wagtail.images.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'file', 'width', 'height', 'file_size']
