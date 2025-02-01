import os

def shutdown():
    confirmation = input("Are you sure you want to shut down the computer? (yes/no): ").strip().lower()
    if confirmation == "yes":
        os.system("shutdown /s /t 0")
    else:
        print("Shutdown canceled.")

shutdown()
