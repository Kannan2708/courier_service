### Courier Service

Courier service informations

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app courier_service
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/courier_service
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit







#setup steps:

1. using bench new-app courier_service, installed the custom app
2. using bench --site demo.com install-app courier_service, installed the app in the repective site


# API List

Customer API List
1. POST /api/customer/register
2. POST /api/customer/customer_login
3. POST /api/customer/create_request


Provider API List
1. POST /api/provider/provider_login
2. GET /api/provider/fetch_pending
3. POST /api/provider/accept_delivery
4. POST /api/provider/update_delivery_status



#worklow explanation


in workflow doctype i have created a new worklow for courier request doctype so that when the service provider is accepting the parcel and when the delievry partner is picking up is tracked in the document through the status 
change.

here there is a role called 'Service Provider' that role assigned users alone make a accept of the parcel and there is a role called 'Delivery Partner' were the role assigned persons alone need to pick up the parcel
and here when the courier request is delivered only the document will be submitted. otherwise the docstatus remains 0.
