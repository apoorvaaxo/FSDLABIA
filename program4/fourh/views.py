from django.shortcuts import render
from datetime import datetime,timedelta
def display_times(request):
    now=datetime.now()
    four_hours_ahead=now+timedelta(hours=4)
    four_hours_before=now-timedelta(hours=4)
    context={
        'current_date_time':now,
        'four_hours_ahead' : four_hours_ahead,
        'four_hours_before':four_hours_before,
    }
    return render(request ,'display_times.html',context)
