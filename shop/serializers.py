from rest_framework import serializers

from .models import PulsarProduct


class PulsarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulsarProduct
        fields = '__all__'

