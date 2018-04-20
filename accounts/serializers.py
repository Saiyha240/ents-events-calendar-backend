from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from accounts.models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nickname', 'birthday', 'gender')


class UserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'profile')

    profile = ProfileSerializer(required=True)

    def create(self, validated_data):
        return super().create(validated_data)

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user
    #
    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     # Unless the application properly enforces that this field is
    #     # always set, the follow could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     profile = instance.profile
    #
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #
    #     profile.is_premium_member = profile_data.get(
    #         'is_premium_member',
    #         profile.is_premium_member
    #     )
    #     profile.has_support_contract = profile_data.get(
    #         'has_support_contract',
    #         profile.has_support_contract
    #     )
    #     profile.save()
    #
    #     return instance
