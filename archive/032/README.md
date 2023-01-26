# 32 - Email & Dates

### Topics Covered

* Sending Email with Python and SMTP

* Working with date and time

* Hosting Python Code Online with PythonAnywhere


### Notes

* **SMTP** - Simple Mail Transfer Protocol
  * A protocol for sending emails over the internet 
  * SMTP is a client-server protocol, which means that there are two programs involved in the process of sending an email
    * The client is the program that you use to write and send your email
    * The server is the program that receives your email and delivers it to the recipient's email server

### Syntax - SMTP

- `IMPORT LIBRARY & CONFIG`

```python
import smtplib

# CONFIG
my_email = "thisispratikkabade@gmail.com"
my_password = "frpxqlelhhzcbykj"
to_mail = "pratik.kabade@outlook.com"
smtp = "smtp.gmail.com"
```

- `CONNECTION`
```python
connection = smtplib.SMTP(smtp")
```

- `SECURE THE CONNECTION`
```python
connection.starttls()
```


- `SEND MAIL`
```python
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email,
                    to_addrs=to_mail, msg="Subject:Hello\n\nBody")
connection.close()
```




### Materials

* [Python File - birthday-email](./032.py)
* [Python File - email-syntax--email-random-quote](./bin/email.py)

---

**[Home](../README.md)**