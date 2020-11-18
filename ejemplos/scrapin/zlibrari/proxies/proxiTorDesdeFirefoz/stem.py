from stem import Signal
from stem.control import Controller

# signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)
