

failed = 0
success = 0

with open("logs.txt", "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:
            failed += 1
        elif "LOGIN_SUCCESS" in line:
            success += 1

print(f"Udane logowania: {success}")
print(f"Nieudane logowania: {failed}")