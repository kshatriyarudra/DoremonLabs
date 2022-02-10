import csv, smtplib, ssl

message = """Subject: Completion of Tasks.
Hello {},


Total number of documents in given range of time is- {}
Total number of documents in given range of response time is- {}

Thanks and Regards
Rudra Pratap Singh"""
from_address = "rudra931592@gmail.com"
password = "#####"

context = ssl.create_default_context()
def send(count_of_timestamp,count_of_response_time):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, password)
        with open("email_ids.csv") as file:
            reader = csv.reader(file)
            next(reader) 
            for name, email in reader:
                server.sendmail(
                    from_address,
                    email,
                    message.format(name,count_of_timestamp,count_of_response_time),
                )
                print("email send to {}".format(name))