from rest_framework import serializers

from pladform.models import Blog, Author


class BLogSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Blog
        fields = [
            'id',
            'name',
            'tagline',
            'url'
        ]

        # read_only_fields = ['name']
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    @staticmethod
    def validate_tagline(value):
        if value in ['huj']:
            raise serializers.ValidationError('sam ty huj')
        return value


