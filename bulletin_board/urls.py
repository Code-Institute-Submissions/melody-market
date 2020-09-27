from django.urls import path
from bulletin_board.views import *
 
urlpatterns = [
    path('',show_ad,name='show_ad'),
    path('addMessage/',addMessage,name='addMessage'),
]