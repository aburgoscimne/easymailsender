# Easy Mail Sender
A simple mail sender.

## Usage
```python
from easymailsender.easymailsender import EasyMailSender

ems = EasyMailSender("<SMTP Server>", "<SMTP Port>", "<SSL or TLS>", "<User>", "<Password>")

ems.send(
    "<Sender e-mail>",
    ["<Recipients e-mail>"],
    "<Subject>",
    "<Message body>",
    "<Path to attachment>"
)