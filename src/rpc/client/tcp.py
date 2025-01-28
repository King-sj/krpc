from __future__ import annotations

__all__ = ['TCPClient']
import socket


class TCPClient:
  def __init__(self):
    self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  def connect(self, host='localhost', port=8000):
    '''
    Connect to the server
    '''
    self._socket.connect((host, port))

  def send(self, data):
    '''
    Send data to the server
    '''
    self._socket.sendall(data.encode('utf-8'))

  def receive(self, length):
    '''
    Receive data from the server
    '''
    return self._socket.recv(length).decode('utf-8')
