import time
import random


def delayed_print(*msgs):
    # a function to print info to the player with time delay for better
    # experience
    for msg in msgs:
        print(msg)
        time.sleep(0)


def handling_invalid_choices(expected_input):
    # a function to handle the invalid inputs entered by the player
    global n
    n = input()
    while n not in expected_input:
        if len(expected_input) == 2:
            n = input("Please Choose [1] or [2]")
        elif len(expected_input) == 3:
            n = input("Please Choose [1], [2], or [3]")


def intro():
    # a function that contains initil info presented to the player
    main_characters = ["Cybersecurity Specialist", "Robotics Programmer",
                       "Quantum Physicist", "Mechatronics Engineer"]
    evil_targets = [("Global Network Disruption:",
                    "Thorn plans to use the portal generator to hack"
                     "and disrupt global communication networks,",
                     "causing worldwide chaos."),
                    ("Weaponized AI Deployment:",
                     "Thorn intends to deploy AI with advanced weaponry,",
                     "giving him control over autonomous combat drones."),
                    ("Genetic Manipulation:",
                     "Thorn aims to use the technology for illegal genetic"
                     "experiments, creating a superhuman army.")]
    evil_target = random.choice(evil_targets)
    main_character = random.choice(main_characters)
    delayed_print("Welcome to Neo-Tokyo, 2145.", "You are Alex Mercer,"
                  f"a talented {main_character} working at "
                  "Stellar Innovations.",
                  "The city is alive with neon lights and advanced "
                  "technology,",
                  "but beneath the surface, secrets and challenges await.")
    delayed_print("One night, while working late in the lab,",
                  "you receive a mysterious encrypted message.",
                  "The blueprints attached appear to be for a groundbreaking "
                  "portal generator - based on your own stolen research.")
    delayed_print("he message hints at Dr. Elias Thorn's plans,",
                  "revealing a primary evil target")
    delayed_print(*evil_target)
    delayed_print("What do you do?")
    delayed_print("[1] Share the discovery with a trusted colleague.")
    delayed_print("[2] Keep it secret and investigate alone.")
    delayed_print("Choose [1] or [2]")


def sharing_msg(total_score):
    # what happens when after the play finds out the encrypted msg
    handling_invalid_choices(["1", "2"])
    if n == "1":
        delayed_print("You share the discovery with Dr. Kamiko, "
                      "a trusted colleague.")
        delayed_print("She agrees to help decode the message but warns you "
                      "to be cautious.",
                      "Together, you uncover a lead pointing to a rival "
                      "company's headquarters.")
        total_score += 10
    elif n == "2":
        delayed_print("You decide to keep the discovery to yourself "
                      "and investigate alone.",
                      "After hours of decrypting,",
                      "you find a lead pointing to a rival "
                      "company's headquarters.")
        total_score -= 10
    return total_score


def rival_company(total_score):
    # finding a clue to the rival company
    delayed_print("You infiltrate the rival company's headquarters.",
                  "Inside, you find evidence that points to "
                  "Dr. Elias Thorn, a disgraced former mentor,",
                  "as the mastermind behind the theft.")
    delayed_print("How do you handle the situation?")
    delayed_print("[1] Sneak out quietly with the evidence.")
    delayed_print("[2] Confront the security team head-on.")
    handling_invalid_choices(["1", "2"])
    if n == "1":
        delayed_print("You manage to sneak out with the evidence"
                      "and head to a hidden facility outside the city.")
        total_score += 15
    elif n == "2":
        delayed_print("You confront the security team, leading to a skirmish.",
                      "You escape with the evidence but are now on "
                      "their radar.",
                      "You head to a hidden facility outside the city.")
        total_score -= 5
    return total_score


def high_tech_lab(total_score):
    # the player the high-tech laboratory in the outskirts of the city
    delayed_print("You visit the high-tech laboratory in the city outskirts.",
                  "There, you find a secret lab with records pointing to"
                  "Dr. Elias Thorn as the mastermind behind the theft.")
    delayed_print("What do you do?")
    delayed_print("[1] Take the direct shuttle to confront Thorn on "
                  "Eridani Prime.",
                  "[2] Return to Neo-Tokyo to gather more information.")
    handling_invalid_choices(["1", "2"])
    if n == "1":
        delayed_print("You take the shuttle and head directly"
                      "to Eridani Prime,"
                      "ready for the confrontation.")
        total_score += 20
    elif n == "2":
        delayed_print("You return to Neo-Tokyo and discover "
                      "more information about Thorn's plans,",
                      "preparing for the final confrontation.")
        total_score += 10
    return total_score


def investigation(total_score):
    # the player starts to investigate
    delayed_print("Your investigation takes you through the "
                  "sprawling districts "
                  "of Neo-Tokyo,",
                  "facing various challenges along the way.")
    delayed_print("Where do you start your investigation?")
    delayed_print("[1] Search for clues at the rival company's headquarters.")
    delayed_print("[2] Visit the high-tech laboratory in "
                  "the outskirts of the city.")
    delayed_print("Choose [1] or [2]")
    handling_invalid_choices(["1", "2", "3"])
    if n == "1":
        total_score += 20
        total_score = rival_company(total_score)

    elif n == "2":
        total_score += 10
        total_score = high_tech_lab(total_score)
    return total_score


def portal_device(total_score):
    # here the player decides the fate of the portal device
    delayed_print("What do you do?")
    delayed_print("[1] Destroy the Portal Device to Prevent Misuse",
                  "[2] Secure the Device for Humanity's Benefit",
                  "[3] Leave the Device in Thorn's Control")
    delayed_print("Choose [1], [2], or [3]")
    handling_invalid_choices(["1", "2", "3"])
    if n == "1":
        delayed_print("The portal device is destroyed,"
                      "and Thorn’s plans are thwarted.",
                      "This is a heroic choice that ensures"
                      "Thorn’s evil targets cannot be realized.")
        delayed_print("You face the fallout from the destruction"
                      "of the device,",
                      "possibly endangering your own escape.")
        total_score += 30
    elif n == "2":
        delayed_print("You secure the device, ensuring it is used"
                      "responsibly and not misused.",
                      "This option requires a lot of trust in your ability"
                      "to manage or safeguard the technology.")
        delayed_print("You must ensure the device is safely"
                      "transported or stored,",
                      "which might involve more challenges.")
        total_score += 20
    elif n == "3":
        delayed_print("If you leave the device,"
                      "Thorn will use it to carry out his evil plans,",
                      "leading to widespread chaos.")
        delayed_print("Thorn executes his plans, causing global "
                      "network disruptions,",
                      "weaponized AI deployment, or illegal genetic"
                      "experiments.")
        total_score -= 30
    return total_score


def conclusion(total_score):
    # what happens to the player at the end of the story
    delayed_print("You’ve tracked Dr. Elias Thorn to a high-tech facility"
                  "on Eridani Prime.",
                  "Thorn is activating the portal device,"
                  "a crucial element in his evil plans.")
    delayed_print("How do you approach the confrontation?")
    delayed_print("[1] Confront Dr. Thorn directly.")
    delayed_print("[2] Attempt to outsmart him and disable the portal device.")
    delayed_print("Choose [1] or [2]")
    handling_invalid_choices(["1", "2"])
    if n == "1":
        delayed_print("You engage Thorn in a fierce battle.")
        if total_score < 25:
            delayed_print("Thorn activates the device, leading"
                          "to disastrous consequences.")
        else:
            delayed_print("You defeat Thorn, but now must decide"
                          "the fate of the portal device.")
            total_score = portal_device(total_score)

    elif n == "2":
        delayed_print("You try to bypass Thorn’s defenses"
                      "to gain control of the device.")
        if total_score >= 25:
            delayed_print("You gain control, but must decide what"
                          "to do with the portal device.")
            total_score = portal_device(total_score)
        else:
            delayed_print("Thorn confronts you, forcing a direct clash.")
    return total_score


def game():
    # main function of the story
    while True:
        total_score = 50
        delayed_print("This is a Sci-Fi adventerous story",
                      "You only needs your keyboard to have fun",
                      f"Your initial score is {total_score}",
                      "Let's get started!!")
        intro()
        total_score = sharing_msg(total_score)
        delayed_print(f"your current score is : {total_score}")
        total_score = investigation(total_score)
        delayed_print(f"your current score is : {total_score}")
        total_score = conclusion(total_score)
        delayed_print(f"Your Final Score is : {total_score}")
        f = input(("Do you want to play again? [y,n]")).lower()
        while f not in ["n", "y", "yes", "no"]:
            delayed_print("Please enter [y, n, yes, no]")
            f = input(("Do you want to play again? [y,n]")).lower()
        if f in ["n", "no"]:
            delayed_print("Thanks for your time!")
            break


game()
