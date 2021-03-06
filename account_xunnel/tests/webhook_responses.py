import json

GET_XUNNEL_PROVIDERS = {
    'response': [{
        'name': 'Acme Bank-Normal',
        'provider_account_identifier': '5b2d85a00b212a1f1c8b456d',
        'provider_identifier': '56cf5728784806f72b8b4568'
    }, {
        'name': 'Acme-test-empty',
        'provider_account_identifier': '123456787890',
        'provider_identifier': '123456787890'
    }]
}

GET_XUNNEL_JOURNALS = {
    'response': [{
        'id_account': '5703f88223428348328b45db',
        'id_account_type': '520d3aa93b8e778e0d000000',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Checking',
        'number': '00000001',
        'balance': 1099,
        'currency': 'MXN',
        'account_type': 'Checking',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1521132979
    }, {
        'id_account': '5703f88323428348328b45eb',
        'id_account_type': '520d3aa93b8e778e0d000002',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Credit',
        'number': '00000011',
        'balance': 535,
        'currency': 'MXN',
        'account_type': 'Credit Card',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1521132979
    }, {
        'id_account': '5703f88323428348328b45f0',
        'id_account_type': '520d3aa93b8e778e0d000004',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Investment',
        'number': '00000021',
        'balance': 499,
        'currency': 'MXN',
        'account_type': 'Investment',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1521132979
    }, {
        'id_account': '57317925234283f1078b6837',
        'id_account_type': '520d3aa93b8e778e0d000002',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Credit',
        'number': '00000011',
        'balance': 535,
        'currency': 'MXN',
        'account_type': 'Credit Card',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1505421108
    }, {
        'id_account': '57317925234283f1078b6841',
        'id_account_type': '520d3aa93b8e778e0d000004',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Investment',
        'number': '00000021',
        'balance': 499,
        'currency': 'MXN',
        'account_type': 'Investment',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1505421108
    }, {
        'id_account': '57317925234283f1078b6843',
        'id_account_type': '520d3aa93b8e778e0d000000',
        'id_currency': '523a25953b8e77910e8b456c',
        'id_user': '5b2d858d0b212a631b8b4569',
        'id_external': '',
        'id_credential': '5b2d85a00b212a1f1c8b456d',
        'id_site': '56cf5728784806f72b8b4568',
        'id_site_organization': '56cf4ff5784806152c8b4567',
        'id_site_organization_type': '56cf4f5b784806cf028b4568',
        'is_disable': 0,
        'name': 'ACME Checking',
        'number': '00000001',
        'balance': 1099,
        'currency': 'MXN',
        'account_type': 'Checking',
        'site': {
            'id_site': '56cf5728784806f72b8b4568',
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'name': 'Normal',
            'organization': 'Acme Bank',
            'avatar': '/images/57310e530c212af6608b45f2/avatar',
            'cover': '/images/57310e530c212af6608b45f2/cover',
            'small_cover': '/images/57310e530c212af6608b45f2/small_cover',
            'time_zone': 'America/Mexico_City'
        },
        'extra': None,
        'keywords': None,
        'dt_refresh': 1505421108
    }]
}

GET_XUNNEL_TRANSACTIONS = {
    'response': json.dumps({
        'balance': 1099, 'transactions': [{
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412226000,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': 'azul',
            'description': 'ACME Checking Transaction 3',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1398920400,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 1,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '5703f88223428348328b45e0',
            'description': 'Fake Checking Transaction 5',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4569',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 15,
            'dt_deleted': None,
            'dt_refresh': 1491177097,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412312400,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '59bc5f9c2442836b028b4570',
            'description': 'ACME Checking Transaction 2',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412485200,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '59bc5f9c2442836b028b456e',
            'description': 'ACME Checking Transaction 1',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412226000,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 1,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '5703f88223428348328b45de',
            'description': 'Fake Checking Transaction 3',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4569',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1491177097,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412485200,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 1,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '5703f88223428348328b45dc',
            'description': 'Fake Checking Transaction 1',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4569',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1491177097,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412139600,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '59bc5f9c2442836b028b4574',
            'description': 'ACME Checking Transaction 4',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412312400,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 1,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '5703f88223428348328b45dd',
            'description': 'Fake Checking Transaction 2',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4569',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1491177097,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1412139600,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 1,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '5703f88223428348328b45df',
            'description': 'Fake Checking Transaction 4',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4569',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 10,
            'dt_deleted': None,
            'dt_refresh': 1491177097,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1398920400,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '59bc5f9c2442836b028b4576',
            'description': 'ACME Checking Transaction 5',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 15,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }, {
            'attachments': [],
            'reference': None,
            'extra': None,
            'currency': 'MXN',
            'keywords': None,
            'dt_transaction': 1398920400,
            'id_account': '5703f88223428348328b45db',
            'is_disable': 0,
            'id_credential': '5b2d85a00b212a1f1c8b456d',
            'id_currency': '523a25953b8e77910e8b456c',
            'id_transaction': '59bc5f9c2442836b028b4578',
            'description': 'ACME Checking Transaction 5',
            'id_external': '',
            'id_site_organization_type': '56cf4f5b784806cf028b4568',
            'id_user': '5b2d858d0b212a631b8b4569',
            'id_site': '56cf5728784806f72b8b4568',
            'is_deleted': 0,
            'id_site_organization': '56cf4ff5784806152c8b4567',
            'amount': 15,
            'dt_deleted': None,
            'dt_refresh': 1505517467,
            'id_account_type': '520d3aa93b8e778e0d000000',
            'dt_disable': None,
            'is_pending': 0,
        }]
    })
}
