from rest_framework import serializers
from russian_fields import INN, KPP, OGRN


class INNBusinessField(serializers.CharField):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        if isinstance(data, INN) or None:
            return data
        return INN(data)


class OGRNField(serializers.CharField):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        if isinstance(data, OGRN) or None:
            return data
        return OGRN(data)


class KPPField(serializers.CharField):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        if isinstance(data, KPP) or None:
            return data
        return KPP(data)
