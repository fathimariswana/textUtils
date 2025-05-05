from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyse(request):
    if request.method=="GET":
        text = request.GET.get('enteredtext')
        chckbox_puct =request.GET.get('removepunc', "off")
        chckbox_capitalize = request.GET.get('makecapital', "off")
        chckbox_lower = request.GET.get('makelower', "off")
        punctuation_list = "!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        processedtext = ''
        selected_count  = sum([
                            chckbox_puct == 'on',
                            chckbox_capitalize == 'on',
                            chckbox_lower == 'on'
                        ])
        if selected_count != 1:
            return HttpResponse('Please select only one!!!!')
        else:
            if chckbox_puct == 'on':
                service="removing punctuation"
                for char in text:
                    if char not in punctuation_list:
                        processedtext = processedtext + char
            elif chckbox_capitalize == 'on':
                service = 'capitalized'
                processedtext = text.upper()
            elif chckbox_lower == 'on':
                service ='converted to lowercase'
                processedtext = text.lower()
            data={
                    'text':processedtext,
                    'service':service
                }
    return render(request, 'analyze.html', data)