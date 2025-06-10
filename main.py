import webbrowser

while True:
    quser = input("Open app or web-site: ").lower()
    
    if quser == "app":
        quser2 = input("Open app (e.g., google chrome): ")
        # You can expand this part with code to open apps if needed
        print(f"Opening app: {quser2} (currently not implemented for apps)")
        
    elif quser == "web-site":
        quser3 = input("Open web-site (github, youtube, channel, channel2, x, pinterest, ): ").lower()
        if quser3 == "github":
            webbrowser.open("https://www.github.com") 
            print("Opening github...")
        elif quser3 == "channel":
            webbrowser.open("https://www.youtube.com/channel/UCWA9W1KqWXBAU_A8v1y5XMg") 
            print("Opening channel...")
        elif quser3 == "channel2":
            webbrowser.open("UCWA9W1KqWXBAU_A8v1y5XMg") 
            print("Opening channel2...")
        elif quser3 == "x":
            webbrowser.open("https://x.com/OuyoussefR90480") 
            print("Opening x...")
        elif quser3 == "pinterest":
            webbrowser.open("https://www.pinterest.com/ouyoussefmohamedreda2/") 
            print("Opening pinterest...")
        elif quser3 == "kafiil":
            webbrowser.open("https://kafiil.com/u/mohamed_reda86") 
            print("Opening kafiil...")
        else:
            print("Website not recognized.")
    
    else:
        print("Invalid option. Please type 'app' or 'web-site'.")
