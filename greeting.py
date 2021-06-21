from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning' + name + '-san!'
    elif hour <= 17:
        message = 'Good evening' + name + '-san!'
        
    else:
        message = 'Hello'
    print(message)

greet('Inoue')