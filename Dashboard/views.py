from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Attendance_info, StudentRecord
from django.http import JsonResponse
import json
from datetime import date, timedelta
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'FaceRecognition',
    user= 'postgres',
    password = 'dragonforcE#1',
    port = '5432'
)

### Connecting to database with pandas
df = pd.read_sql('select * from attendance_info', conn)

def get_student_values(request):
    return  render(request, 'temp_charts.html')



@login_required(login_url='/login')
def home_page(request):
    info = Attendance_info.objects.order_by('date').values()
    names_attend = Attendance_info.objects.values('student_name')
    return render(request, 'home.html', {'infos': info})


def todays_record(request):
    today_date = date.today().strftime("%d-%m-%Y")

    info = Attendance_info.objects.filter(date=today_date).order_by('student_id')
    return render(request, 'home.html', {'infos': info})





@login_required(login_url='/login')
def get_student_record(request):
    records = StudentRecord.objects.order_by('student_id').values()

    return render(request, 'record.html', {'records': records})


