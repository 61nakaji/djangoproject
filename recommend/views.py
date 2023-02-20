from django.shortcuts import render

# フォーム対応
from django.db.models import Q
from .forms import ProfileSearchFormSet
from .models import Profile

# ログイン対応
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm


def recommend_view(request):
    return render(request, 'recommend/recommend_view.html', {})

# フォーム対応


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

            q_kwargs = {}
            name = form.cleaned_data.get('name')
            if name:
                q_kwargs['name__contains'] = name

            album = form.cleaned_data.get('album')
            if album:
                q_kwargs['album__contains'] = album

            artist = form.cleaned_data.get('artist')
            if artist:
                q_kwargs['artist__contains'] = artist

            length = form.cleaned_data.get('length')
            if length:
                q_kwargs['length__lte'] = length

            # Qオブジェクトの引数になる。
            gender = form.cleaned_data.get('gender')
            if gender:
                q_kwargs['gender'] = gender

            popularity = form.cleaned_data.get('popularity')
            if popularity:
                q_kwargs['popularity__gte'] = popularity

            danceability = form.cleaned_data.get('danceability')
            if danceability:
                q_kwargs['danceability__gte'] = danceability

            acousticness = form.cleaned_data.get('acousticness')
            if acousticness:
                q_kwargs['acousticness__gte'] = acousticness

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


# ログイン処理
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'recommend/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'recommend/login.html'
