# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RetailLoan(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.credit_card.doctype.retail_loan_product_table.retail_loan_product_table import RetailLoanProductTable
		from frappe.types import DF

		account_number: DF.SmallText | None
		applicant_name: DF.Data | None
		citizenship_number: DF.Data | None
		data_ybyp: DF.Data | None
		father_in_laws_name: DF.Data | None
		fathers_name: DF.Data | None
		grandfathers_name: DF.Data | None
		is_credit_card: DF.Data | None
		is_existing_customer: DF.Data | None
		issued_date: DF.Date | None
		issuing_district: DF.Data | None
		mothers_name: DF.Data | None
		pan_number: DF.Data | None
		product_table: DF.Table[RetailLoanProductTable]
		spouse_name: DF.Data | None
	# end: auto-generated types
	pass
