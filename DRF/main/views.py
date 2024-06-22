from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Exchange, Bank
from .permission import AdminOrReadOnly, IsOwnerOrRadOnly
from .serializers import ExchangeSerializer


# для глобального исопльзования пермишенов пользуеемся  settings. Но объявленные permission_classes - используются в первыую чоередь


class ExchangePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'   # позовляет api делать запрос чреез url  на колво элемнетво на странице
    max_page_size = 10000  # влияет только на page_size_query_param


# вьюхи для проверки прав доступа
class ExchangeAPIList(generics.ListCreateAPIView):  # вьюха для вывода списка и доавблени get post
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # настрока пермишенов (конкретно этот - не авторизованны й может читать, авторизованный  добавлять)
    pagination_class = (ExchangePagination,)   # подлючаем свою пагинацию (болший приортетиет чем глобальное через settings)


class ExchangeAPIUpdate(generics.RetrieveUpdateAPIView):  # вьюха для обновления (put, patch)
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )  # означает что этот мтеод доступен только по токенам

class ExchangeAPIDestroy(generics.RetrieveDestroyAPIView):  # вьюха для удаления
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (AdminOrReadOnly,)  # только дя админа (при нем юзеру вообще ничгео нельзя)


# class ExchangeViewSet(viewsets.ModelViewSet):
#     # этот ModelViewSet ползволяет делать все. есть еще без долавления и прочее
#     # при необходимости можно залезть внутрь скопировава миксины котрые  делают этот вьюсет
#     # и затем удалив ненужны, чтобы отредактировать его под себя
#     queryset = Exchange.objects.all()
#     serializer_class = ExchangeSerializer
#
#     # если требуется выбор какого-то опеределнного кол-ва записей то надо переопределить
#     # метод get_queryset (в данном случае 3 первых элемента)
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#
#         if not pk:
#             return Exchange.objects.all()[:3]
#
#         return Exchange.objects.filter(pk=pk)   # тут обязательно долже быть списк, поэтому фильтр

# данный декораток используется для создания маршрту котрого нет в
# базовом наборе в methods -указываем методы используемые на маршруте,
# detail - если Тру(то одна запитсь) иначе - список
# т.е сейчас появится новый маршрут http://127.0.0.1:8000/api/v1/exchange/bank
# bank - берется из названия функции(метода)
# @action(methods=['get'], detail=False)   # это для вывода только списка
# def bank(self, request):
#     bank = Bank.objects.all()
#     return Response({'bank': [b.name for b in bank]})

# @action(methods=['get'], detail=True)   # это для вывода не только списка банков а и инфы по ним
# def bank(self, request, pk=None):
#     bank = Bank.objects.get(pk=pk)
#     return Response({'bank': bank.name})


# # три продвинутые вьюхи для работы напрямую с данаыми связанными ст аблицами (но они хоть и выполняют разные
# # разные действия , в них есть дубблирование кода. поэтому етсь более продвинутые viewset
#
# class ExchangeAPIList(generics.ListCreateAPIView):   # вьюха для вывода списка и доавблени get post
#     queryset = Exchange.objects.all()
#     serializer_class = ExchangeSerializer
#
# class ExchangeAPIUpdate(generics.UpdateAPIView): # вьюха для обновления (put, patch)
#     queryset = Exchange.objects.all()
#     serializer_class = ExchangeSerializer
#
# class ExchangeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # вьюха для всего сразу (в том числе иудаления)
#     queryset = Exchange.objects.all()
#     serializer_class = ExchangeSerializer


# class ExchangeAPIView(APIView):   # тренировка с базовым классом
#     def get(self, request):      # обработка запрос от пользователя
#         q = Exchange.objects.all()
#         return Response({'exchange': ExchangeSerializer(q, many=True).data})   # передаем уже сериализатор many=True если значений несоклько
#
#     def post(self, request):      # обработка запрос от пользователя
#         serializer = ExchangeSerializer(data=request.data)   # пердвариатнльо считываем данные и проверяем их на валидность
#         serializer.is_valid(raise_exception=True)
#
#
#         # new = Exchange.objects.create(    # перенсли добаление в сериализатор
#         #     currency_exchange=request.data['currency_exchange'],
#         #     date=request.data['data'],
#         #     bank_id=request.data['bank_id'],   # передается именно с тем полем к которому ключ привязан
#         #     currency_id=request.data['currency_id'],
#         #
#         # )
#
#         serializer.save() # сохранияем данные в таблицу
#
#         return Response({'exchange': serializer.data})   # serializer.data сслыается на новый созданный объект
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'метод PUT не разрешен'})
#         try:
#             instance =Exchange.objects.get(pk=pk)
#         except:
#             return Response({'error': 'объект не найден'})
#
#         serializer = ExchangeSerializer(data=request.data, instance=instance)  # пердвариатнльо считываем данные и проверяем их на валидность
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()  # сохранияем данные в таблицу
#
#         return Response({'exchange': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'метод DELETE не разрешен'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             instance = Exchange.objects.get(pk=pk).delete()
#             return Response({'message': 'Удалены данные с id ' + str(pk)}, status=status.HTTP_204_NO_CONTENT)
#         except Exchange.DoesNotExist:
#             return Response({'error': 'Объект не найден'}, status=status.HTTP_404_NOT_FOUND)
#
#
#


# class ExchangeAPIView(APIView):   # тренировка с базовым классом
#     def get(self, request):      # обработка запрос от пользователя
#         lst = Exchange.objects.all().values()  # т.к нужен не кверисет а список значений
#         return Response({'exchange': list(lst)})
#
#     def post(self, request):      # обработка запрос от пользователя
#         new = Exchange.objects.create(
#             currency_exchange=request.data['currency_exchange'],
#             data=request.data['data'],
#             bank_id=request.data['bank_id'],   # передается именно с тем полем к которому ключ привязан
#             currency_id=request.data['currency_id'],
#
#         )
#         return Response({'exchange': model_to_dict(new)})   # model_to_dict  - функция перевода модели в словарь
