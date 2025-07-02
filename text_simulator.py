import random

print("👋 Welcome to Si ka Khel – Digital Startup Tycoon")
money = 1000000
month = 1
valuation = 1000000
morale = 70
rating = 3.0
funding_success = 0
funding_attempts = 0

# Leadership flags
cto_hired = False
coo_hired = False

print("Choose your startup domain:")
print("1. SaaS\n2. Gaming\n3. EdTech")
domain = int(input("Enter choice: "))
domains = {1: "SaaS", 2: "Gaming", 3: "EdTech"}
print(f"You chose: {domains.get(domain, 'Unknown')}")

while money > 0 and valuation < 10000000:
    print(f"\n📅 Month {month} | 💰 ₹{money} | 📈 ₹{valuation} | 😊 Morale: {morale}% | ⭐ Rating: {round(rating, 1)}/5")
    print("Choose an action:")
    print("1. Hire Team – ₹2L (Morale +10)")
    print("2. Run Ads – ₹1L (Rating +0.2)")
    print("3. Build Product – ₹3L (Rating +0.5, Morale -5)")
    print("4. Seek Funding (based on investor confidence)")
    print("5. Hire CTO – ₹3L (Slow morale decay)")
    print("6. Hire COO – ₹3L (Boost funding confidence)")

    choice = int(input("Enter your action: "))

    if choice == 1:
        money -= 200000
        valuation += 100000
        morale = min(morale + 10, 100)
        print("👨‍💻 Team hired. Morale boosted.")
    elif choice == 2:
        money -= 100000
        valuation += 150000
        rating = min(rating + 0.2, 5.0)
        print("📢 Ads ran successfully. Public perception improved.")
    elif choice == 3:
        money -= 300000
        valuation += 250000
        rating = min(rating + 0.5, 5.0)
        morale = max(morale - 5, 0)
        print("🚀 Product updated. Devs are a bit tired.")
    elif choice == 4:
        funding_attempts += 1
        confidence = funding_success / funding_attempts if funding_attempts > 1 else 0.5
        chance = 0.4 + confidence * 0.4
        if coo_hired:
            chance += 0.1

        if random.random() < chance:
            funds = random.randint(300000, 700000)
            money += funds
            funding_success += 1
            print(f"💸 Funding secured: ₹{funds} | Investor confidence increased.")
        else:
            print("❌ Investors rejected your pitch.")
    elif choice == 5:
        if not cto_hired and money >= 300000:
            money -= 300000
            cto_hired = True
            print("🧑‍💻 CTO hired! Morale won't drop as fast.")
        else:
            print("❌ Already hired or not enough funds.")
    elif choice == 6:
        if not coo_hired and money >= 300000:
            money -= 300000
            coo_hired = True
            print("📈 COO hired! Investor trust improved.")
        else:
            print("❌ Already hired or not enough funds.")
    else:
        print("Invalid choice.")

    # 🔥 Competitor Attack (capped)
    if random.random() < 0.2:
        impact = min(random.randint(50000, 200000), 150000)
        valuation -= impact
        print(f"⚔️ Competitor launched rival feature. Lost ₹{impact} in valuation.")

    # 🧠 Morale decay
    morale_loss = 2 if not cto_hired else 1
    morale = max(morale - morale_loss, 0)

    # ❌ Game Over Conditions
    if morale <= 0:
        print("\n😵‍💫 Your team lost motivation. Everyone quit!")
        break
    if rating <= 1.0:
        print("\n👎 Public hates your product. You went viral… for all the wrong reasons!")
        break

    month += 1

# 🏁 End Summary
print("\n📊 Game Summary:")
print(f"🏁 You survived for {month} months.")
print(f"📈 Final Valuation: ₹{valuation}")
print(f"💰 Final Balance: ₹{money}")
print(f"😊 Team Morale: {morale}%")
print(f"⭐ Product Rating: {round(rating, 1)}/5")
print(f"💼 Funding Success Rate: {funding_success}/{funding_attempts}")
print(f"🧑‍💻 CTO Hired: {'Yes' if cto_hired else 'No'}")
print(f"📈 COO Hired: {'Yes' if coo_hired else 'No'}")

if money <= 0:
    print("💸 You ran out of funds! Startup collapsed. 😓")
elif valuation >= 10000000:
    print("🦄 You built a ₹1 Cr+ Unicorn! Investors love you. 🎉")
