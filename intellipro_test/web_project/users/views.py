"""
Views of web project

functions:
    home: Render the home page.
    register: Register new user.
    crud: create new label and display all labels for the user
    update_label: change(rename) the label
    delete_label: delete the label

"""
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .form import LabelForm
from .models import Label
# Create your views here.


def home(request):
    """
    Render the home page.
    """
    return render(request, "users/home.html")


def register(request):
    """
    Register new user.
    """
    if request.method == "GET":
        return render(request, "users/register.html", {"form": UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))


def crud(request):
    """
    Create new labels and view all labels for the user.
    """
    # create a new label item for thr user
    if request.method == 'POST':
        label_name = request.POST.get("new-label")
        label = Label.objects.create(title=label_name, user=request.user)

        return redirect("crud")

    # view all label items that the user has
    labels = Label.objects.filter(user=request.user)
    context = {"labels": labels}

    return render(request, "users/crud.html", context)


def update_label(request, pk):
    """
    Update label item
    param:
        pk (Integer): Label ID - primary key
    """
    # returns the object if exists, status 404 not found otherwise
    label = get_object_or_404(Label, user=request.user, id=pk,)

    label.title = request.POST.get(f"label_{pk}")
    label.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_label(request, pk):
    """
    Delete label item
    param:
        pk (Integer): Label ID - Primary key
    """
    label = get_object_or_404(Label, id=pk, user=request.user)
    label.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

