import os
import subprocess

def main():
    print("Zipwn")
    archive = input("Enter Archive: ").strip()
    if not os.path.exists(archive):
        print("Archive not found!")
        input("Press Enter to exit...")
        return

    wordlist = input("Enter Wordlist: ").strip()
    if not os.path.exists(wordlist):
        print("Wordlist not found!")
        input("Press Enter to exit...")
        return

    print("Cracking...")
    attempt_num = 1
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            if attempt(password, archive, attempt_num):
                print(f"Success! Password Found: {password}")
                input("Press Enter to exit...")
                return
            attempt_num += 1
    print("shitty wordlist dumbass")
    input("Press Enter to exit...")

def attempt(password, archive, attempt_num):
    process = subprocess.Popen(['C:\\Program Files\\7-Zip\\7z.exe', 'x', '-p'+password, archive, '-o', 'cracked', '-y'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"Attempt {attempt_num}: {password}")
    return process.returncode == 0

if __name__ == "__main__":
    main()
