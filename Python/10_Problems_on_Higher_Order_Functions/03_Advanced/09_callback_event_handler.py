def send_email():
    print("send_email executed")

def write_log():
    print("write_log executed")

def register_event(callbacks):
    for callback in callbacks:
        callback()

callbacks = [send_email, write_log]

register_event(callbacks)
