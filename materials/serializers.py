from rest_framework import serializers
from materials.models import Handout

class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = ('id', 'created', 'text', 'words', 'word_order', 'definitions', 'definitions_order')

# class MaterialSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=False, max_length=200)
#     level = serializers.CharField(required=True, allow_blank=False, max_length=2)
#
#     def create(self, validated_data):
#         return Material.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.level = validated_data.get('level', instance.level)
#         instance.save()
#         return instance
