from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.generic import TemplateView 



class Home(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        # Obtenha os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        destinatario = 'jotaven.moura@gmail.com'
        corpo_email = f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}'

        send_mail('Nova mensagem!', corpo_email, 'noreply@jotinha.com', [destinatario])
        return render(request, self.template_name, {'sucesso': True})

        
