import json
from django.test import TestCase
from django.shortcuts import reverse
from api.models import Person, Company, FoodItem


class CompanyEndpointTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(name="test_company")
        self.person = Person.objects.create(name="test", company=self.company)

    def tearDown(self):
        self.company.delete()
        self.person.delete()

    def test_company_endpoint(self):
        url = reverse('company-view', kwargs={'pk': self.company.pk})
        response = self.client.get(url)
        expected_output = {
            "id": self.company.pk, "name": "test_company",
            "employees": [{"username": "test", "age": 0, "fruits": [], "vegetables": []}]
        }
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), expected_output)


class PersonEndpointTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(name="test_company")
        self.aubergine = FoodItem.objects.create(name='aubergine', category='vegetable')
        self.apple = FoodItem.objects.create(name='apple', category='fruit')
        self.person = Person.objects.create(name="test", company=self.company)
        self.person.favourite_foods = [self.apple, self.aubergine]

    def tearDown(self):
        self.company.delete()
        self.aubergine.delete()
        self.apple.delete()
        self.person.delete()

    def test_person_endpoint(self):
        url = reverse('person-view', kwargs={'pk': self.person.pk})
        response = self.client.get(url)
        expected_output = {
            u'age': 0,
            u'fruits': [u'apple'],
            u'username': u'test',
            u'vegetables': [u'aubergine']}
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), expected_output)


class CommonFriendsEndpointTest(TestCase):

    def setUp(self):
        self.brown_eyed_alive = [
            Person.objects.create(name="common_one", eye_color="brown", deceased=False),
            Person.objects.create(name="common_two", eye_color="brown", deceased=False)
        ]
        self.brown_eyed_dead = [
            Person.objects.create(name="nooo", eye_color="brown", deceased=True),
            Person.objects.create(name="nope", eye_color="brown", deceased=True)
        ]
        self.blue_eyed = [
            Person.objects.create(name="nooo2", eye_color="blue", deceased=False),
            Person.objects.create(name="nope2", eye_color="blue", deceased=False)
        ]
        self.person_one = Person.objects.create(name="test")
        self.person_one.friends = [self.brown_eyed_alive[0], self.blue_eyed[1], self.brown_eyed_dead[1]]
        self.person_two = Person.objects.create(name="test")
        self.person_two.friends = [self.brown_eyed_alive[0],
                                   self.brown_eyed_alive[1],
                                   self.blue_eyed[1], self.brown_eyed_dead[1]]

    def tearDown(self):
        for instance in self.brown_eyed_dead:
            instance.delete()
        for instance in self.blue_eyed:
            instance.delete()
        for instance in self.brown_eyed_alive:
            instance.delete()
        self.person_one.delete()
        self.person_two.delete()

    def test_person_endpoint(self):
        url = reverse('common-friends-view', kwargs={
            'user_id': self.person_one.pk, 'comparison_user_id': self.person_two.pk})
        response = self.client.get(url)
        expected_output = {u'common_friends': [u'common_one'],
                           u'user_one': {u'address': None,
                                         u'age': 0,
                                         u'phone': None,
                                         u'username': u'test'},
                           u'user_two': {u'address': None,
                                         u'age': 0,
                                         u'phone': None,
                                         u'username': u'test'}}
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), expected_output)