# RPC 项目

这是一个基于TCP协议的RPC（远程过程调用）项目，包含客户端和服务器端的实现。该项目允许客户端通过网络调用服务器上的函数。 ![alt text](images/架构图.png)

## 项目结构

- `src/`

  - `rpc/`

    - `__init__.py`: 包含RPC客户端和服务器端的初始化代码。
    - `client.py`: 包含RPC客户端的实现。
    - `server.py`: 包含RPC服务器端的实现。
    - `tcp.py`: 包含TCP客户端和服务器端的实现。

  - `tests/`

    - `test_rpc.py`: 包含针对RPC客户端和服务器端的测试代码。

## 安装

### 使用

```sh
pip install ksj-rpc
```
### 参与开发

1\. 克隆代码库：

````
```sh
git clone https://github.com/King-sj/krpc.git
cd krpc
```
````

1. 安装依赖项：

  ```sh
  pip install -r requirements.txt
  ```

# 使用方法

## 启动服务器

在服务器端，创建一个RPC服务器并注册要暴露的函数：

```python
from rpc.server import RPCServer

def test_function(*args, **kwargs):
    return f"function test called with args: {args} and kwargs: {kwargs}"

server = RPCServer()
server.register(test_function)
server.loop('127.0.0.1', 8000)
```

## 启动客户端

在客户端，创建一个RPC客户端并连接到服务器：

```python
from rpc.client import RPCClient

client = RPCClient()
client.connect('127.0.0.1', 8000)
result = client.test_function('测试项', kw1="1")
print(result)  # 输出: function test called with args: ('测试项',) and kwargs: {'kw1': '1'}
```

# 测试

使用`pytest`运行测试：

```sh
pytest tests/test_rpc.py
```

# 开发

## 依赖项

项目依赖项在`pyproject.toml`文件中定义。使用以下命令安装开发依赖项：

```sh
pip install flit
flit install --deps develop
```

## 代码风格

使用`flake8`和`black`检查代码风格：

```sh
flake8 src/
black src/
```

## 类型检查

使用`pyright`进行类型检查：

```sh
pyright src/
```

# 贡献

欢迎贡献和建议！请提交拉取请求或报告问题。
