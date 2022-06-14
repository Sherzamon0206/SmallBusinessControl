from django.test import TestCase

import os

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

# choose english as language
os.environ["INVOICE_LANG"] = "en"

client = Client('Muhiddinocv Sherzamon')
provider = Provider('Ruzimurodov Nodirjon', bank_account='2600420569', bank_code='2010')
creator = Creator('Nodirjon')

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.currency = 'USZ '
invoice.use_tax = True
invoice.add_item(Item(3, 600, description="Item 1"))
invoice.add_item(Item(6, 50, description="Item 2", tax=21))
invoice.add_item(Item(12, 60, description="Item 3", tax=0))
invoice.add_item(Item(5, 600, description="Item 4", tax=15))

from InvoiceGenerator.pdf import SimpleInvoice

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf", generate_qr_code=True)

