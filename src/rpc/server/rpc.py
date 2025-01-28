from __future__ import annotations

__all__ = ['RPCServer']
import json

from .tcp import TCPServer


class RPCStub:
  def __init__(self):
    self.functions = {}

  def register_function(self, fn, name=None):
    '''
    Register a function with the RPC server
    '''
    if name is None:
      name = fn.__name__
    self.functions[name] = fn

class JSONRPC:
  def __init__(self):
    self.data = None

  def from_json(self, data):
    '''
    Load JSON data
    '''
    self.data = json.loads(data.decode('utf-8'))

  def call_method(self):
    '''
    Call the method and return the result
    '''
    fn = self.data['name'] # type: ignore
    args = self.data['args'] # type: ignore
    kwargs = self.data['kwargs'] # type: ignore

    if fn in self.functions: # type: ignore
      res = self.functions[fn](*args, **kwargs) # type: ignore
    else:
      res = f'Function {fn} not found'
    data = {
      'res': res
    }
    return json.dumps(data)

class RPCServer(TCPServer, JSONRPC, RPCStub):
  def __init__(self):
    TCPServer.__init__(self)
    JSONRPC.__init__(self)
    RPCStub.__init__(self)
    self.isStopped = False

  def process_request(self, data):
    '''
    Process the request
    '''
    # dat
    self.from_json(data)
    return self.call_method()

  def loop(self, host='0.0.0.0', port=8000):
    '''
    Start the server
    '''
    self.bind(host, port)
    print(f'Server listening on {host}:{port}')
    while not self.isStopped:
      self.accept_receive_close()
  def stop(self):
    '''
    Stop the server
    '''
    self.isStopped = True
    self._socket.close()
