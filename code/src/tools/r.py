#!/usr/local/bin/python
# reader.py
import os
import select
import time
#from message import decode_msg_size
from emtec.ipc import *

def check_poll(fifor,fifow,poll,timeout,counter):
    # Check if there's data to read. Timeout after 2 sec.
    if (fifor, select.POLLIN) in poll.poll(timeout*1000):
    # Do something with the message
        print('size:',os.stat(IPC_FIFO_NAME).st_size)
        msg = get_message(fifor)
        print(counter,msg,len(msg))
        """
        if len(msg):
            content = f"Bye {msg}!".encode("utf8")
            msg = create_msg(content)
            os.write(fifow, msg)
        """
    else:
        # No data, do something else
        print(counter,"Nobody here :(")
        content = f"Counter {counter}!".encode("utf8")
        msg = create_msg(content)
        os.write(fifow, msg)

def check_pipe(fifor,fifow,poll,timeout,counter):
    # Do something with the message
    try:
        msg = get_message(fifor)
        print(f"{counter}: {msg} {len(msg)}")
        """
        if len(msg):
            content = f"Bye {msg}!".encode("utf8")
            msg = create_msg(content)
            os.write(fifow, msg)
        """
        if len(msg) == 0:
            # No data, do something else
            print(counter,"Nobody here :(")
            content = f"Counter {counter}!".encode("utf8")
            msg = create_msg(content)
            os.write(fifow, msg)
    except Exception as e:
        if e.errno == 11:
            print(f"{counter}: Nobody here :(")
        else:
            print(f"{counter}: {e}")

if __name__ == "__main__":
    # Make the named pipe and poll for new messages.
    IPC_FIFO_NAME = "FIFO.fifo"
    try:
        try:
            os.remove(IPC_FIFO_NAME)
        except:
            pass
        os.mkfifo(IPC_FIFO_NAME)
    except Exception as e:
        print(f"{IPC_FIFO_NAME} {e}")
    try:
        # Open the pipe in non-blocking mode for reading
        fifo  = os.open(IPC_FIFO_NAME, os.O_RDONLY | os.O_NONBLOCK)
        fifow = os.open(IPC_FIFO_NAME, os.O_WRONLY)
        print(f"namedpipe={IPC_FIFO_NAME} {os.stat(IPC_FIFO_NAME)}")
        print(f"fifor={fifo } ({id(fifo) })")
        print(f"fifow={fifow} ({id(fifow)})")
        try:
            # Create a polling object to monitor the pipe for new data
            poll = select.poll()
            poll.register(fifo, select.POLLIN)
            counter=0
            try:
                timeout=5
                while True:
                    counter+=1
                    #heck_poll(fifo,fifow,poll,timeout,counter)
                    check_pipe(fifo,fifow,poll,timeout,counter)
                    time.sleep(1)
                    """
                    # Check if there's data to read. Timeout after 2 sec.
                    if (fifo, select.POLLIN) in poll.poll(5000):
                    # Do something with the message
                        print('size:',os.stat(IPC_FIFO_NAME).st_size)
                        msg = get_message(fifo)
                        print(counter,msg,len(msg))
                        '''
                        if len(msg):
                            content = f"Bye {msg}!".encode("utf8")
                            msg = create_msg(content)
                            os.write(fifow, msg)
                        '''
                    else:
                        # No data, do something else
                        print(counter,"Nobody here :(")
                        content = f"Counter {counter}!".encode("utf8")
                        msg = create_msg(content)
                        os.write(fifow, msg)
                    """
            except KeyboardInterrupt:
                print(f"\rInterrupted by user")
                pass
            except Exception as e:
                print(f"{e}")
            finally:
                poll.unregister(fifo)
        finally:
            os.close(fifo)
    finally:
        # Delete the named pipe when the reader terminates
        try:
            os.remove(IPC_FIFO_NAME)
        except:
            print(f"{IPC_FIFO_NAME} does not exist.")
        finally:
            print("Completed")
