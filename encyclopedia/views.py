from django.shortcuts import render, redirect
from . import util
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import dataform
import random

# wiki home index
def index(request):
    # render index with list entries
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# entrie page
def article_page(request, name):
    if name in util.list_entries():
        # render target article based on name string in url
        return render(request, "encyclopedia/article.html", {
            "name": name,
            "markdown": util.convert_tohtml(util.get_entry(name))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": 'requested page was not found.'
        })
    
# wiki layout search field
def search_form(request):
    search_result = request.GET['q']
    print(search_result)
    entries = util.list_entries()
    if search_result in util.list_entries():
        # render with redirect for exact match search field
        return render(request, "encyclopedia/article.html", {
            "name": search_result,
            "markdown": util.convert_tohtml(util.get_entry(search_result))
        })
    # loop inside entries list and search for any match char
    elif any(search_result.lower() in entry.lower() for entry in entries):
                # return list entries of loop result
                results = [entry for entry in entries if search_result.lower() in entry.lower()]
                return render(request, "encyclopedia/search_results.html", {
                    "query": search_result,
                    "results": results
                }) 
    else:
        # render error message if not matching char
        return render(request, "encyclopedia/error.html", {
            "error": 'Searched item not found'
        })


# Create new Page
def add_new_page(request):
    if request.method == "POST":
        form = dataform.new_page_form(request.POST)
        # validate form
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['article_name']
            content = form.cleaned_data['article_text']
            if name.lower() in (i.lower() for i in util.list_entries()):
                 return render(request, 'encyclopedia/error.html', {
                    "error": 'Article already exist'
                })
            else:
                # save new entry 
                util.save_entry(name, content)
                return render(request, "encyclopedia/article.html", {
                    "name": name,
                    "markdown": util.convert_tohtml(util.get_entry(name))
                })
        else:
            # if form is not valid
            return render(request, "encyclopedia/newpage.html", {
                "article_name" : form.cleaned_data['article_name'],
                "article_text" : form.cleaned_data['article_text']
            })
    else:
        # render form if != POST
        form = dataform.new_page_form()
        return render(request, "encyclopedia/newpage.html", {
            "article_name" : form['article_name'],
            "article_text" : form['article_text']

        })

def edit_page(request, name):
    if request.method == "POST":
        form = dataform.edit_page(request.POST)
        # validate form
        if form.is_valid():
            new_text = form.cleaned_data['article_text']
            # save text changes
            util.save_entry(name, new_text)
            return render(request, "encyclopedia/article.html", {
                "name": name,
                "markdown": util.convert_tohtml(util.get_entry(name))
            })
        else:
            return render(request, "encyclopedia/editpage.html", {
                "form": form
            }) 
    else:
        current_data = util.get_entry(name)
        form = dataform.edit_page({
            'article_name': name,
            'article_text': current_data
        })
        return render(request, "encyclopedia/editpage.html", {
            "name": name,
            "article_text": form['article_text']
        })


def random_page(request):
    entries = util.list_entries()  
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/article.html", {
        "name": random_entry,
        "markdown": util.convert_tohtml(util.get_entry(random_entry))
    })