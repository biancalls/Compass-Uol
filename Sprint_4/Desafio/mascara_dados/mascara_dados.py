import hashlib

def main():
    while True:
        string = input(f"Digite algo: ")
        sha1 = hashlib.sha1(string.enconde("utf-8")).hexdigest()
        print(f"SHA-1:{sha1}")

if __name__=="__main__":
    main()


        