import datetime

from api.models import Document, Department
from django.test import TestCase


class SetupTestCase(TestCase):
    def setUp(self):
        d = Document()
        dep = Department()
        try:
            dep.name = 'NIH'
            dep.save()
        except:
            self.fail('Department could not be saved!')
        try:
            d.title = 'Correlations within Causations'
            d.institution = 'COS'
            d.PI_first_name = 'Foo'
            d.PI_last_name = 'Bar'
            d.PI_email = 'foo@bar.com'
            d.status = 'Pending'
            d.date_published = datetime.datetime.now()  # update this to use datetime
            d.file_link = '~/doc.txt'
            d.department = dep
            d.save()
        except:
            self.fail('Document could not be saved!')

    def test_if_something(self):
        x = 1 + 1
        self.assertEqual(x, 2)
