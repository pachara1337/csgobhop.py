import pymem
import win32api
import time

#fset

localp = 14423228
forcej = 86538508
health = 256
flags = 260

def bhop() -> None:
    pm = pymem.Pymem("csgo.exe")

    #getmodladrs

    for module in list(pm.list_modules()):
        if module.name == "client.dll":
            client = module.lpBaseOfDll

    #loop

    while True:
        time.sleep(0.01)

        #spbar

        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_p: int = pm.read_uint(client + localp)

        if not local_p:
            continue

        #alive

        if not pm.read_int(local_p + health):
            continue

        #ground

        if pm.read_uint(local_p + flags) & 1 << 0:
            pm.write_uint(client + forcej, 6)
            time.sleep(0.01)
            pm.write_uint(client + forcej,4)

if __name__ == "__main__":
    bhop()