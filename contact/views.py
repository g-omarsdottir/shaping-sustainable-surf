from django.shortcuts import render

from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):

    contact_form = ContactForm()

    if request.method == "POST":

        form_data = {
            "name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
        }
        contact_form = ContactForm(form_data)

        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                    contact_form = ContactForm(initial={
                        "name": user_profile.user.get_full_name() or user_profile.user.username,
                        "email": user_profile.user.email,
                        "contact.phone": user_profile.default_phone_number,
                    })
                except UserProfile.DoesNotExist:
                    contact_form = ContactForm()
            else:
                contact_form = ContactForm()
        
            return redirect(reverse(
                "contact_success", args=[contact.email])
            )        
        else:
            messages.error(
                request,
                "There was an error with your form. "
                "Please double check your information.",
            )

    template = "contact/contact.html"

    context = {
        "contact_form": contact_form,
    }

    return render(request, template, context)


def contact_success(request, email, name):
    

    success_message = (
        f"Thank you for contacting us, {name}! "
        f"A confirmation email will be sent to {contact.email}."
    )
    messages.success(request, success_message)

    template = "contact/contact_success.html"
    
    context = {
        "name": request.user.get_full_name() or contact.name,
        "email": email,
    }

    return render(request, template, context)