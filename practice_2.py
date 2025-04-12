# Dictionary to categorize suspicious IPs
suspicious_ip = {
    "192.168.1.1": "low",
    "10.0.0.1": "medium",
    "172.16.0.1": "high",
    "8.8.8.8": "danger",
    "192.168.0.100": "low",
    "10.0.0.50": "medium",
    "172.16.1.1": "high",
    "1.1.1.1": "danger",
    "192.168.1.50": "low",
    "10.0.0.100": "medium",
    "172.16.2.1": "high",
    "8.8.4.4": "danger",
    "192.168.2.1": "low",
    "10.0.1.1": "medium",
    "172.16.3.1": "high",
    "9.9.9.9": "danger",
    "192.168.3.1": "low",
    "10.0.2.1": "medium",
    "172.16.4.1": "high",
    "4.4.4.4": "danger"
    
}
print("Select the category of suspicious IPs you want to see: ")
print("1. Low")
print("2. Medium")
print("3. High")
print("4. Danger")
print("5. All")
mark= input("Enter your choice (1-5): ")
if mark == "1":
    print("Low Suspicious IPs:")
    for ip, level in suspicious_ip.items():
        if level == "low":
            print(ip)
elif mark == "2":
    print("Medium Suspicious IPs:")
    for ip, level in suspicious_ip.items():
        if level == "medium":
            print(ip)
elif mark == "3":   
    print("High Suspicious IPs:")
    for ip, level in suspicious_ip.items():
        if level == "high":
            print(ip)
elif mark == "4":
    print("Danger Suspicious IPs:")
    for ip, level in suspicious_ip.items():
        if level == "danger":
            print(ip)
elif mark == "5":
    print("All Suspicious IPs:")
    for ip, level in suspicious_ip.items():
        print(f"{ip}: {level}") 
else:
    print("Invalid selection. Please choose a valid option.")
    
print(".......................Ip filter Program By peter-Parker")
print("Program finished....................................")
print("Thanks for using this program.................................")
print("Bye Bye....................................................................")
print("All rights reserved.")