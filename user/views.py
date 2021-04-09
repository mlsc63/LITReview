from django.shortcuts import render
from  .models import User
from .forms import UserForm
from django.http import HttpResponse
from django.template import loader

def connetion (request):
    message = "salut"
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = User.objects.filter(email=email)
        if not contact.exists():
            user = User.objects.create_user('usedsqdqsfdsqdsqrfdsf1', email, password)
            user.save()
            content = User.objects.all()
            content_formated = ["<li>{}</li>".format(contents.email) for contents in content]
            message = """<ul>{}</ul>""".format("\n".join(content_formated))
            return HttpResponse(message)

    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'connection.html', context)

