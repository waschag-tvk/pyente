import requests


class Client:
    def __init__(self, enteapi_url='http://localhost', ente_id=1):
        self.appointment_url = enteapi_url + '/enteapi/v1/appointment/'
        self.token_auth_url = enteapi_url + '/enteapi/token-auth/'
        self.last_used_for_each_machine_url = (
                self.appointment_url + 'last_used_for_each_machine/')
        self.ente_id = ente_id

    def get_available_appointments(self):
        return requests.get(self.appointment_url).json()

    def get_last_used_for_each_machine(self):
        '''see the latest actual users for each machine'''
        return requests.get(self.last_used_for_each_machine_url)

    def get_authenticated_session(self, username, password):
        token = requests.post(
                self.token_auth_url,
                json={'username': username, 'password': password},
                ).json()['token']
        return AuthenticatedSession(self, token)

    def activate(self, token, machine):
        appointment = list(filter(
                lambda a: a['machine'] == machine,
                get_available_appointments()))
        if len(appointment) != 1:
            raise RuntimeError(
                    'Appointment for the machine not available or ambiguous!')
        appointment_pk = appointment[0]['pk']
        requests.post(
                self.appointment_url + '{:d}/activate/'.format(appointment_pk),
                json={"enteId": self.ente_id},
                headers={'Authorization': 'JWT ' + token})


class AuthenticatedSession:
    def __init__(self, client, token):
        self.client = client
        self.token = token

    def activate(self, machine):
        self.client.activate(self.token, machine)
