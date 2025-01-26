# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BeneficiaryDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		anticipated_no_of_transaction_per_year: DF.Literal[None]
		are_you_associated_with_foreign_country: DF.Literal[None]
		customer_cif_id: DF.Data | None
		customer_relation: DF.Literal[None]
		district: DF.Data | None
		email: DF.Data | None
		father_name: DF.Data | None
		first_name: DF.Data | None
		foreign_citydistrict: DF.Literal[None]
		foreign_state: DF.Literal[None]
		foreign_vdcmunicipality: DF.Data | None
		full_name: DF.Data | None
		gender: DF.Literal[None]
		grandfathers_name: DF.Data | None
		have_you_been_punished_for_any_crime: DF.Literal[None]
		high_level_officialpep: DF.Literal[None]
		house_number: DF.Data | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		mobile_code: DF.Data | None
		mobile_number: DF.Data | None
		mothers_name: DF.Data | None
		name_of_country: DF.Data | None
		nationality: DF.Literal[None]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		phone_number: DF.Data | None
		province: DF.Data | None
		saluation: DF.Literal[None]
		select_erpq: DF.Literal[None]
		spouse_name: DF.Data | None
		streettole: DF.Data | None
		vdcmunicipality: DF.Data | None
		ward_number: DF.Data | None
	# end: auto-generated types
	pass
