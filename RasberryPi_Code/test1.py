import requests
from datetime import datetime

def getTime(machineid):
    url = 'http://mail.vendy.store/0v2/Get_schedule'

    # Get current time and date
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(current_date)

    data = {
        'machine_id': machineid,
        'current_time': current_time,
        'date': current_date
    }

    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.text)
    schedule_data = response.json()
    return schedule_data
#schedule='machine1'
#print(getTime(schedule))


