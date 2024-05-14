from django.urls import re_path
from score_prediction.views import score_prediction_page,index,winner_prediction_page

urlpatterns = [
    re_path(r'^$',score_prediction_page, name='score_prediction'),
    re_path('score_prediction/',score_prediction_page, name='score_prediction'),

    # re_path(r'^$',index, name='index'),
    re_path('winner_prediction/',score_prediction_page, name='winner_prediction'),


    

]