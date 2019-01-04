from rest_framework import serializers
from materials.models import Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'title', 'level')

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
