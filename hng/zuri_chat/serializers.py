from rest_framework import serializers

from zuri_chat.models import bio

class BioSerializer(serializers.ModelSerializer):
   class Meta:
       model = bio
       fields = ('slack_username', 'backend', 'age', 'bio')

