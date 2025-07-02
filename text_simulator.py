import random

print("👋 Welcome to Si ka Khel – Digital Startup Tycoon")
money = 1000000
month = 1
valuation = 1000000

print("Choose your startup domain:")
print("1. SaaS\n2. Gaming\n3. EdTech")
domain = int(input("Enter choice: "))
domains = {1: "SaaS", 2: "Gaming", 3: "EdTech"}
print(f"You chose: {domains.get(domain, 'Unknown')}")

while money > 0 and valuation < 10000000:
    print(f"\n📅 Month {month} | 💰 Balance: ₹{money} | 💼 Valuation: ₹{valuation}")
    print("Choose an action:")
    print("1. Hire Team – ₹2L")
    print("2. Run Ads – ₹1L")
    print("3. Build Product – ₹3L")
    print("4. Seek Funding (50% chance)")

    choice = int(input("Enter your action: "))

    if choice == 1:
        money -= 200000
        valuation += 100000
        print("👨‍💻 Team hired. Valuation increased.")
    elif choice == 2:
        money -= 100000
        valuation += 150000
        print("📢 Ads worked! New users onboarded.")
    elif choice == 3:
        money -= 300000
        valuation += 250000
        print("🚀 Product launched! Market response positive.")
    elif choice == 4:
        if random.random() < 0.5:
            funds = random.randint(300000, 700000)
            money += funds
            print(f"💸 Funding secured: ₹{funds}")
        else:
            print("❌ Investors rejected your pitch.")
    else:
        print("Invalid choice.")

    # Random event
    if random.random() < 0.2:
        loss = random.randint(50000, 150000)
        money -= loss
        print(f"⚠️ Unexpected expense! Lost ₹{loss}")

    month += 1

# End Game
if money <= 0:
    print("\n💀 You ran out of money! Game over.")
else:
    print("\n🎉 Congratulations! Your startup reached ₹1 Cr+ valuation!")
