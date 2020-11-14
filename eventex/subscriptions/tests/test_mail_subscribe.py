from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name="Maurício Fagundes", cpf="12345678909",
                    email="mauricio.fagundes@gmail.com", phone="21-99811-9570")
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(self.email.subject, expect)

    def test_subscription_email_from(self):
        expect = 'mauricio@mfagundes.com.br'

        self.assertEqual(self.email.from_email, expect)

    def test_subscription_email_to(self):
        expect = ['mauricio@mfagundes.com.br', 'mauricio.fagundes@gmail.com']

        self.assertEqual(self.email.to, expect)

    def test_subscription_email_body(self):
        contents= [
            'Maurício Fagundes',
            '12345678909',
            'mauricio.fagundes@gmail.com',
            '21-99811-9570'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
