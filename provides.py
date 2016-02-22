from charms.reactive import RelationBase
from charms.reactive import scopes
from charms.reactive import hook


class RebacaProvider(RelationBase):
    ''' Idempotent method to deal with data for the relationship.
        You should only be communicating with the remote application
        in this class. Actions that need to be taken on the host
        are written in decorated methods'''

    # Define a service level communication scope.
    scope = scopes.SERVICE

    auto_accessors=['private-address', 'client']

@hook('{provides:rebaca}-relation-{joined,changed}')
def joined_and_changed(self):
    '''
    Implement this behavior like so:

    `metadata.yaml`
    provides:
      server:
         interface: rebaca

    `reactive/module.py`
    @when('server.connected')
    def do_something(server):
        print(server.private_address())

    '''
    self.set_state('{relation_name}.connected')



@hook('{provides:rebaca}-relation-{broken,departed}')
def broken_and_departed(self):
    '''
Implement this behavior like so:

    `metadata.yaml`
    provides:
      server:
         interface: rebaca

    `reactive/module.py`
    @when_not('server.connected')
    def cleanup(server):
        # do something here to cleanup after the connection is broken
    '''
    self.remove_state('{relation_name}.connected')
    pass
