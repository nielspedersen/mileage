from django.conf.urls import url, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='placeholder/milage-index.html')),
    url(r'^$', index, name='milage-index'),
    url(r'^cars/$', cars_overview, name='cars'),
    url(r'^cars/edit/([0-9]+)/$', car_edit, name='car-edit'),
    url(r'^cars/delete/([0-å]+)/$', car_delete, name='car-delete'),
    url(r'^history/$', history, name='history'),
    url(r' history/$', history, name='history-car'),
    url(r'^overview/$', overview, name='overview'),
    url(r'^overview/$', overview, name='overview-car'),
    url(r'upload/$', upload_csv, name='upload'),
    url(r'^delete/([0-9]+)/$', delete, name='delete'),
    url(r'^change-car/([0-å]+)/$', change_car, name='change-car'),
    url(r'^edit/([0-9]+)/$', edit, name='edit'),
    url(r'^history/clear$', clear_history, name='clear_history')
]