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
    def get(self, request, pk):
        request.session['table_number_qr'] = pk
        return redirect('index')


class PrintHookah(View):
    def get(self, request):
        mes = f"Кальянщик на стол {request.session.get('table_number_qr')}"
        telegram_send.send(messages=[mes])
        return redirect('index')


class PrintBarman(View):
    def get(self, request):
        mes = f"Бармен на стол {request.session.get('table_number_qr')}"
        telegram_send.send(messages=[mes])
        return redirect('index')


class AdminSendView(View):
    def post(self, request):
        form = AdminSendForm(request.POST)
        input_data_form = form.data.dict()
        data = {"table": request.session.get('table_number_qr'),
                "message": input_data_form['message']}
        mes = f"Сообщение администратору со стола {data['table']}: {data['message']}"
        telegram_send.send(messages=[mes])
        return redirect('index')
