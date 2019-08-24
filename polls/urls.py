from django.urls import path, include
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>', PollDetail.as_view(), name='polls_detail'),
    path('vote/', CreateVote.as_view(), name="create_vote"),
    path('choices/', ChoiceList.as_view(), name="choice_list")
]