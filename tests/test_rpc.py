from __future__ import annotations

import pytest

from rpc import RPCClient, RPCServer


def test_rpc_client_server(unit_test_mocks: None):
  server = RPCServer()
  def test(*args, **kwargs):
    print(f"function test called with args: {args} and kwargs: {kwargs}")
    return f"test called "
  server.register_function(test)

  import threading
  server_thread = threading.Thread(target=server.loop, args=('127.0.0.1', 8000), daemon=True)
  server_thread.start()

  client = RPCClient()
  client.connect('127.0.0.1', 8000)

  res = client.test('测试项', kw1="1")
  assert res['res'] == 'test called '

  server.stop()
  server_thread.join()
if __name__ == "__main__":
  pytest.main()
