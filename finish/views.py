from django.shortcuts import render, redirect
from .models import Duser
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from .crawling import danggn
from .crawling import hellomarket
from .crawling import sellit
from django.views.generic import TemplateView
from config import version


def form_test(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        search = request.POST["search"]
        dgimgurl, dgdata, dgtitle, dgcost = danggn(search)
        himgurl, hdata, htitle, hcost = hellomarket(search)
        simgurl, sdata, stitle, scost = sellit(search)

        return render(
            request,
            "index.html",
            context={
                "dgimgurl": dgimgurl,
                "dgdata": dgdata,
                "dgtitle": dgtitle,
                "dgcost": dgcost,
                "himgurl": himgurl,
                "hdata": hdata,
                "htitle": htitle,
                "hcost": hcost,
                "simgurl": simgurl,
                "sdata": sdata,
                "stitle": stitle,
                "scost": scost,
            },
        )


def lform_test(request):
    if request.method == "GET":
        return render(request, "logindex.html")
    elif request.method == "POST":
        search = request.POST["lsearch"]
        dgimgurl, dgdata, dgtitle, dgcost = danggn(search)
        himgurl, hdata, htitle, hcost = hellomarket(search)
        simgurl, sdata, stitle, scost = sellit(search)

        return render(
            request,
            "logindex.html",
            context={
                "dgimgurl": dgimgurl,
                "dgdata": dgdata,
                "dgtitle": dgtitle,
                "dgcost": dgcost,
                "himgurl": himgurl,
                "hdata": hdata,
                "htitle": htitle,
                "hcost": hcost,
                "simgurl": simgurl,
                "sdata": sdata,
                "stitle": stitle,
                "scost": scost,
            },
        )


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)
        useremail = request.POST.get("useremail", None)

        res_data = {}
        if not (username and password and re_password and useremail):
            res_data["error"] = "모든 값을 입력하시오."
        elif password != re_password:
            # return HttpResponse("비밀번호가 다름")
            res_data["error"] = "비밀번호가 다름"
        else:
            finish = Duser(
                username=username,
                password=make_password(password),
                useremail=useremail,
            )

            finish.save()

        return render(request, "register.html", res_data)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session["user"] = form.user_id

            return render(request, "logindex.html", {"form": form})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout(request):
    if request.session["user"]:
        del request.session["user"]

    return redirect("/")


class ServiceWorkerView(TemplateView):
    template_name = "service-worker.js"
    content_type = "application/javascript"
    name = "service-worker.js"

    def get_context_data(self, **kwargs):
        return {
            "version": version,
        }

