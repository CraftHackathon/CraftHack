import requests

def create_dummy_emails():
    response = requests.post("http://192.168.203.49:8000/email-populate/")
    emails = [
        {
            'email_address': 'support@microsoft.com',
            'email_body': 'Dear user, we have detected a security vulnerability in your Windows operating system. Please install the latest security update by visiting example.com/update.',
            'is_scam': True
        },
        {
            'email_address': 'security@yourbank.com',
            'email_body': 'Dear customer, your account has been locked due to a suspected unauthorized login attempt. Please reset your password immediately to secure your account.',
            'is_scam': True
        },
        {
            'email_address': 'newsletter@fashionstore.com',
            'email_body': 'Hello, check out our latest collection for the upcoming season. Visit our website to browse the trendy fashion items and enjoy exclusive discounts.',
            'is_scam': False
        },
        {
            'email_address': 'support@socialmedia.com',
            'email_body': 'Hi there, we noticed some unusual activity on your social media account. To secure your account, please review your recent login activity and update your password.',
            'is_scam': True
        },
        {
            'email_address': 'info@youruniversity.edu',
            'email_body': 'Dear student, please note that the deadline to submit your course registration is approaching. Log in to your student portal and complete your registration as soon as possible.',
            'is_scam': False
        },
    ]



# Call the function to create the additional dummy emails
create_dummy_emails()
