from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest
from .forms import AdminSendForm
import telegram_send


class IndexView(View):
    """
    Отображение главной (и единственной) страницы.
    """

    def get(self, request: HttpRequest):
        if request.session.get('table_number_qr'):
            number = request.session.get('table_number_qr')
        else:
            number = None
        form = AdminSendForm()
        content = {'table_number': number,
                   'form': form}
        return render(request, 'main_project/main_page.html', content)


class GenerateView(View):
    """
    Генерация сессии в зависимости от ссылки
    """

    def get(self, request, pk):
        dict_address = {67868598762858: 1,
                        77497795: 2,
                        77488198676462: 3,
                        678634267680: 4,
                        79829578142542: 5,
                        76278529: 6,
                        76276327676429: 7,
                        76863426758658: "Круглый",
                        67285185676429: "Зеленый",
                        762726817548968077868596: "VIP малый",
                        66868587504967897642: "VIP большой"
                        }
        request.session['table_number_qr'] = dict_address[pk]
        return redirect('index')


class PrintHookah(View):
    """
    Отправка сообщения в Telegram
    """

    def get(self, request):
        mes = f"Кальянщик на стол {request.session.get('table_number_qr')}"
        telegram_send.send(messages=[mes])
        return redirect('index')


class PrintBarman(View):
    """
    Отправка сообщения в Telegram
    """

    def get(self, request):
        mes = f"Бармен на стол {request.session.get('table_number_qr')}"
        telegram_send.send(messages=[mes])
        return redirect('index')


class PrintNotDisturb(View):
    """
    Отправка сообщения в Telegram
    """

    def get(self, request):
        mes = f"Стол {request.session.get('table_number_qr')} просит не беспокоить"
        telegram_send.send(messages=[mes])
        return redirect('index')


class AdminSendView(View):
    """
    Отправка сообщения в Telegram
    """

    def post(self, request):
        form = AdminSendForm(request.POST)
        input_data_form = form.data.dict()
        data = {"table": request.session.get('table_number_qr'),
                "message": input_data_form['message']}
        mes = f"Сообщение администратору со стола {data['table']}: {data['message']}"
        telegram_send.send(messages=[mes])
        return redirect('index')
