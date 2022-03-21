from rest_framework import serializers
from .models import Nordic


class NordicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nordic
        fields = ['title', 'state', 'commit_hash', 'built_at', 'committed_at', 'author', 'email', 'fw_binary']
