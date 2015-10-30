from django.shortcuts import render, redirect
from biostar4.forum import forms
from biostar4.forum.models import *
from biostar4.forum import utils
from biostar4.run import search


@fill_user
def search_view(request, user):
    query = request.GET.get('q')
    if not query:
        utils.error(request, "please enter a search query")
        redirect("home")

    result, hits = search.do_search(query)
    context = dict(
        user=user,
        result=result,
        hits=hits,
    )
    return render(request, "search.html", context=context)


def post_details(request, user, post):
    answers = Post.objects.filter(parent=post, ptype=Post.ANSWER).order_by('-vote_count',
                                                                           'creation_date')

    context = dict(
        user=user,
        post=post,
        answers=answers,
    )
    return render(request, "post_details.html", context=context)


@login_required
@fill_user
def post_new(request, user):
    if request.method == 'POST':
        form = forms.TopLevel(request.POST, request.FILES)
        # Save uploaded file.
        stream = request.FILES.get('upload')
        if form.is_valid():
            get = form.cleaned_data.get
            title, text, ptype = get('title'), get('text'), get('type')
            tag_val, status = get('tags'), get('status')
            post = Post(title=title, text=text, type=ptype, author=user,
                        lastedit_user=user,
                        status=status, tag_val=tag_val)
            post.save()
            return redirect("post_details", pid=post.id)
    else:
        form = forms.TopLevel()

    context = dict(
        user=user,
        form=form,
        form_title='Create a new post'
    )

    return render(request, "post_new.html", context=context)


@fill_user
def planet_list(request, user):
    context = dict(
        user=user,
    )
    return render(request, "planet_list.html", context=context)
