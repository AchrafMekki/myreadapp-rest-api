from rest_framework import serializers
from apps.book.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # TODO specify the model that this serializer will link to
    # TODO specify which fiels should be considered in the model

    name = serializers.CharField()  # read-only

    # Create a serialized metod
    username = serializers.SerializerMethodField()

    #  Serial

    def get_username(self,obj):
        return '_'.join([obj.first_name, obj.last_name])


    def validate_first_name(self, value):  # validate_<field_name>
        if "-" in value:
            # TODO: Always raise a validation exception when condition fails
            raise serializers.ValidationError('first name should not contain hyphen (-)')
            # TODO : If condition is true, then return the value
        return value


    def validate(self, attrs):  # valide
        """Object-level Validation"""

        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first name and last name should not be the same')
        return attrs

    class Meta:
        model = Author
        fields = '__all__'  # ('id', 'first_name', 'last_name')
