#   -------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
# """RPC Package"""
# 协议定义如下:
# {
#     'method_name': name,
#     'method_args': args,
#     'method_kwargs': kwargs
# }

# 支持 延迟类型注解
from __future__ import annotations

__version__ = "0.0.2"

from rpc.client import RPCClient
from rpc.server import RPCServer

# test

# c = RPCClient()
# c.connect('127.0.0.1, 8000')
# res = c.test('测试项', kw1="1")
# print(res)

# def test(*args, **kwargs):
#   print(f"function test called with args: {args} and kwargs: {kwargs}")
#   return f"test called "
# s = RPCServer()
# s.register(test)
# s.loop('127.0.0.1', 8000)
