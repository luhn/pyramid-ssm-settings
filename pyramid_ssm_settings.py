import boto3


def includeme(config):
    client = boto3.client('ssm')
    path = config.get_settings()['ssm.path']
    next_token = None
    settings = dict()
    while True:
        kwargs = {
            'Path': path,
            'WithDecryption': True,
        }
        if next_token:
            kwargs['NextToken'] = next_token
        response = client.get_parameters_by_path(**kwargs)
        for param in response['Parameters']:
            key = param['Name'][len(path):]
            settings[key] = param['Value']
        if 'NextToken' in response:
            next_token = response['NextToken']
        else:
            break
    config.add_settings(settings)
