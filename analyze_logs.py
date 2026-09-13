from collections import Counter

log_file = "security.log"

failed_logins = []
successful_logins = []

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if "LOGIN_FAILED" in line:
            failed_logins.append(line)

        elif "LOGIN_SUCCESS" in line:
            successful_logins.append(line)

print("CYBERSECURITY LOG ANALYSIS")
print("=" * 35)

print(f"\nTotal failed login attempts: {len(failed_logins)}")
print(f"Total successful logins: {len(successful_logins)}")

# Analyze failed login attempts
failed_ips = []
failed_users = []

for entry in failed_logins:
    parts = entry.split()

    for part in parts:
        if part.startswith("ip="):
            failed_ips.append(part.replace("ip=", ""))

        if part.startswith("user="):
            failed_users.append(part.replace("user=", ""))

ip_counts = Counter(failed_ips)
user_counts = Counter(failed_users)

print("\nFailed Login Attempts by IP")
print("-" * 35)

for ip, count in ip_counts.items():
    print(f"{ip}: {count} attempts")

print("\nTargeted User Accounts")
print("-" * 35)

for user, count in user_counts.items():
    print(f"{user}: {count} failed attempts")

print("\nSuspicious Activity")
print("-" * 35)

suspicious_ips = []

for ip, count in ip_counts.items():
    if count >= 3:
        suspicious_ips.append(ip)
        print(f"WARNING: {ip} generated {count} failed login attempts.")

print("\nSuccessful Login After Suspicious Activity")
print("-" * 35)

for entry in successful_logins:
    for ip in suspicious_ips:
        if f"ip={ip}" in entry:
            print(f"ALERT: Successful login detected from {ip}")
            print(f"Event: {entry}")
