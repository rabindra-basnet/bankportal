# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LetterofCredit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.credit_card.doctype.other_charges_details.other_charges_details import OtherChargesDetails
		from frappe.model.document import Document
		from frappe.types import DF

		acceptance: DF.Check
		account_details: DF.Literal[None]
		add_amount_covered: DF.Data | None
		additional_condition: DF.LongText | None
		additional_request: DF.Literal[None]
		advice_through_bankif_any: DF.Data | None
		advising_bank_charges: DF.Literal[None]
		advising_banks_reference_no: DF.Data | None
		advising_swift_code: DF.Literal[None]
		advising_thru_bank_charges: DF.Literal[None]
		allow_margin_modification: DF.Literal[None]
		allow_pricing_modification: DF.Data | None
		allow_waive: DF.Literal[None]
		amendment_number: DF.Data | None
		amortization_of_charges: DF.Literal[None]
		amortize: DF.Literal[None]
		amount: DF.Int
		amount_covered: DF.Data | None
		amount_currency_code: DF.Literal[None]
		amount_lcy_value: DF.Data | None
		annual_basis: DF.Literal[None]
		applicable_rules: DF.Literal[None]
		applicant_account_number: DF.Data
		applicant_address: DF.Data | None
		applicant_bankif_any: DF.Literal[None]
		applicant_country: DF.Data | None
		applicant_email: DF.Data | None
		applicant_exim_code: DF.Data | None
		applicant_name: DF.Data
		applicant_pan_no: DF.Data | None
		applicant_phone: DF.Phone | None
		applicant_postal_code: DF.Data | None
		back_to_back: DF.Check
		bank_name: DF.Literal[None]
		beneficiary_account_number: DF.Int
		beneficiary_address_1: DF.Data | None
		beneficiary_address_2: DF.Data | None
		beneficiary_address_3: DF.Data | None
		beneficiary_name: DF.Data | None
		beneficiary_sanction_check: DF.Check
		blacklist_check: DF.Check
		branch_name: DF.Data | None
		cdd: DF.Check
		channel: DF.Literal[None]
		charge_amount: DF.Data | None
		charge_code: DF.Data | None
		charge_frequency: DF.Literal[None]
		charge_in_home_currency: DF.Data | None
		charges_agent__insurance_others: DF.Data | None
		charges_amount_date: DF.Date | None
		cif_id: DF.Data | None
		collection_method: DF.Literal[None]
		commision_account_details: DF.Data | None
		commision_allow_waive: DF.Literal[None]
		commision_of_charge_code: DF.Literal[None]
		confirmation_charges: DF.Literal[None]
		confirmation_instruction: DF.Literal[None]
		confirming_bank: DF.Literal[None]
		confirming_swift_code: DF.Data | None
		consolidatedshipping_agent: DF.Data | None
		corresponding_bank: DF.Literal[None]
		corresponding_branch: DF.Literal[None]
		country: DF.Literal[None]
		covered_by: DF.Literal[None]
		credit_avaiable_with: DF.Literal[None]
		custom_entry_point: DF.Data | None
		date: DF.Date | None
		date_of_expiry: DF.Date | None
		date_of_issue: DF.Date | None
		debit_amount: DF.Data | None
		deferred_payment: DF.Check
		deferred_payment_details: DF.Data | None
		delivery_terms: DF.Literal[None]
		demand_loan_additional_request: DF.Literal[None]
		demand_loan_excess_amount: DF.Data | None
		demand_loan_limits: DF.Data | None
		demand_loan_oustanding: DF.Data | None
		demand_loan_total_exposure: DF.Data | None
		description: DF.LongText | None
		direct_reimbursement: DF.Literal[None]
		documents_name: DF.Literal[None]
		drafts_at42c: DF.Literal[None]
		drawee: DF.Data | None
		due_date_indicator: DF.Literal[None]
		email: DF.Data | None
		entity: DF.Literal[None]
		excess_amount: DF.Data | None
		exim_code: DF.Int
		foreign_loan: DF.Literal[None]
		form_of_documentary_credit: DF.Literal[None]
		from_date: DF.Date | None
		fund_available: DF.Check
		funded_outstanding: DF.Data | None
		fx_rate: DF.Data | None
		goods: DF.Check
		hire_additional: DF.Literal[None]
		hire_excess_amount: DF.Data | None
		hire_loan: DF.Data | None
		hire_outstanding: DF.Data | None
		hire_total_exposure: DF.Data | None
		house_airway_bill_allowed: DF.Literal[None]
		in_transit_to: DF.Data | None
		initiated_by: DF.Data | None
		instructions_to_the_advising_negotiating_confirming_bank: DF.LongText | None
		insurance_covered_by: DF.Literal[None]
		insurance_details: DF.Data | None
		issuing_bank: DF.Literal[None]
		later_collection_amount: DF.Data | None
		latest_date_of_shipment: DF.Date | None
		lc_commision_account_number: DF.Data | None
		lc_commission_amount: DF.Data | None
		lc_commission_type: DF.Literal[None]
		lc_margin_account_amount: DF.Data | None
		lc_margin_account_number: DF.Data | None
		lc_margin_account_type: DF.Literal[None]
		lc_swift_account_number: DF.Data | None
		lc_swift_amount: DF.Data | None
		lc_swift_type: DF.Literal[None]
		lc_transferred_to: DF.Data | None
		limits: DF.Data | None
		margin_amount: DF.Data | None
		margin_collection_mode: DF.Data | None
		margin_currency: DF.Literal[None]
		margin_date: DF.Date | None
		margin_debit_credit_amount: DF.Data | None
		margin_details: DF.Literal[None]
		margin_details_account_details: DF.Data | None
		margin_later_collection_amount: DF.Data | None
		margin_modification_approved_by: DF.Data | None
		margin_ref_no: DF.Data | None
		margin_refund: DF.Literal[None]
		margin_treasury_rate: DF.Data | None
		margin_waiver_approved_by: DF.Data | None
		max_credit_amount: DF.Data | None
		min_charge_amount: DF.Data | None
		minimum_amount_for_amortization: DF.Data | None
		mixed_amount: DF.Check
		mixed_payment_details: DF.Data | None
		mobile_code: DF.Data | None
		mode_of_tansport: DF.Literal[None]
		mortage_limit: DF.Data | None
		mortgage_additional_request: DF.Literal[None]
		mortgage_excess_amount: DF.Data | None
		mortgage_outstanding: DF.Data | None
		mortgage_total_exposure: DF.Data | None
		negotiating_bank_ref_no: DF.Data | None
		negotiation: DF.Check
		non_conference_line_shipment_allowed: DF.Data | None
		non_dormat: DF.Check
		non_funded_additional: DF.Literal[None]
		non_funded_excess_amount: DF.Data | None
		non_funded_limits: DF.Data | None
		non_funded_outstanding: DF.Data | None
		non_funded_total_exposure: DF.Data | None
		open_ended: DF.Check
		origin_of_goods: DF.Data | None
		other_charges_outside_country: DF.Literal[None]
		others_on_deck: DF.Data | None
		outside_importing_country: DF.Data | None
		outstanding: DF.Data | None
		pan_no: DF.Int
		partial_shipment: DF.Literal[None]
		party_to_charge: DF.Literal[None]
		party_to_debitcreditlien: DF.Data | None
		payment: DF.Check
		pep_passed: DF.Check
		period_of_presentation: DF.Data | None
		phone_number: DF.Data | None
		place_of_expire: DF.Data | None
		place_of_final_destination: DF.Data | None
		place_of_taking_in_chargedispatch: DF.Data | None
		port_of_discharge: DF.Data | None
		port_of_loading: DF.Data | None
		ports: DF.Check
		pricing_currency: DF.Literal[None]
		pricing_modification_approved_by: DF.Data | None
		proforma_invoice_purchase_order: DF.Data | None
		red_letter: DF.Check
		ref_no: DF.Data | None
		ref_to_pre_advice: DF.Data | None
		remarks: DF.Data | None
		remarks_if_waiver_allowed: DF.LongText | None
		request_swift_code: DF.Data | None
		request_type: DF.Literal[None]
		revolving: DF.Check
		risky_juresdiction: DF.Data | None
		sanction_check: DF.Check
		select_additional_conditions: DF.Literal[None]
		sender_to_receiver_information: DF.LongText | None
		settlement_bank_name: DF.Literal[None]
		settlement_instructions: DF.LongText | None
		settlement_swift_code: DF.Literal[None]
		shipment_additional_request: DF.Literal[None]
		shipment_excess_amount: DF.Data | None
		shipment_limits: DF.Data | None
		shipment_mode: DF.Data | None
		shipment_outstanding: DF.Data | None
		shipment_period: DF.Data | None
		shipment_total_exposure: DF.Data | None
		show_hide: DF.Check
		sol_id: DF.Data | None
		special_payment_conditionfor_beneficiary: DF.Literal[None]
		special_payment_conditionfor_receiving_bank: DF.Literal[None]
		specify: DF.Data | None
		spot_contract_signed: DF.Literal[None]
		spot_rate_incase_of_currency_other_than_home_country: DF.Data | None
		standby: DF.Check
		statutory: DF.Data | None
		statutory_details: DF.Literal[None]
		statutory_margin_amount: DF.Data | None
		statutory_margin_refund: DF.Literal[None]
		statutory_type_flat: DF.Literal[None]
		swift_code: DF.Data | None
		table_kbos: DF.Table[Document]
		table_kurj: DF.Table[OtherChargesDetails]
		team_loan_limits: DF.Data | None
		tenor: DF.Literal[None]
		term_additional_request: DF.Literal[None]
		term_excess_amount: DF.Data | None
		term_outstanding: DF.Data | None
		term_total_exposure: DF.Data | None
		to_date: DF.Date | None
		tolerance_negative: DF.Data | None
		tolerance_positive: DF.Data | None
		total_amount_including_charges: DF.Data | None
		total_exposure: DF.Data | None
		trade_country: DF.Check
		trade_services: DF.Data | None
		transferra: DF.Check
		transhipment: DF.Literal[None]
		treasury_rate: DF.Data | None
		trust_additional_request: DF.Data | None
		trust_excess_amount: DF.Data | None
		trust_limits: DF.Data | None
		trust_total_exposure: DF.Data | None
		type: DF.Literal[None]
		type_flat: DF.Literal[None]
		type_of_lc: DF.Literal[None]
		valid: DF.Check
		valid_until: DF.Date | None
		vessels: DF.Check
		vpn_enabled: DF.Data | None
		waiver_approved_by: DF.Data | None
		work_item_number: DF.Data | None
	# end: auto-generated types
	pass
