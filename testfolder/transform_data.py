#def transform_data(finfire_data):
#    method 1
#    return [{'field1': record['field1'], 'field2': record['field2']} for record in finfire_data]
def transform_data(finfire_data):
    """
    Transform the Finfire data into a desired format.

    Args:
        finfire_data (list): The original Finfire data to be transformed.

    Returns:
        list: The transformed data.
    """
    transformed_data = []
    for record in finfire_data:
        transformed_record = {
            'field1': record.get('field1'),
            'field2': record.get('field2')
        }
        transformed_data.append(transformed_record)
    return transformed_data