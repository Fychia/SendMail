import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd

def send_email(to_address, subject, body):
    from_address = "" # Insert the email address
    password = "" # Insert the email password

    # Set up the SMTP server
    server = smtplib.SMTP('', ) # Insert the SMTP server address and port
    server.starttls()
    server.login(from_address, password)

    # Create message
    msg = MIMEMultipart('related')
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Create email body part
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    # Attach email body
    msg_text = MIMEText(body, 'html')
    msg_alternative.attach(msg_text)

    # Attach embedded image
    with open(image_path, 'rb') as img:
        mime_image = MIMEImage(img.read())
        mime_image.add_header('Content-ID', '<image>')
        mime_image.add_header('Content-Disposition', 'inline', filename='signature.png')
        msg.attach(mime_image)

    # Send email
    server.send_message(msg)
    server.quit()

# Read CSV file
try:
    df = pd.read_csv(r'E:\WorkSpace\SendMail\csv\emails.csv') # Insert the .csv file path
    
    # Check if 'email' and 'name' columns exist
    if 'email' not in df.columns or 'nome' not in df.columns:
        raise KeyError("The CSV file must contain the columns 'email' and 'name'.")
except FileNotFoundError:
    print("Error: The 'CSV' file was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The 'CSV' file is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: The 'CSV' file is poorly formatted.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

clients = df.to_dict(orient='records')

# Image Path 
image_path = r'E:\WorkSpace\SendMail\imgs\ass.png'

# Send emails individually
for client in clients:
    email = client["email"]
    nome = client["nome"]
    subject = "" # Fill in the email subject
    
    
    # Describe the email body
    body = f"""
    <p style="font-size: 15px;">Hello {nome}, how are you?</p>

    <p style="font-size: 15px;">My name is [], and I'm from Wetok Software.</p>
    <p style="font-size: 15px;">I'm contacting you to discuss [].</p>
    <p style="font-size: 15px;">We have a feature within [] that [], .....</p>
    <p style="font-size: 15px;">To use this feature, I would like to know:</p>

    <ul>
        <li style="font-size: 15px;">Who is responsible for the...</li>
        <li style="font-size: 15px;">What is the responsible person's email?</li>
        <li style="font-size: 15px;">What would be the phone number?</li>
    </ul>
    
    <p style="font-size: 15px;">Thank you in advance.</p>
    
    <img src="cid:image" width="250px">
    <img src="https://i.imgur.com/GW90sq5.png" width="250px">
    """
    send_email(email, subject, body, image_path)
    print(f"Email sent to {email}")
