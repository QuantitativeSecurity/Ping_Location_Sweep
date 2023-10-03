import socket
import smtplib
from email.mime.text import MIMEText
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="ping_sweeper")

def get_location(host):
    try:
        location = geolocator.geocode(socket.gethostbyname(host))
        return location.latitude, location.longitude
    except Exception as e:
        print(f"Error retrieving location for {host}: {e}")
        return None

def ping(host):
    try:
        # Sends a maximum sized UDP packet to the host
        socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(b"x" * 65507, (host, 80))
        return True
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return False

def send_email(to, subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "ping_sweeper@example.com"
        msg['To'] = to

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("ping_sweeper@example.com", "your_password_here")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    hosts = []
    # Sweep your home network to find all IP addresses
    for i in range(1, 256):
        host = "X.X.X.X" + str(i)
        if ping(host):
            hosts.append(host)

    # Retrieve the location for each host that responded to the ping
    locations = [get_location(host) for host in hosts]
    # Compile the IP addresses and locations into lists
    ip_addresses = [f"{host}" for host in hosts]
    latitudes = [location[0] for location in locations if location is not None]
    longitudes = [location[1] for location in locations if location is not None]

    # Prepare the body of the email
    body = "IP Addresses:\n" + "\n".join(ip_addresses) + "\n\n"
    body += "Latitudes:\n" + "\n".join(str(lat) for lat in latitudes) + "\n\n"
    body += "Longitudes:\n" + "\n".join(str(long) for long in longitudes)

    # Send the email
    send_email("____________@gmail.com", "Sweep Results", body)
