from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# quando qualcun cerca per esempio /polls/34
#django va in mysiteurls perchè è indicato nell'impostazione ROTT_URLCONF
#una volta che sorre la variabile urlpatterns e trova "polls/"
#viene rimandato a polls/urls.py e qui riscorre urlpatterns
# django ha tagliato 'polls/' e ha spedito la parte rimanente "34/"
#al polls.urls URLconf per futuri processi.
#'qui si abbina a '<int:question_id>/'risultando in una chiamata
#detail(request=<HttpRequest object>, question