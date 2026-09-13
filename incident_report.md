# Security Incident Report

## Incident Summary

A simulated security log analysis identified suspicious authentication activity involving the `admin` account.

Five consecutive failed login attempts originated from the same external IP address, followed shortly by a successful login from that IP address.

## Evidence Identified

**Suspicious IP Address:** `185.220.101.14`

**Targeted Account:** `admin`

**Failed Attempts:** 5

**Successful Login:** Yes

**Time of Failed Attempts:** Approximately 09:45 AM

**Time of Successful Login:** Approximately 09:46 AM

## Analysis

The repeated failed authentication attempts followed by a successful login from the same IP address represents potentially suspicious behavior.

The pattern could indicate an attempted password-guessing or brute-force attack that eventually resulted in successful authentication.

Because this is a simulated dataset, the activity cannot be confirmed as an actual attack. However, the event should be investigated by a security analyst in a real environment.

## Recommended Response

1. Review the `admin` account for unauthorized activity.
2. Verify whether the successful login was legitimate.
3. Reset the account password if unauthorized access is suspected.
4. Review additional authentication and system logs for related activity.
5. Consider implementing account lockout or rate-limiting controls.
6. Monitor the suspicious IP address for additional activity.

## Conclusion

The analysis demonstrates how automated log analysis can help identify potentially malicious authentication patterns.

The Python script successfully detected repeated failed login attempts, identified the affected account and IP address, and flagged a successful login following the suspicious activity.

