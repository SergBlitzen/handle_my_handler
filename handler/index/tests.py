from django.test import TestCase

from index.models import Handler, SocialLink


class HandlerTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.handler = Handler.objects.create(
            greeting='Test headline',
            nickname='test_nickname',
            mail='test.com'
        )
        cls.social_1 = SocialLink.objects.create(
            sitename='test.org',
            link='https://test.org/test_nickname',
            handler=cls.handler
        )
        cls.social_2 = SocialLink.objects.create(
            sitename='test_2.org',
            link='https://test_2.org/test_nickname',
            handler=cls.handler
        )

    def test_models_exists(self):
        handler_count = Handler.objects.count()
        self.assertEqual(handler_count, 1)

    def test_models_create(self):
        Handler.objects.create(
            greeting='New test headline',
            nickname='new_test_nickname',
            mail='test.com'
        )
        handler_count = Handler.objects.count()
        self.assertEqual(handler_count, 2)

    def test_handler_links_access(self):
        links = HandlerTestCase.handler.sitelinks.all()
        self.assertEqual(len(links), 2)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


class SocialLinkTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.handler = Handler.objects.create(
            greeting='Test headline',
            nickname='test_nickname',
            mail='test.com'
        )
        cls.social_1 = SocialLink.objects.create(
            sitename='test.org',
            link='https://test.org/test_nickname',
            handler=cls.handler
        )
        cls.social_2 = SocialLink.objects.create(
            sitename='test_2.org',
            link='https://test_2.org/test_nickname',
            handler=cls.handler
        )

    def test_models_exists(self):
        links_count = SocialLink.objects.count()
        self.assertEqual(links_count, 2)

    def test_models_create(self):
        SocialLink.objects.create(
            sitename='test_3.org',
            link='https://test_3.org/test_nickname',
            handler=SocialLinkTestCase.handler
        )
        links_count = SocialLink.objects.count()
        self.assertEqual(links_count, 3)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
