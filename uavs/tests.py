from django.test import TestCase
from django.contrib.auth.models import User
from .models import Uav, Reservation, Brand, Category, create_slug
from datetime import datetime, timedelta


# Create your tests here.

class ReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        brand = Brand.objects.create(name='testbrand', slug=create_slug('testbrand'))
        category = Category.objects.create(name='testcategory', slug=create_slug('testcategory'))
        self.uav = Uav.objects.create(name='testuav', model='testmodel', weight='123', brand=brand, category=category)

        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=1)

        self.reservation = Reservation.objects.create(uav=self.uav, user=self.user, start_date=self.start_date,
                                                      end_date=self.end_date)

    def test_reservation_creation(self):
        new_reservation = Reservation.objects.create(
            uav=self.uav,
            user=self.user,
            start_date=self.end_date + timedelta(days=1),
            end_date=self.end_date + timedelta(days=3)
        )
        self.assertTrue(isinstance(new_reservation, Reservation))

    def test_reservation_date_overlap(self):
        with self.assertRaises(ValueError):
            Reservation.objects.create(
                uav=self.uav,
                user=self.user,
                start_date=self.start_date,
                end_date=self.end_date
            )

    def test_reservation_date_validation(self):
        with self.assertRaises(ValueError):
            Reservation.objects.create(
                uav=self.uav,
                user=self.user,
                start_date=self.end_date,
                end_date=self.start_date
            )
