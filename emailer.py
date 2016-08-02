import weather
import smtp

'''
Send a greeting email to our customer email list
with the daily weather forecast and schedule
'''

def get_emails():
    # Reading emails from a file
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
            
    except FileNotFoundError as err:
        print(err)

    return emails


def get_schedule():
    # Reading our schedule from a file
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
        
    return schedule


def main():
    # Get our dictionary of customer emails and names
    emails = get_emails()
    
    # Get our daily performance schedule
    schedule = get_schedule()
    
    # Get the current weather forecast
    forecast = weather.get_weather_forecast()

    # Send emails to all of our customers with our forecast and schedule
    smtp.send_emails(emails, schedule, forecast)


main()
