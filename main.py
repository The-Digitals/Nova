import requests
from bs4 import BeautifulSoup

# Ορίζουμε το URL της ιστοσελίδας που θέλουμε να αναζητήσουμε
url = 'https://www.kathimerini.gr/'

# Ορίζουμε τη λέξη-κλειδί που θέλουμε να αναζητήσουμε
keyword = 'ΤΖΟΛΑΚΗΣ'

# Ανακτούμε την ιστοσελίδα
response = requests.get(url)

# Ελέγχουμε την επιτυχία του αιτήματος
if response.status_code == 200:
    # Χρησιμοποιούμε το BeautifulSoup για να αναλύσουμε τη σελίδα
    soup = BeautifulSoup(response.text, 'html.parser')

    # Αναζητούμε όλα τα κείμενα στη σελίδα
    text_elements = soup.find_all(string=True)

    # Ελέγχουμε κάθε κείμενο για την περιεκτικότητα της λέξης-κλειδιού
    for text in text_elements:
        if keyword in text:
            print("Η λέξη-κλειδί '{}' βρέθηκε!".format(keyword))
            break
    else:
        print("Η λέξη-κλειδί '{}' δεν βρέθηκε στη σελίδα.".format(keyword))
else:
    print("Αποτυχία ανάκτησης της ιστοσελίδας")