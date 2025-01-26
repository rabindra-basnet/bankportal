# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BGBeneficiaryDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.Data | None
		address_line_3: DF.Data | None
		beneficiary_contact_person: DF.Data | None
		beneficiary_name: DF.Data | None
		contact_number: DF.Data | None
		country: DF.Data | None
		email: DF.Data | None
		form_settings_connections_no_label: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types
	pass
