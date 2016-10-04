
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

