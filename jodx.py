import os, time, sys, pyfiglet, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Colors
R, G, W = "\033[1;31m", "\033[1;32m", "\033[0m"

def lock_screen():
    os.system('clear')
    print(R + pyfiglet.figlet_format("JODX", font="slant"))
    print(f"      {R}[ BY JODX ]{W}\n")
    print(f"{R}THIS TOOL IS LOCKED. REDIRECTING YOU TO INSTAGRAM PAGE...{W}")
    print(f"{R}LIKE, FOLLOW UNLOCK THE TOOL{W}\n")
    for i in range(9, -1, -1):
        sys.stdout.write(f"\r{R}Redirecting in {i} seconds...{W}")
        sys.stdout.flush()
        time.sleep(1)
    os.system("am start -a android.intent.action.VIEW -d 'https://www.instagram.com/cybersecurity_expert1551?igsh=MThuZ3BhOXE5ZjZtOQ==/@TEAM_X_termux?si=EJzW66FcfcYwGcQv'")
    input(f"\n\n{G}[+] Hit Enter after following...{W}")

def encrypt_msg(msg, password):
    # AES sync ke liye PBKDF2 key derivation
    key = PBKDF2(password, b'salt', dkLen=32, count=10000)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(msg.encode(), 16))
    return base64.b64encode(iv + encrypted).decode()

def main():
    lock_screen()
    while True:
        os.system('clear')
        print(f"{R}{pyfiglet.figlet_format('jodx MENU')}{W}")
        print(f"1. Hide Message (Generate Link)\n2. Exit")
        choice = input(f"\n{G}jodx >> {W}")
        if choice == '1':
            msg = input(f"{G}Type message: {W}")
            pwd = input(f"{G}Set password: {W}")
            enc_data = encrypt_msg(msg, pwd)
            # Yahan apna GitHub Pages link dalo
            link = f"https://hackerscolonyofficial.github.io/HCO-Steganography/#data={enc_data}"
            print(f"\n{G}[+] LINK GENERATED:\n{link}\n{R}KEY: {pwd}{W}")
            input(f"\n{G}Press Enter...{W}")
        else: break

if __name__ == "__main__":
    main()