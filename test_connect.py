import os
import time
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("host")
PASSWORD = os.getenv("password")


def test_reboot(ssh_connect):
    stdin, stdout, stderr = ssh_connect.exec_command("sudo -S -p '' reboot")
    stdin.write(f"{PASSWORD}\n")
    stdin.flush()
    # Опрашиваем сервер в течении 45 секунд после команды на перезагрузку:
    time.sleep(5)
    timer = time.time() + 40
    while time.time() < timer:
        response = os.system(f"ping -n 1 {HOST}")
        if response == 0:
            break
    else:
        raise AssertionError('Host is down')
