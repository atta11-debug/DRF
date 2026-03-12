from rest_framework.serializers import Serializer, ModelSerializer
from .models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
