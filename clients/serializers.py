from django.core.validators import RegexValidator
from rest_framework import serializers

from . import fields as f
from .models import City, Client
from .russian_fields_fixed import (FixedINNBusinessField, FixedKPPField,
                                   FixedOGRNField)


class ClientSerializer(serializers.ModelSerializer):
    serializer_field_mapping = (
        serializers.ModelSerializer.serializer_field_mapping.copy()
    )
    serializer_field_mapping[FixedINNBusinessField] = f.INNBusinessField
    serializer_field_mapping[FixedKPPField] = f.KPPField
    serializer_field_mapping[FixedOGRNField] = f.OGRNField

    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    email = serializers.EmailField()
    phone_number = serializers.CharField(
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=(
                'Phone number must be entered in the format:'
                ' \'+999999999\'. Up to 15 digits allowed.'
            )
        )]
    )
    site_url = serializers.URLField()

    class Meta:
        model = Client
        fields = (
            'id', 'city', 'company_name', 'address', 'inn', 'kpp', 'ogrn',
            'email', 'phone_number', 'site_url',
        )
