import pytest
import paramiko
from dotenv import load_dotenv
import os


load_dotenv()
HOST = os.getenv("host")
USERNAME = os.getenv("ssh_username")
PASSWORD = os.getenv("password")


@pytest.fixture()
def ssh_connect():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, username=USERNAME, password=PASSWORD, port=22)
    except OSError:
        raise AssertionError('Can`t connect')
    yield(ssh)
    ssh.close()
