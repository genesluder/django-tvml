
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


class TVMLRendererMixin(object):
    """
    Simple mixin that renders xml

    """

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context, content_type="text/xml; charset=utf-8")


class TVMLAlertView(TemplateView, TVMLRendererMixin):
    """
    Convenience alert view. 

    Example context that can be passed to populate the default template: 

        'title': 'An Alert', 
        'description': 'An Alert Description',
        'background_image': '/static/resources/images/background/bg_dark.jpg', 
        'buttons': [ 
            {
                'title': 'OK',
                'highlight': True,
            }, 
            {
                'title': 'CANCEL',
            },
            {
                'title': 'DISABLED',
                'disabled': True,
            },  
        ]

    """

    template_name = "tvml/alert.xml"


class TVMLListView(ListView, TVMLRendererMixin):
    """
    A generic Django list view that returns xml
    """
    pass


class TVMLDetailView(DetailView, TVMLRendererMixin):
    """
    A generic Django detail view that returns xml
    """
    pass
