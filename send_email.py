def send_email(code):
    '''
    This function sends an email to a user, that has a verification link!
    '''
    
    link = "google.ca"
    fromaddr = "r_asif_11@hotmail"  #the email youre sending the email from
    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = "r_asif_11@hotmail" #the address you want to send an email to
    msg['Subject'] = "A random email"
    html = """
        \
    <html>
    <head></head>
    <body>
     <p>This is an automated e-mail<br>
       Here is a <a href=""" + link  +""">link</a> for a search engine<br>
       Rabia Asif :) <br>
       Below is a picture of a kitten! :P
    </p>
        <img src="https://www.thesprucepets.com/thmb/810a_HYIb2E8DxkedI6V-3gtkys=/450x0/filters:no_upscale():max_bytes(150000):strip_icc()/kitten-looking-at-camera-521981437-57d840213df78c583374be3b.jpg" width="166.5px" height="44.5px">
    </body>
    </html>
    """
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = smtplib.SMTP('smtp.live.com',587)
    server.starttls()
    server.login(fromaddr, "MY_PASSWORD_HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()