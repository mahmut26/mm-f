import os
def main():


        exec(open("kamera.py").read())

        restart = input("Do you want a new quote?").lower()

        if restart == "yes":
            main()

main()