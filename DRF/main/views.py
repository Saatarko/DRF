from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Exchange
from .serializers import ExchangeSerializer


# Create your views here.
# class ExchangeAPIView(generics.ListAPIView):
#     queryset = Exchange.objects.all()
#     serializer_class = ExchangeSerializer


class ExchangeAPIList(generics.ListCreateAPIView):   # вьюха для вывода списка и доавблени get post
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class ExchangeAPIUpdate(generics.UpdateAPIView): # вьюха для обновления (put, patch)
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class ExchangeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # вьюха для всего сразу (в том числе иудаления)
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

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