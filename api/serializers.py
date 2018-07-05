from rest_framework import serializers

from api.models import Company, Person, FoodItem


class PersonSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='name')
    fruits = serializers.SerializerMethodField()
    vegetables = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('username', 'age', 'fruits', 'vegetables')

    def get_fruits(self, person):
        return person.favourite_foods.filter(category='fruit').values_list('name', flat=True)

    def get_vegetables(self, person):
        return person.favourite_foods.filter(category='vegetable').values_list('name', flat=True)


class MinimalPersonSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='name')

    class Meta:
        model = Person
        fields = ('username', 'age', 'address', 'phone')


class CompanySerializer(serializers.ModelSerializer):
    employees = PersonSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'employees')
