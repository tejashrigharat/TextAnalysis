# creator: Tejashri

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

# Perform text analysis operations
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc =  request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcapitalize','off')
    newline = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    analyzed = ''
    # Remove the listed 14 punctuations
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed+i
        params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
    # Capitalize the entire text
    if fullcaps == 'on':
        if analyzed == '':
            analyzed = djtext.upper()
        else:
            analyzed = analyzed.upper()
        params = {'purpose': 'Convert to upper case', 'analyzed_text': analyzed}
    # Remove all the newlines from the text
    if newline == 'on':
        if analyzed == '':
            for i in djtext:
                if i != "\n" and i != '\r':
                    analyzed += i
        else:
            p = ''
            for i in analyzed:
                if i != "\n" and i != '\r':
                    p += i
            analyzed = p
        params = {'purpose': 'Remove the new line', 'analyzed_text': analyzed}
    # Remove all the spaces from the text
    if spaceremove == 'on':
        if analyzed == '':
            for i in djtext:
                if i != ' ':
                    analyzed += i
        else:
            p = ''
            for i in analyzed:
                if i != ' ':
                    p += i
            analyzed = p
        params = {'purpose': 'Remove Space', 'analyzed_text': analyzed}
    # Count all the characters in the entered text
    if charcount == 'on':
        count = len(djtext)
        analyzed += str(count)
        params = {'purpose': 'Count the characters', 'analyzed_text': analyzed}

    if removepunc == 'on' or fullcaps == 'on' or newline == 'on' or spaceremove == 'on' or charcount == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Please select the analysis for text entered!!!')
