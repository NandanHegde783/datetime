from django.http import HttpResponse
#from django.utils import timezone
from datetime import datetime, timedelta

def current_datetime(request):
    now = datetime.now()
    html = '<html><body>Current date and time: %s</body></html>'%now
    return HttpResponse(html)
def hours_ahead(request, offset):
    offset =int(offset)
    now = datetime.now()
    ltr = datetime.now() + timedelta(hours = offset)
    html = '<html><body> %s hrs later date and time: %s</body></html>'%(offset, ltr)
    return HttpResponse(html)