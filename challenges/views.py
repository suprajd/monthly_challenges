from django.shortcuts import render
from django.http import HttpResponse, Http404,  HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is January",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is october",
    "november": "This is november",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    """for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    print(response_data)
    return HttpResponse(response_data)"""


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirecth_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirecth_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,  "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
        """ender_to_string("404.html")
        return HttpResponseNotFound(response_data)
    response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)
    try:
        challenge_text = monthly_challenges[month]
        #response_data = f"<h1>{challenge_text}</h1>"
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    #except:
        return HttpResponseNotFound("This month is not supported!")"""
