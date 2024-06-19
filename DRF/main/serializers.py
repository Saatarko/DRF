import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):  # создаем сериализатор для данных точнос связанных с таблицей
    class Meta:
        model = Exchange  # модель которую берем за основу
        # fields = ('currency_exchange', 'date', 'bank', 'currency')  # поля для сериализации  при этом 'bank', 'currency' -используются как в можели (а не пополям, как в просто сериалзаторе)
        fields = '__all__'

#
# class ExchangeModel:
#     def __init__(self, currency_exchange, data):
#         self.currency_exchange = currency_exchange
#         self.data = data


# # функция кодирования данных модели в json формат
#
# def encode():
#     exchange = ExchangeModel(55.90,"2024-09-30")
#     exchange_sr = ExchangeSerializer(exchange)
#     print(exchange_sr.data, type(exchange_sr.data), sep='\n')
#     json = JSONRenderer().render(exchange_sr.data)
#     print(json)
#
# # функция декодирования данных модели в json формат
#
# def decode():
#     stream = io.BytesIO(b'{"currency_exchange":"55.90","data":"2024-09-30"}')
#     data = JSONParser().parse(stream)
#     serializer = ExchangeSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#
# class ExchangeSerializer(serializers.Serializer):  # создаем сериализатор (простой без базовой привязки к модели можетбытьвообще не привязан к можели
#     currency_exchange = serializers.DecimalField(max_digits=10, decimal_places=2)
#     date = serializers.DateField()
#     bank_id = serializers.IntegerField()   # в сериализаторе прописывать нужно конкретным образом к чему привязка поля
#     currency_id = serializers.IntegerField()
#
#     def create(self, validated_data):  # переопределине фукнции создания таблицы
#         return Exchange.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # переопределине фукнции обновления данных таблицы
#         instance.currency_exchange = validated_data.get('currency_exchange', instance.currency_exchange)
#         instance.date = validated_data.get('date', instance.date)
#         instance.bank_id = validated_data.get('bank_id', instance.bank_id)
#         instance.currency_id = validated_data.get('currency_id', instance.currency_id)
#         instance.save()
#         return instance
