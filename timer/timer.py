try:
    from plyer import notification
    import time
except ModuleNotFoundError:
    print("please install the required modules with: \npy -m pip install -r ./timer/requirements.txt")
    exit(1)


def getseconds() -> int:
    userin = input("How many seconds do you want ? (default: 30) : ")
    if userin == "":
        return 30
    if userin.isnumeric():
        return int(userin)
    else:
        print(f"{userin} is not a number.")
        return getseconds()


if __name__ == "__main__":
    sec = getseconds()

    for i in range(0, sec):
        time.sleep(1)
        print("\r", end="")
        print(f"countdown : {i+1} / {sec}", end="")
    # send notif
    notification.notify(
        title='Timer.py',
        message=f"Your {sec} second timer has ended !",
        app_icon=None,
        timeout=1
    )
