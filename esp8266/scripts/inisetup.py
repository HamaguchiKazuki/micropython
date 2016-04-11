import uos
import network
from flashbdev import bdev

def wifi():
    import ubinascii
    ap_if = network.WLAN(network.AP_IF)
    ap_if.config(essid=b"MicroPython %s" % ubinascii.hexlify(ap_if.mac()[-3:]))

def check_bootsec():
    buf = bytearray(bdev.SEC_SIZE)
    bdev.readblocks(0, buf)
    empty = True
    for b in buf:
        if b != 0xff:
            empty = False
            break
    if empty:
        return True
    fs_corrupted()

def fs_corrupted():
    import time
    while 1:
        print("""\
FAT filesystem appears to be corrupted. If you had important data there, you
may want to make a flash snapshot to try to recover it. Otherwise, perform
factory reprogramming of MicroPython firmware (completely erase flash, followed
by firmware programming).
""")
        time.sleep(3)
