from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.utils import (BadRequestError, filter_page_type,
                                  page_models_from_string)
from wagtail.core.models import Page


class PortfolioPagesAPIEndpoint(PagesAPIEndpoint):
    """
    Override stock wagtail pages api to handle private pages
    """
    def get_queryset(self):
        request = self.request

        # Allow pages to be filtered to a specific type
        try:
            models = page_models_from_string(request.GET.get('type', 'wagtailcore.Page'))
        except (LookupError, ValueError):
            raise BadRequestError("type doesn't exist")

        if not models:
            models = [Page]

        if len(models) == 1:
            queryset = models[0].objects.all()
        else:
            queryset = Page.objects.all()

            # Filter pages by specified models
            queryset = filter_page_type(queryset, models)

        if self.request.user.is_authenticated:
            # Get all live pages
            queryset = queryset.live()
        else:
            # Get live pages that are not in a private section
            queryset = queryset.public().live()

        # Filter by site
        queryset = queryset.descendant_of(request.site.root_page, inclusive=True)

        return queryset
