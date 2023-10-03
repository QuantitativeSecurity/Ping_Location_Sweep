Ping Sweeper and Location Retriever

This program performs a ping sweep on a specified range of IP addresses in your home network, retrieves the geographic locations of the hosts that respond to the ping, and sends an email with the list of IP addresses and their respective locations.
Dependencies

    Python 3.x
    socket, smtplib, and email libraries (Included with Python)
    geopy library

You can install the geopy library using pip:

bash

pip install geopy

Usage

    Copy the code from the program and save it into a file named ping_sweeper.py.
    Update the following placeholders in the code:
        Replace "your_password_here" with the password for your email account.
        Replace "____________@gmail.com" with the recipient's email address.
        Replace "X.X.X." with the first three octets of your IP address range.
    Execute the program by running the following command in your terminal:

bash

python ping_sweeper.py

Program Overview

The program performs the following steps:

    Importing Necessary Libraries:
    The required libraries are imported for network communication, email composition, and geographic location retrieval.

    Initializing Geolocator:
    A Nominatim geolocator object is created with a user agent of "ping_sweeper".

    Defining Functions:
        get_location(host): Retrieves the geographic location of a host.
        ping(host): Sends a ping to a host.
        send_email(to, subject, body): Composes and sends an email.

    Main Execution:
        A loop iterates through a range of IP addresses and pings each host.
        For each host that responds, its IP address is stored.
        The geographic location of each responsive host is retrieved.
        Lists of IP addresses, latitudes, and longitudes are compiled.
        An email body is composed with the IP addresses and locations.
        The email is sent to the specified recipient.

Output

Check the inbox of the specified recipient email address for an email with the subject "Sweep Results". The email will contain a list of IP addresses, latitudes, and longitudes of the hosts that responded to the ping.
