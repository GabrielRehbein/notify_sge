import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import response, status
from webhooks.models import Webhook
from services.callmebot import CallMeBot


class WebhookSaleView(APIView):

    def post(self, request):
        data = request.data

        Webhook.objects.create(
            event_type = data.get('event_type'),
            event = json.dumps(data, ensure_ascii=False)
        )

        call_me_bot = CallMeBot()
        message = (
            f"🎉 Venda Concluída com Sucesso! 🎉\n\n"
            f"Uma nova venda foi registrada no SGE! Confira os detalhes abaixo:\n"
            f"     📅 Data da Venda: {data.get('created_at', 'N/A')}\n"
            f"     💻 Produto Vendido: {data.get('product', 'N/A')}\n"
            f"     🔢 Quantidade: {data.get('quantity', 'N/A')} unidade(s)\n"
            f"     💰 Valor Total da Venda: R${data.get('total_price', 'N/A')}\n"
            f"     📈 Lucro Obtido: R${data.get('profit', 'N/A')}\n"
            f"     📝 Observação: {data.get('description', 'N/A')}"
        )
        call_me_bot.whatsapp_message(
            message
        )

        send_mail(
            subject='Nova Saída SGE',
            message='',
            from_email=f'SGE <{settings.EMAIL_HOST_USER}>',
            recipient_list=[settings.EMAIL_ADMIN_RECEIVER],
            html_message=render_to_string('outflow.html', data),
            fail_silently=False
        )

        return response.Response(
        data=data,
        status=status.HTTP_201_CREATED
        )

