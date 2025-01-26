# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BankGuaranteeUpdated(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.credit_card.doctype.bg_beneficiary_details.bg_beneficiary_details import BGBeneficiaryDetails
		from frappe.credit_card.doctype.bg_description_of_goods_and_services.bg_description_of_goods_and_services import BGDescriptionofGoodsAndServices
		from frappe.credit_card.doctype.jv_details.jv_details import JVDetails
		from frappe.types import DF

		amended_from: DF.Link | None
		beneficiary_table_data: DF.Table[BGBeneficiaryDetails]
		carrier_name_and_address: DF.Data | None
		custom_applicant_name: DF.Data | None
		custom_applicant_type: DF.Literal["", "Single", "JV"]
		custom_beneficiary_type: DF.Literal["", "Suppliers Credit", "Customs", "Court"]
		custom_bg_category: DF.Literal["", "Suppliers Credit", "Customs", "Court", "Vehicle Permit", "Government", "Industry", "Trading"]
		custom_bg_expiry_place: DF.Data | None
		custom_carrier_id: DF.Data | None
		custom_cif_id: DF.Data | None
		custom_claim_expiry_date: DF.Date | None
		custom_classification_of_bg: DF.Literal["", "Local", "Counter Guarantee (International Gtee)", "BG against Counter G'tee", "Line of Credit/Commitment Liability", "Others"]
		custom_contract_date: DF.Date | None
		custom_contract_number: DF.Data | None
		custom_for_of_undertaking: DF.Literal["", "DGAR (Demand Guarantee)", "STBY (Standby LC)"]
		custom_lc_amount: DF.Data | None
		custom_lc_number: DF.Data | None
		custom_numberof_beneficiary: DF.Int
		custom_type_of_bg: DF.Literal["", "Tender G'tee (Bid Bond)", "Performance G'tee", "Financial G'tee", "Advance Payment G'tee", "Retention & Warranty Bond", "Deferred Payment G'tee", "Payment G'tee", "Shipping G'tee"]
		custom_undertaking_amount_figures: DF.Data | None
		custom_undertaking_currency_code: DF.Literal["", "USD", "NPR", "EUR", "GBP", "INR", "JPY", "AUD", "CAD"]
		custom_valid_until: DF.Date | None
		custom_vechicle_details: DF.Data | None
		file: DF.Literal["", "Select pdf to Upload", "Select Image to Upload"]
		file_upload_to_ai: DF.Attach | None
		goods_descrition_details: DF.Table[BGDescriptionofGoodsAndServices]
		image_upload_to_ai: DF.AttachImage | None
		jv_details_table: DF.Table[JVDetails]
		pan_holder_name: DF.Data | None
		pan_number: DF.Data | None
		pan_registration_date: DF.Data | None
		pan_registration_office: DF.Data | None
		pan_registration_type: DF.Data | None
		purpose_of_guarantee: DF.Data | None
		status: DF.Data | None
	# end: auto-generated types
	pass
