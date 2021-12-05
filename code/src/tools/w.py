#!/usr/local/bin/python3
# writer.py
import os
#from message import create_msg
from emtec.ipc import *

if __name__ == "__main__":
    IPC_FIFO_NAME = "FIFO.fifo"

    fifo = os.open(IPC_FIFO_NAME, os.O_WRONLY)
    print(f"namedpipe={IPC_FIFO_NAME} fifo={fifo} ({id(fifo)})")
    try:
        while True:
            name = input("Enter a name: ")
            content = f"Hello {name}!".encode("utf8")
            msg = create_msg(content)
            os.write(fifo, msg)
    except KeyboardInterrupt:
        print("\nGoodbye!")
    finally:
        os.close(fifo)
