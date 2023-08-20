import frappe
from frappe.utils.print_format import report_to_pdf
 
# def get_context(context):
# 	print=''
# 	selling_settings=frappe.get_doc("Selling Settings")
# 	if selling_settings:
# 		inv_no = frappe.request.url.split('?')[1][:-3]
# 		inv_type = frappe.request.url[-3:]
# 		if inv_type == 'POS':
# 			if selling_settings.pos_invoice_format:
# 				print = frappe.get_doc('Print Format', selling_settings.pos_invoice_format)
# 				doc = frappe.get_doc('POS Invoice', inv_no)
# 		elif inv_type == 'INV':
# 			if selling_settings.sales_invoice_format:
# 				print = frappe.get_doc('Print Format', selling_settings.sales_invoice_format) # Only custom formats allowed
# 				doc = frappe.get_doc('Sales Invoice', inv_no)

# 	context.body = frappe.render_template(print.html, {"doc":doc})


@frappe.whitelist()
def get_sms_body(url):
	print=''
	selling_settings=frappe.get_doc("Selling Settings")
	if selling_settings:
		inv_no = url.split('?')[1][:-3]
		inv_type = url[-3:]
		if inv_type == 'POS':
			if selling_settings.pos_invoice_format:
				print = frappe.get_doc('Print Format', selling_settings.pos_invoice_format)
				doc = frappe.get_doc('POS Invoice', inv_no)
		elif inv_type == 'INV':
			if selling_settings.sales_invoice_format:
				print = frappe.get_doc('Print Format', selling_settings.sales_invoice_format) # Only custom formats allowed
				doc = frappe.get_doc('Sales Invoice', inv_no)

	return frappe.render_template(print.html, {"doc":doc})
