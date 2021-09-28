import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'FaceRecognition',
    user= 'postgres',
    password = 'dragonforcE#1',
    port = '5432'
)

df = pd.read_sql('select * from attendance_info', conn)
# print(df)

def get_student_temp(name):
    df1 = df.loc[df['student_name'] == name]
    print(df1[['student_name', 'body_temp']])



if __name__ == '__main__':
    get_student_temp('Jayateerth')