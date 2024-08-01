## About the Project

This solution was developed to address a problem reported by the support team, who found it labor-intensive to manually inform clients of new features via email. The project's goal is to automate the creation and sending of these emails, streamlining the process and reducing manual effort.
Features

- Automatic Email Creation: Generates emails containing information about new features.
- Bulk Sending: Automatically sends emails to a list of clients.

## Technologies Used

The following technologies were used to develop this solution:

- SMTP (Simple Mail Transfer Protocol): Used for sending emails.
        Library: smtplib

- MIME (Multipurpose Internet Mail Extensions): Used to create and structure email messages with multiple types of content, such as text and images.
        Libraries:
            email.mime.multipart.MIMEMultipart
            email.mime.text.MIMEText
            email.mime.image.MIMEImage

- Pandas: Data analysis library used for data manipulation and reading, in this case, to read and process the CSV file containing client data.
        Library: pandas
