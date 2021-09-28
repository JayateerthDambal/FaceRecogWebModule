from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='Home'),
    path('student_record', views.get_student_record, name='Record'),
    path('todays_record', views.todays_record, name='TodaysRecord'),
    path('body_temp_trends', views.get_student_values, name='TempTrends'),

]