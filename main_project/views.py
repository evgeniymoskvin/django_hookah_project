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
        dict_address = {"Zmlyc3Q": 1,
                        "dHdv": 2,
                        "dGhyZWU": 3,
                        "Zm91cg": 4,
                        "Zml2ZQ": 5,
                        "c2l4": 6,
                        "c2V2ZW4": 7,
                        "cm91bmQ": "Круглый",
                        "Z3JlZW4": "Зеленый",
                        "c21hbGwgdmlw": "VIP малый",
                        "YmlnIHZpcA": "VIP большой"
                        }
        print(dict_address[pk])
        print(type(dict_address[pk]))
        request.session['table_number_qr'] = 1
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
