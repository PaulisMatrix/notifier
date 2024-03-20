class Processors:
    def __init__(self) -> None:
        pass

    def send_toemail(self, event_payload: dict):
        print("got the event payload: ", event_payload)

    def send_towhatsapp(self, event_payload: dict):
        pass

    def send_tophone(self, event_payload: dict):
        pass
