
from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'url', 'created_at', 'type']
        read_only_fields = ['created_at']

    def update(self, instance, validated_data):
        # Only allow updating news items that were created through the API
        if instance.api_created:
            instance.title = validated_data.get('title', instance.title)
            instance.url = validated_data.get('url', instance.url)
            instance.type = validated_data.get('type', instance.type)
            instance.save()
            return instance
        raise serializers.ValidationError('This news item was not created through the API and cannot be updated.')

    def destroy(self, instance):
        # Only allow deleting news items that were created through the API
        if instance.api_created:
            instance.delete()
        else:
            raise serializers.ValidationError('This news item was not created through the API and cannot be deleted.')
