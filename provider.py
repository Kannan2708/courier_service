@frappe.whitelist(allow_guest=True)
def provider_login(username,password):
	login_provider = frappe.auth.LoginManager()
	login_provider.authenticate(username,password)
	login_provider.post_login()

	user = frappe.get_doc('User',username)

	if not user:
		frappe.throw('No User')
	if not user.api_key:
		user.api_key = frappe.generate_hash(length=15)
	api_secret = frappe.generate_hash(length=15)
	user.api_secret = api_secret
	user.save()

	return {'api_key':user.api_key,'api_secret':api_secret}


@frappe.whitelist()
def update_delivery_status(status,name):
	frappe.db.set_value('Courier Request',name,"status",status)
	frappe.db.commit()

@frappe.whitelist()
def accept_delivery(status,name):
	frappe.db.set_value("Courier Request",name,"status",status)
	frappe.db.commit()

@frappe.whitelist()
def fetch_pending(status):
	return frappe.get_doc('Courier Request',filters:{'status':'pending'})

