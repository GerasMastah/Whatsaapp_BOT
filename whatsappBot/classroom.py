from __future__ import print_function
import pickle
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tabulate import tabulate





# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly',
          'https://www.googleapis.com/auth/classroom.coursework.me',]

def main():
    tareas = []
    dues = []
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    
    results = service.courses().list(pageSize=6).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        #print('Tareas Pendientes')
        for course in courses:
            
            CurrentDate = datetime.datetime.now()
                
            #print('\n\n',course['name']+":")
            courseName = course['name']+":"
            dues.append(courseName)
##            print(courseName)
            courseWorkList = service.courses().courseWork().list(courseId=course['id']).execute()
            #print(courseWorkList)
            for courseWork in courseWorkList["courseWork"]:
                try:
                    year = courseWork["dueDate"]['year']
                    month = courseWork["dueDate"]['month']
                    day = courseWork["dueDate"]['day']
                    hour = courseWork["dueTime"]['hours']
                    date =  '  ', str(day),'/',str(month),'/',str(year)
                    date = " ".join(date)
                    dueDate = date.replace(" ","") +" "+ str(hour)+':00'
                    #print(dueDate,"bingo")
                    title = courseWork["title"]
                    ExpectedDate = datetime.datetime.strptime(dueDate, "%d/%m/%Y %H:%M")
                    #print(ExpectedDate,"test")
##                    print(courseWork)
                    if ExpectedDate < CurrentDate:
                        
                        dues = []
               
                    
                    else :
##                        print(title, date.replace(" ",""),courseWork["dueTime"]['hours'])
                        #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        tarea = title + '  ' + date.replace(" ","")+"           " 
                      
                        dues.append(tarea)
                    
                        tareas.append(dues)
                        dues = []
##                        print(tabulate(tareas))
               
                except KeyError:
                            status = False
                            #print('Can not find "something"')
                            
                    
    return(tabulate(tareas))

    
##if __name__ == '__main__':
##    print(main())
