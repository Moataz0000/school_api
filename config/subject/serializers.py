from .models import Subject
from rest_framework import serializers
from .repository import SubjectRepo



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['is_active', 'created_at']
        
    def create(self, validated_data):
        return SubjectRepo.add_subject(**validated_data)