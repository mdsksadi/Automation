from dataclasses import dataclass


@dataclass
class MailItem:
    uid: str
    from_: str
    subject: str
    date: str