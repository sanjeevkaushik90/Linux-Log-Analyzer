with open("sample.log") as file:
    count = 0
    ip_count = {}

    for line in file:
        if "Failed password" in line:
            count += 1

            print(line.strip())

            ip = line.split("from")
            ip_address = ip[1].strip()

            if ip_address not in ip_count:
                ip_count[ip_address] = 1
            else:
                ip_count[ip_address] += 1

    print(f"Failed login attempts: {count}")

    for ip, attempts in ip_count.items():
        print(f"{ip} → {attempts} failed attempts")

    threshold = 3

    for ip, attempts in ip_count.items():
      if attempts >= threshold:
        print("IP address with more than 3 failed attempts:", ip)
      else:
        print("IP address with less than 3 failed attempts:", ip)