# I have created this file - Mohib

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(render(request, 'index.html'))
def Analyze(request):
    #Get the text
    Text = request.POST.get('text', 'default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in Text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        Text = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in Text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        Text = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in Text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        Text = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(Text):
            if not (Text[index] == " " and Text[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
        Text = analyzed


    elif charcount == "on":
        count = 0
        for char in Text:
            if char != " ":
                count = count + 1
        params = {'purpose': 'Removed Extra space', 'analyzed_text': count}
        # Analyze the text
        return HttpResponse(render(request, 'analyze.html', params))

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please select any option and Try again")

    # Analyze the text
    return HttpResponse(render(request, 'analyze.html', params))
