from rest_framework import serializers
from apps.book.models import Tag
import re


class TagSerializer(serializers.Serializer): 
    
    name = serializers.SerializerMethodField(read_only=True)
    
    def name(self,obj):
        return obj.name.title()

    
    def validate_tag_name(self,value):
        # if value in ['%','!','@','#','$','%','^','&','*']:
        #     raise serializers.ValidationError(
        #         "Tag nameshould not contain special characters like '%','!','@','#','$','%','^','&','*'"
        #         )
        # return value

        if re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError("Tag name should not contain special characters like !@#$%^&*")
        return value

    class Meta:
        model = Tag
        fields = "__all__"  # ('id', 'name')
        read_only_fields = ('id',)
