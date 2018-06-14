from optimus.transformer import transform


def test_string_literal(purchase_order_data, purchase_order_schema):
    pos = purchase_order_schema

    # Add a new field `foo` with default value `bar`
    pos['properties']['foo'] = {
        'type': 'function',
        'source': ['string_literal', [], ['bar']]
    }

    transformed_data = transform(
        purchase_order_data,
        purchase_order_schema
    )

    assert purchase_order_data != transformed_data
    assert 'foo' in transformed_data
    assert transformed_data['foo'] == 'bar'


def test_default_value_when_source_is_empty(
        purchase_order_data, purchase_order_schema):
    pos = purchase_order_schema

    # Add a default value for comment
    pos['properties']['comment'] = {
        'type': 'function',
        'source': ['default_value', ['comment'], ['no comment']]
    }

    transformed_data = transform(
        purchase_order_data,
        purchase_order_schema
    )

    assert purchase_order_data != transformed_data
    assert transformed_data['comment'] == 'no comment'


def test_default_value_when_source_is_filled(
        purchase_order_data, purchase_order_schema):
    pos = purchase_order_schema

    # Add a default value for comment
    pos['properties']['comment'] = {
        'type': 'function',
        'source': ['default_value', ['comment'], ['no comment']]
    }

    purchase_order_data['comment'] = 'some comment'

    transformed_data = transform(
        purchase_order_data,
        purchase_order_schema
    )

    assert transformed_data['comment'] != 'no comment'
    assert transformed_data['comment'] == 'some comment'


def test_format_date(purchase_order_data, purchase_order_schema):
    pos = purchase_order_schema

    # Format date in DD-MM-YYYY (02-06-2018)
    pos['properties']['date'] = {
        'type': 'function',
        'source': ['format_date', ['date'], ['DD-MM-YYYY']]
    }

    transformed_data = transform(
        purchase_order_data,
        purchase_order_schema
    )

    assert purchase_order_data != transformed_data
    assert transformed_data['date'] == '02-06-2018'
