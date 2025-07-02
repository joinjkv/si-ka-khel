import random

print("👋 Welcome to Si ka Khel – Digital Startup Tycoon")
money = 1000000
month = 1
valuation = 1000000
morale = 70  # out of 100
rating = 3.0  # out of 5

print("Choose your startup domain:")
print("1. SaaS\n2. Gaming\n3. EdTech")
domain = int(input("Enter choice: "))
domains = {1: "SaaS", 2: "Gaming", 3: "EdTech"}
print(f"You chose: {domains.get(domain, 'Unknown')}")

while money > 0 and valuation < 10000000:
    print(f"\n📅 Month {month} | 💰 ₹{money} | 📈 ₹{valuation} | 😊 Morale: {morale}% | ⭐ Rating: {rating}/5")
    print("Choose an action:")
    print("1. Hire Team – ₹2L (Morale +10)")
    print("2. Run Ads – ₹1L (Rating +0.2)")
    print("3. Build Product – ₹3L (Rating +0.5, Morale -5)")
    print("4. Seek Funding (50% chance)")

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
        if random.random() < 0.5:
            funds = random.randint(300000, 700000)
            money += funds
            print(f"💸 Funding secured: ₹{funds}")
        else:
            print("❌ Investors rejected your pitch.")
    else:
        print("Invalid choice.")

    # 🔥 Random Event: Competitor Attack
    if random.random() < 0.2:
        impact = random.randint(100000, 200000)
        valuation -= impact
        print(f"⚔️ Competitor launched a rival feature. Lost ₹{impact} in valuation.")

    # 📉 Morale Decay
    morale = max(morale - 2, 0)

    # ☠️ Game Over Conditions
    if morale <= 0:
        print("\n😵‍💫 Your team lost motivation. Game Over.")
        break
    if rating <= 1.0:
        print("\n👎 Public hates your product. Game Over.")
        break

    month += 1

# 🎉 End Game
if money <= 0:
    print("\n💀 You ran out of money! Game over.")
elif valuation >= 10000000:
    print("\n🎉 You built a ₹1 Crore+ startup! Unicorn badge unlocked!")
