from rest_framework import serializers
from .models import Ustoz, Guruh, Talaba


class UstozSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    guruhlar = serializers.SerializerMethodField()
    guruhlar_soni = serializers.SerializerMethodField()

    class Meta:
        model = Ustoz
        fields = ['id', 'firstname', 'lastname', 'subject', 'full_name', 'guruhlar', 'guruhlar_soni']

    def get_full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"
    
    def get_guruhlar(self, obj):
        return [guruh.name for guruh in obj.guruhlar.all()]
    
    def get_guruhlar_soni(self, obj):
        return obj.guruhlar.count()
    


class GuruhSerializer(serializers.ModelSerializer):
    ustoz_fullname = serializers.StringRelatedField(source='ustoz')
    students = serializers.SerializerMethodField()

    class Meta:
        model = Guruh
        fields = ['id', 'name', 'ustoz', 'ustoz_fullname', 'students']

    
    def get_students(self, obj):
        return [f"{talaba.firstname} {talaba.lastname}" for talaba in obj.talabalar.all()]


class TalabaSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    group_name = serializers.CharField(source='group.name', read_only=True)
    class Meta:
        model = Talaba
        fields = ['id', 'firstname', 'lastname', 'birth_date', 'grade', 'group', 'full_name', 'group_name']
    

    def get_full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"