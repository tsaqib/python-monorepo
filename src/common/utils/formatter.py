import os, socket


def get_host_ip():
    return socket.gethostbyname(socket.getfqdn())


def fmt_message(svc_name, message):
    return f"[{svc_name}:{os.getpid()} @ {get_host_ip()}] => {message}"
