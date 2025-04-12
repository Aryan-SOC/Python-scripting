# Dictionary of 100 most commonly used port numbers and their associated services
port_services = {
    20: "FTP (Data Transfer)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft-DS",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    520: "RIP",
    587: "SMTP (Mail Submission)",
    631: "IPP",
    636: "LDAPS",
    873: "rsync",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle Database",
    1723: "PPTP",
    1812: "RADIUS (Authentication)",
    1813: "RADIUS (Accounting)",
    2049: "NFS",
    2082: "cPanel",
    2083: "cPanel (Secure)",
    2181: "Apache Zookeeper",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion",
    4369: "Erlang Port Mapper",
    5432: "PostgreSQL",
    5672: "RabbitMQ",
    5900: "VNC",
    5984: "CouchDB",
    6379: "Redis",
    6667: "IRC (Default)",
    8000: "HTTP (Alternative)",
    8080: "HTTP (Alternative)",
    8081: "HTTP (Alternative)",
    8443: "HTTPS (Alternative)",
    8888: "HTTP (Alternative)",
    9000: "SonarQube",
    9092: "Kafka",
    9200: "Elasticsearch",
    9300: "Elasticsearch (Transport)",
    11211: "Memcached",
    27017: "MongoDB",
    27018: "MongoDB (Shard)",
    27019: "MongoDB (Config Server)",
    28017: "MongoDB (Web Admin)",
    50000: "SAP",
    50070: "Hadoop NameNode",
    50075: "Hadoop DataNode",
    50090: "Hadoop Secondary NameNode"
}

# Take user input for a port number
try:
    port = int(input("Enter a common port number: "))
    service = port_services.get(port)
    if service is None:
        print(f"Hello! The port {port} is not listed in our database.")
        print("You can check more details about this port at: https://www.speedguide.net/ports.php")
    else:
        print(f"Port {port}: {service}")
    service = port_services.get(port, "Unknown or not in the list")
    # print(f"Port {port}: {service}")
except ValueError:
    print("Invalid input. Please enter a valid port number.")