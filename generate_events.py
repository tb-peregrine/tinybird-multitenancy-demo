import json
import random
from datetime import datetime
import time
import requests


def send_events(data, token, host):

    params = {
        'name': 'landing_datasource',
        'token': token,
        'host': host
    }

    r = requests.post(f'{host}/v0/events', params=params, data=data)
    print(data)


def create_events():

    tenant_ids = list(range(50))
    event_types = ['login', 'open', 'edit', 'save', 'delete', 'click', 'comment']
    responses = [200, 400, 500]
    response_weights = [95, 4, 1]

    with open ('./.tinyb') as tinyb:
        tb = json.load(tinyb)
        token = tb['token']
        host = tb['host']

    while True:
        events = []
        for i in range(10):
            message = {
                'timestamp': datetime.utcnow().isoformat(),
                'tenant_id': random.choice(tenant_ids),
                'event_type': random.choice(event_types),
                'response': random.choices(responses, response_weights)[0] 
            }
            events.append(message)
        data = '\n'.join(json.dumps(e) for e in events)
        send_events(data, token, host)
        time.sleep(0.1)

if __name__ == '__main__':
    create_events()