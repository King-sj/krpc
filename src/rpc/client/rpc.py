from __future__ import annotations

__all__ = ['RPCClient']
import json

from .tcp import TCPClient


class RPCStub:
  def __getattr__(self, name):
    def wrapper(*args, **kwargs):
      data = json.dumps({
        'name': name,
        'args': args,
        'kwargs': kwargs
      })
      self.send(data)
      return json.loads(self.receive(1024))
    setattr(self, name, wrapper)
    return wrapper
class RPCClient(RPCStub, TCPClient):
  def __init__(self):
    RPCStub.__init__(self)
    TCPClient.__init__(self)
