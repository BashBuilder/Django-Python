from django.shortcuts import redirect, render

from .form import ContactForm

# def index(request):
#     tours = Tour.objects.all()
#     context = {"tours": tours}
#     return render(request, "tours/index.html", context)


def home_view(request):
    return render(request, "form_app/home.html")


# contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("contact-success")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "form_app/contact.html", context)


# success view function
def contact_success_view(request):
    return render(request, "form_app/contact_success.html")
