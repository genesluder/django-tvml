
from django.conf.urls import url

from tvml.views import TVMLAlertView

from .views import HomeView, VideoDetailView


urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^videos/(?P<pk>[\w-]+)/$', VideoDetailView.as_view(), name='video-detail'),

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

