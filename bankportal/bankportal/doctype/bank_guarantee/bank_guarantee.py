# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BankGuarantee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.credit_card.doctype.bg_beneficiary_details.bg_beneficiary_details import BGBeneficiaryDetails
		from frappe.credit_card.doctype.bg_description_of_goods_and_services.bg_description_of_goods_and_services import BGDescriptionofGoodsAndServices
		from frappe.credit_card.doctype.deferral_table.deferral_table import DeferralTable
		from frappe.credit_card.doctype.facility_sheet.facility_sheet import FacilitySheet
		from frappe.credit_card.doctype.jv_details.jv_details import JVDetails
		from frappe.types import DF

		account_details: DF.Data | None
		additional_amount_information: DF.Data | None
		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		address_line_3: DF.Data | None
		adviseswiftcode: DF.Literal[None]
		advisethroughbankname: DF.Literal[None]
		advising_bank_reference_number: DF.Data | None
		advisingname: DF.Literal[None]
		advisingswiftcode: DF.Literal[None]
		aggregate_limit: DF.Data | None
		allow_margin_modification: DF.Literal[None]
		allow_waive: DF.Literal[None]
		amended_from: DF.Link | None
		amortization_of_charges: DF.Literal[None]
		amortize: DF.Literal[None]
		amount: DF.Data | None
		applicable_rules: DF.Literal["None", "URDG", "UCPR", "ISPR", "Other"]
		applicant_name: DF.Data | None
		applicant_type: DF.Literal["", "Single", "JV"]
		approval_obtained: DF.Literal["", "Yes", "No"]
		approval_obtained_to_issue_fcy_bg: DF.Data | None
		automatic_extension_final_expiry_date: DF.Date | None
		automatic_extension_notification_period: DF.Data | None
		automatic_extension_period: DF.Literal[None]
		automatic_extensionnon_extension_notification: DF.Data | None
		available_amount: DF.Data | None
		available_with: DF.Data | None
		availablewithbankname: DF.Literal[None]
		availablewithswiftcode: DF.Literal[None]
		bank_branch: DF.Data | None
		bank_name: DF.Literal[None]
		beneficiary_type: DF.Literal["", "Government", "Others"]
		bg_amount: DF.Data | None
		bg_category: DF.Literal["", "Suppliers Credit", "Customs", "Court", "Vehicle Permit", "Government", "Industry", "Trading"]
		bg_expiry_date: DF.Date | None
		bg_expiry_place: DF.Data | None
		bg_format_vetted__approved: DF.Data | None
		bg_issuance_charges: DF.Literal[None]
		bg_issuance_charges_charges_outside_country: DF.Literal[None]
		bg_type: DF.Literal["", "Inward", "Outward"]
		bgissuingbank: DF.Literal[None]
		bill_of_lading_no: DF.Data | None
		caa_account_balance: DF.Data | None
		caa_account_number: DF.Data | None
		carrier_id: DF.Data | None
		carrier_name_and_address: DF.Data | None
		cg_clause_vetted__approved: DF.Data | None
		cg_expiry_date: DF.Data | None
		cg_issuance_compliance_checked: DF.Data | None
		charge_amount: DF.Data | None
		charge_code: DF.Literal[None]
		charge_in_home_currency: DF.Data | None
		chargesmargin_debit_account_number: DF.Data | None
		cif_id: DF.Data | None
		claim_expiry_date: DF.Date | None
		claim_period: DF.Data | None
		clasification_of_bg: DF.Literal["", "Local", "Counter Guarantee (International Gtee)", "BG against Counter G'tee", "Line of Credit/Commitment Liability", "Others"]
		collection_mode: DF.Literal[None]
		confirmation_instructions: DF.Literal[None]
		confirmingbankname: DF.Literal[None]
		confirmingbankswiftcode: DF.Literal[None]
		contact_number: DF.Data | None
		contract_date: DF.Date | None
		contract_number: DF.Data | None
		country: DF.Literal[None]
		ctsbgalladdress: DF.SmallText | None
		ctsbgallbenename: DF.SmallText | None
		currency_code: DF.Literal[None]
		currency_type: DF.Literal[None]
		customer_email_address: DF.Data | None
		customer_id: DF.Data | None
		data_bfxf: DF.Data | None
		data_dviz: DF.Data | None
		data_ebod: DF.Data | None
		data_vcim: DF.Data | None
		data_ycdz: DF.Data | None
		data_yfkh: DF.Data | None
		data_zsfe: DF.Data | None
		date_of_installment_due: DF.Date | None
		date_of_issue: DF.Date | None
		date_xzfy: DF.Date | None
		days__month__quarter: DF.Data | None
		debit_amount: DF.Data | None
		deferral_received_by_rm: DF.Literal[None]
		delivery_of_original_undertaking: DF.Data | None
		delivery_to__collection_by: DF.Literal[None]
		demand_indicator: DF.Data | None
		direct_reimbursements: DF.Literal[None]
		document_and_presentation_instruction: DF.Data | None
		documentlcyamount: DF.Data | None
		draweebankname: DF.Literal[None]
		draweeswiftcode: DF.Literal[None]
		effective_date: DF.Date | None
		email: DF.Data | None
		exchange_rate: DF.Data | None
		exim_code_no: DF.Data | None
		expiry_conditionevent: DF.Data | None
		expiry_date: DF.Data | None
		expiry_tenure_type: DF.Literal["", "OPEN (Open ended)", "FIXD (Fixed Term)", "COND"]
		force_majuere_clause: DF.Literal["", "Yes", "No"]
		form_of_undertaking: DF.Literal["", "DGAR (Demand Guarantee)", "STBY (Standby LC)"]
		format_vetted__approved: DF.Literal["", "Yes", "No"]
		from_date: DF.Date | None
		fx_rate: DF.Data | None
		fx_rate_code: DF.Data | None
		gacountry: DF.SmallText | None
		generate_swift_message__gtee_text: DF.Literal[None]
		governing_law__place_of_jurisdiction: DF.Data | None
		governing_law_andor_place_of_jurisdiction: DF.Literal[None]
		guaddressline2: DF.Data | None
		guaddressline3: DF.Data | None
		guaddressline: DF.Data | None
		gucountry: DF.Data | None
		installment_payment_details: DF.Literal["", "Monthly", "Quarterly", "Annually"]
		invoked_liability_exists: DF.Literal["", "Yes", "No"]
		issuanceagainstdateofissue: DF.Date | None
		issuer: DF.Data | None
		issuingbankclaimperiond: DF.Data | None
		issuingbankexpiryplace: DF.Data | None
		issuingbankname: DF.Literal[None]
		jv_detail: DF.Table[JVDetails]
		lc_amount_fcy: DF.Data | None
		lcy_amount: DF.Data | None
		lcy_value: DF.Data | None
		limit_node_to_be_used: DF.Data | None
		limit_suffix: DF.Data | None
		margin_amount: DF.Data | None
		margin_currency: DF.Data | None
		margin_debitcredit_account: DF.Data | None
		margin_details: DF.Literal[None]
		margin_refund: DF.Literal[None]
		min_charge_amount: DF.Data | None
		minimum_amount_for_amortization: DF.Data | None
		no_of_beneficiary: DF.Int
		obligorbankname: DF.Literal[None]
		oda_account_balance: DF.Data | None
		oda_account_number: DF.Data | None
		pan_no: DF.Data | None
		party_limit_id: DF.Data | None
		party_to_charge: DF.Literal[None]
		purpose_of__guarantee: DF.Data | None
		purpose_of_messgae: DF.Literal[None]
		rate_code: DF.Literal["", "Buy", "Sell", "Mid"]
		receivers_contact_number: DF.Data | None
		receivers_id_number: DF.Data | None
		receivers_name: DF.Data | None
		reimbursingaccountdetail: DF.Data | None
		reimbursingbankname: DF.Literal[None]
		remarks_for_cg: DF.SmallText | None
		remarks_if_waiver_allowed: DF.SmallText | None
		remarls: DF.SmallText | None
		requestconfirmswiftcode: DF.Literal[None]
		requested_local_undertaking_terms_and_conditions: DF.Data | None
		requested_value_in_words: DF.Data | None
		requestedconfirmationbankname: DF.Literal[None]
		segment: DF.Literal["Select"]
		select_ifhr: DF.Literal["", "Bank Standard", "Beneficiary's Format", "Bank Standard with changes"]
		select_ljee: DF.Literal[None]
		select_tyzv: DF.Literal[None]
		sender_to_receiver_information72: DF.SmallText | None
		sender_to_receiver_information: DF.Literal[None]
		settlement_sender_to_receiver_information: DF.Data | None
		settlementaccountdetails: DF.Literal[None]
		settlementbankname: DF.Literal[None]
		settlementswiftcode: DF.Literal[None]
		situatorytype: DF.Literal[None]
		spot_contract_signed: DF.Data | None
		spot_rate_incase_of_currency_other_than_home_currency: DF.Data | None
		standard_wording_requested_language: DF.Data | None
		statutory_details: DF.Literal[None]
		statutorymarginrefu: DF.Literal[None]
		sustantiate_claims: DF.Data | None
		swift_code: DF.Literal[None]
		table_egco: DF.Table[BGDescriptionofGoodsAndServices]
		table_ezal: DF.Table[BGBeneficiaryDetails]
		table_gbax: DF.Table[FacilitySheet]
		table_xidv: DF.Table[DeferralTable]
		task: DF.Literal["", "BG Copy", "BG Issue", "Amend", "Modify", "Verify", "Cancel", "Mark as Invoke", "Invoke"]
		transaction_referrence_no: DF.Data | None
		transfer_conditions: DF.Data | None
		transfer_indicator: DF.Data | None
		tt_debit_account: DF.Data | None
		type_flat: DF.Literal[None]
		type_of_bg: DF.Literal["", "Tender G'tee(Bid Bond)", "Performance G'tee", "Financial G'tee", "Advance Payment G'tee", "Retention & Warranty Bond", "Deferred Payment G'tee", "Payment G'tee", "Shipping G'tee"]
		type_of_undertaking: DF.Literal[None]
		under_taking_amount_currency_code: DF.Literal[None]
		under_taking_amount_figures: DF.Data | None
		underlying_transaction_details: DF.Data | None
		undertaking_amount_fx_rate: DF.Data | None
		undertaking_amount_lcy_value: DF.Data | None
		undertaking_number: DF.Data | None
		undertaking_terms_and_conditions: DF.Data | None
		unverified_bg_amount: DF.Literal[None]
		valid_until: DF.Date | None
		validity: DF.Data | None
		value_of_documentrequest_amountproposed: DF.Data | None
	# end: auto-generated types
	pass
