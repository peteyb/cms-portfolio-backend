import requests
from django.conf import settings
from django.dispatch import receiver
from wagtail.core.signals import page_published


@receiver(page_published)
def trigger_jamstack_build(sender, **kwargs):
    """
    Trigger build in netlify when any model published
    """
    requests.post(settings.BUILD_HOOK_URL, data={}, headers={}, verify=False)
