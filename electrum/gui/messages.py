# note: qt and kivy use different i18n methods

MSG_RECOVERABLE_CHANNELS = """
Add extra data to your channel funding transactions, so that a static backup can be recovered from your seed.

Note that static backups only allow you to request a force-close with the remote node. This assumes that the remote node is still online, did not lose its data, and accepts to force close the channel.

If this is enabled, other nodes cannot open a channel to you. Channel recovery data is encrypted, so that only your wallet can decrypt it. However, blockchain analysis will be able to tell that the transaction was probably created by Electrum.
"""

MSG_REQUEST_FORCE_CLOSE = """If you choose to request force-close, your node will pretend that it has lost its data and ask the remote node to broadcast their latest state. Doing so from time to time helps make sure that nodes are honest, because your node can punish them if they broadcast a revoked state."""
