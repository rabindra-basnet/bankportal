# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PanDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		city_name: DF.Data | None
		pan_holder_name: DF.Data | None
		pan_number: DF.Data | None
		pan_registration_date: DF.Data | None
		pan_registration_office: DF.Data | None
		pan_registration_type: DF.Data | None
		status: DF.Data | None
		street_name: DF.Data | None
		telephone: DF.Data | None
		ward_number: DF.Data | None
	# end: auto-generated types
	pass
