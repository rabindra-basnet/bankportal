# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RetailLoanProductTable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		interest_rate: DF.Data | None
		loan_amount: DF.Data | None
		loan_tenure: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		product_type: DF.Data | None
		purpose_of_loan: DF.Data | None
	# end: auto-generated types
	pass
