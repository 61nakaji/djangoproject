from django.shortcuts import render

#フォーム対応
from django.db.models import Q
from .forms import ProfileSearchFormSet
from .models import Profile

def recommend_view(request):
    return render(request, 'recommend/recommend_view.html', {})

#フォーム対応
def index(request):
    profile_list = Profile.objects.all()
    formset = ProfileSearchFormSet(request.POST or None)
    if request.method == 'POST':
        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        formset.is_valid()

        # Qオブジェクトを格納するリスト
        queries = []

        # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作っていく
        for form in formset:
            # Qオブジェクトの引数になる。
            # {gender: 1, height__gte: 170} → Q(gender=1, height__gte=170)
            q_kwargs = {}
            gender = form.cleaned_data.get('gender')
            if gender:
                q_kwargs['gender'] = gender

            yearly_income = form.cleaned_data.get('yearly_income')
            if yearly_income:
                q_kwargs['yearly_income__gte'] = yearly_income

            height = form.cleaned_data.get('height')
            if height:
                q_kwargs['height__gte'] = height

            weight = form.cleaned_data.get('weight')
            if weight:
                q_kwargs['weight__lte'] = weight

            # ここは、そのフォームに入力があった場合にのみ入る。
            # フォームが空なら、q_kwargsは空のままです。
            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            # filter(Q(...) | Q(...) | Q(...))を動的に行っている。
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            profile_list = profile_list.filter(base_query)

    context = {
        'profile_list': profile_list,
        'formset': formset,
    }
    return render(request, 'recommend/profile_list.html', context)
