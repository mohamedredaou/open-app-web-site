import webbrowser

while True:
    quser = input("Open app or web-site: ").lower()
    
    if quser == "app":
        quser2 = input("Open app (e.g., google chrome): ")
        # You can expand this part with code to open apps if needed
        print(f"Opening app: {quser2} (currently not implemented for apps)")
        
    elif quser == "web-site":
        quser3 = input("Open web-site (e.g., youtube): ").lower()
        if quser3 == "youtube":
            webbrowser.open("https://www.youtube.com") 
            print("Opening YouTube...")
        else:
            print("Website not recognized.")
    
    else:
        print("Invalid option. Please type 'app' or 'web-site'.")