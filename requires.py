from charms.reactive import RelationBase
from charms.reactive import scopes
from charms.reactive import hook

from charmhelpers.core.hookenv import unit_get


class RebacaClient(RelationBase):
    ''' Idempotent method to deal with data for the relationship.
        You should only be communicating with the remote application
        in this class. Actions that need to be taken on the host
        are written in decorated methods'''

    scope = scopes.SERVICE
    auto_accessors=['private-address', 'client']

@hook('{provides:rebaca}-relation-{joined,changed}')
def joined_and_changed(self, logdir="", cucumber_file=""):
    self.state('{relation_name}.connected')
    conv = self.conversation()
    conv.set_remote(data={'client': unit_get('public-address')})

@hook('{provides:rebaca}-relation-{broken,departed}')
def broken_and_departed(self):
    self.remove_state('{relation_name}.connected')
    pass
