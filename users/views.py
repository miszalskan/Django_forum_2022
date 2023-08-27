from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import RegisterUserForm
from .token import account_activation_token


def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_profile.html', {'user': user})


def confirm(request):
    return render(request, 'confirmation.html')


def send_email(request):
    return render(request, 'send_email.html')


def logout_user(request):
    logout(request)
    messages.success(request,  "You were logged out..")
    return redirect('forum:index')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum:index')
        else:
            messages.success(request, "There was an error logging in, try again..")
            return redirect('users:login')
    else:
        return render(request, 'login.html')


def change_password(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')

            if new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                # return redirect(request, get_current_site(request))

            user.set_password(new_password)
            user.save()
            return redirect('login')
    else:
        messages.success(request, 'Invalid link.')
    return render(request, 'change_password.html')


def forget_password(request):
    try:
        if request.method == 'POST':
            to_email = request.POST.get('email')

            if not User.objects.filter(email=to_email).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('forget_password')
            user = User.objects.get(email=to_email)
            current_site = get_current_site(request)
            mail_subject = 'Reset link has been sent to your email id'
            message = render_to_string('active2.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('confirm')
    except Exception as e:
        print(e)
    return render(request, 'forget_password.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('active.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('confirm')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')
