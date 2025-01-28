from __future__ import annotations

import socket


class TCPServer:
  def __init__(self):
    self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def bind(self, host='localhost', port=8000, listen_count=5):
    '''
    Bind the server to the host and port
    '''
    self._socket.bind((host, port))

    self._socket.listen(listen_count)

  def accept_receive_close(self, length=1024):
    '''
    Accept a connection, receive data, and close the connection
    '''
    conn, addr = self._socket.accept()
    r = conn.recv(length)
    data = self.process_request(r) # type: ignore
    conn.sendall(data.encode('utf-8'))
    conn.close()
    return data
