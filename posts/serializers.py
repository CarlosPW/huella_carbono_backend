from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "address_start_point",
            "address_end_point",
            "transportation",
            "kilometers",
            "users",
            "round_trip",
        )
        model = Post