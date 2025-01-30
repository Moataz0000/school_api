from .models import Subject
from rest_framework import serializers
from .repository import SubjectRepo



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['created_at']
        
    
    def __init__(self, *args, **kwargs):
        """Dynamically remove 'is_active' from writable fields when creating an object."""
        super().__init__(*args, **kwargs)
        
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.fields['is_active'].read_only = True
            
        
    def create(self, validated_data):
        return SubjectRepo.add_subject(**validated_data)
    
    
    def update(self, instance, validated_data):
        subject = SubjectRepo.modify_subject(
            pk=instance.id, 
            title=validated_data.get("title", instance.title),
            is_active=validated_data.get("is_active", instance.is_active)
        )
        return subject
