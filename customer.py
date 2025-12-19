@frappe.whitelist(allow_guest=True)
def register(full_name,mobile_number,email,password,is_active):
	register = frappe.get_doc({
			'doctype':'Courier Customer',
			'full_name':full_name,
			'mobile_number':mobile_number,
			'email':email,
			'password':password,
			'is_active':is_active
})
	register.insert(ignore_permission=True)

	return {"registered_name":register.name}



@frappe.whitelist()
def create_request(request_id,customer,parcel_type,estimated_weight,estimated_distance):
	request = frappe.get_doc({
			'doctype':'Courier Request',
			'request_id':request_id,
			'customer':customer,
			'parcel_type':parcel_type,
			'estimated_weight':estimated_weight,
			'estimated_distance':estimated_distance
})
	request.insert(ignore_permission=True)

	return {"requested_name":request.name}



def cutomer_login(username,password):
        login_customer = frappe.auth.LoginManager()
        login_customer.authenticate(username,password)
        login_customer.post_login()

        user = frappe.get_doc('User',username)

        if not user:
                frappe.throw('No User')
        if not user.api_key:
                user.api_key = frappe.generate_hash(length=15)
        api_secret = frappe.generate_hash(length=15)
        user.api_secret = api_secret
        user.save()

        return {'api_key':user.api_key,'api_secret':api_secret}


