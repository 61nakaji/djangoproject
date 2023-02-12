from django.shortcuts import render

def recommend_view(request):
    return render(request, 'recommend/recommend_view.html', {})
