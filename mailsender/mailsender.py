import smtplib
import ssl
from email.mime.text import MIMEText
from typing import List
from typing_extensions import Literal


class MailSender:
    def __init__(
        self,
        host: str,
        port: int,
        protocol: Literal["SSL", "TLS"],
        user: str,
        password: str,
    ) -> None:
        self.host = host
        self.port = port
        self.protocol = protocol
        self.user = user
        self.password = password

    def send(self, sender: str, targets: List[str], subject: str, body: str) -> None:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = ", ".join(targets)

        server = smtplib.SMTP(self.host, self.port)
        if self.protocol == "TLS":
            context = ssl.create_default_context()
            server.starttls()
        elif self.protocl == "SSL":
            pass  # ToDo

        server.login(self.user, self.password)
        server.sendmail(sender, targets, message.as_string())
        server.quit()
