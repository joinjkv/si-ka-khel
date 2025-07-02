print("👋 Welcome to Si ka Khel – Digital Startup Tycoon")
money = 1000000
print("You have ₹10,00,000 to build your startup.")

print("\nChoose your domain:")
print("1. SaaS\n2. Gaming\n3. EdTech")
domain = int(input("Enter choice: "))
domains = {1: "SaaS", 2: "Gaming", 3: "EdTech"}
print(f"You chose: {domains.get(domain, 'Unknown')}")

print("\nChoose an action:")
print("1. Hire Developers – ₹2,00,000")
print("2. Run Ads – ₹1,00,000")
print("3. Build MVP – ₹3,00,000")
choice = int(input("Enter choice: "))

if choice == 1:
    money -= 200000
    print("👨‍💻 Developers hired.")
elif choice == 2:
    money -= 100000
    print("📢 Ads are running.")
elif choice == 3:
    money -= 300000
    print("🚀 MVP is built.")
else:
    print("❌ Invalid choice.")

print(f"💰 Remaining Money: ₹{money}")
