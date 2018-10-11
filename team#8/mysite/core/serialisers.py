from .models import Profile, bmm
from rest_framework import *

class profile_dataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class bmm_dataSerialiser(serializers.ModelSerializer):
    class Meta:
        model = bmm
        fields = '__all__'
