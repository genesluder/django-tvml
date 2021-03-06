=============================
django-tvml
=============================

Includes an example Django project and Apple TV app. 


Usage
-----------------

views.py::

    from tvml.views import TVMLDetailView, TVMLListView
    from .models import Collection, Video


    class HomeView(TVMLListView):

        model = Collection
        template_name = 'example_app/home.xml'

        def get_context_data(self, **kwargs):
            context = super(HomeView, self).get_context_data(**kwargs)
            return context


    class VideoDetailView(TVMLDetailView):

        model = Video
        template_name = 'example_app/detail.xml'

        def get_context_data(self, **kwargs):
            context = super(VideoDetailView, self).get_context_data(**kwargs)
            context['title'] = self.object.title
            return context


urls.py::

    from django.conf.urls import url

    from tvml.views import TVMLAlertView

    urlpatterns = [

        url(r'^alert/$', TVMLAlertView.as_view(), {
            'title': 'An Alert', 
            'description': 'Florem ipsum crocus summer snowflake',
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
        }, name='alert'), 
    ]
