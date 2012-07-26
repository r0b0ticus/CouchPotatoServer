from .main import BaconBits

def start():
    return BaconBits()

config = [{
    'name': 'baconbits',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'providers',
            'name': 'BaconBits',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
            ],
        },
    ],
}]
