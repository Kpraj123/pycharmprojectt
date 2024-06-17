import smtplib

# Update your correct email address and password
my_email = "prajakatakatikar@gmail.com"
# If you have 2FA enabled, use app password generated from Google Account settings
passw = ""

# Connect to Gmail's SMTP server
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()

# Login using your email and app password
connection.login(user=my_email, password=passw)

# Send the email
connection.sendmail(from_addr=my_email, to_addrs="pradnyakatikar123@gmail.com", msg="Hello")

# Close the connection
connection.close()