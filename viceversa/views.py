from django.shortcuts import render

def home(requst):
    return render(requst, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    res = len(user_text.split())
    return render(request, 'reverse.html', {'usertext':user_text,
                                            'reversedtext':reversed_text,
                                            'count_words':res})
