from django.urls import path, include

from .views import cbv, fbv as views

app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
    path('<int:question_id>/', cbv.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', cbv.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', cbv.VoteView.as_view(), name='vote'),
]

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('cbv/', include(urlpatterns_cbv)),
]
