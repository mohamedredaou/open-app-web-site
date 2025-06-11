import webbrowser

while True:
  quser = input("open type (system|Programming|design|drawing|internet|Freelance|games|chine) : ").lower()
  if quser == "system":
  elif quser == "Programming":
    quser1 = input("open (Visual Studio Code (vsc)|GitHub|Git|Command Prompt (cmd.exe)|app development|Game development) : ").lower()
    if quser1 == "Visual Studio Code (vsc)" or quser1 == "Visual Studio Code" or quser1 == "vsc":
    elif quser1 == "GitHub":
      webbrowser.open("https://github.com/mohamedredaou") 
      print("Opening GitHub...")
    elif quser1 == "Git":
    elif quser1 == "Command Prompt (cmd.exe)" or quser1 == "Command Prompt" or quser1 == "cmd" or quser1 == "cmd.exe":
    elif quser1 == "app development":
      quser2 = input("open (Flutter|android developer studio (ads)) : ").lower()
      if quser2 == "android developer studio (ads)" or quser1 == "android developer studio" or quser1 == "ads":
      elif quser2 == "Flutter":
      else:
        print("This app & web-site does not exist")
    elif quser1 == "Game development":
      quser3 = input("open (godot|Unreal Engine 5) : ").lower()
      if quser3 == "godot":
      elif quser3 == "Unreal Engine 5":
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  elif quser == "design":
    quser5 = input("open (unblast|unsplash|freepik|dribbble|behance|sketchfab|free3d|edit video & image|design ui, ux|graphic design|3D design|Social media design) : ").lower()
    if quser5 == "unblast":
      webbrowser.open("https://unblast.com/") 
      print("Opening unblast...")
    elif quser5 == "unsplash":
      webbrowser.open("https://unsplash.com/") 
      print("Opening unsplash...")
    elif quser5 == "freepik":
      webbrowser.open("https://freepik.com/") 
      print("Opening freepik...")
    elif quser5 == "dribbble":
      webbrowser.open("https://dribbble.com/") 
      print("Opening dribbble...")
    elif quser5 == "behance":
      webbrowser.open("https://behance.com/") 
      print("Opening behance...")
    elif quser5 == "sketchfab":
      webbrowser.open("https://sketchfab.com/") 
      print("Opening sketchfab...")
    elif quser5 == "free3d":
      webbrowser.open("https://free3d.com/") 
      print("Opening free3d...")
    elif quser5 == "edit video & image":
      quser6 = input("open (davinci resolve) : ").lower()
      if quser6 == "davinci resolve":
    elif quser5 == "design ui, ux":
      quser7 = input("open (figma) : ").lower()
      if quser7 == "figma":
        webbrowser.open("https://figma.com/") 
        print("Opening figma...")
      else:
        print("This app & web-site does not exist")
    elif quser5 == "graphic design":
      quser8 = input("open (Inkscape) : ").lower()
      if quser8 == "Inkscape":
      else:
        print("This app & web-site does not exist")
    elif quser5 == "3D design":
      quser9 = input("open (blender|SketchUp) : ").lower()
      if quser9 == "blender":
      elif quser9 == "SketchUp":
      else:
        print("This app & web-site does not exist")
    elif quser5 == "Social media design":
      quser10 = input("open (photopea) : ").lower()
      if quser10 == "photopea":
        webbrowser.open("https://photopea.com/") 
        print("Opening photopea...")
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  elif quser == "drawing":
    quser4 = input("open (Clip Studio Paint (csp)|Infinite Painter|DeviantArt|artstation|tumblr) : ").lower()
    if quser4 == "Clip Studio Paint (csp)" or quser4 == "csp" or quser4 == "Clip Studio Paint":
    elif quser4 == "Infinite Painter":
    elif quser4 == "DeviantArt":
    elif quser4 == "artstation":
    elif quser4 == "tumblr":
    else:
      print("This app & web-site does not exist")
#  elif quser == "internet":
  elif quser == "Freelance":
    queser15 = input("open (behance|Freelancer|dribbble|kafiil|khamsat|mostaql) : ").lower()
    if quser15 == "behance":
    elif quser15 == "Freelancer":
    elif quser15 == "dribbble":
    elif quser15 == "kafiil":
    elif quser15 == "khamsat":
    elif quser15 == "mostaql":
    else:
      print("This app & web-site does not exist")
  elif quser == "games":
    queser14 = input("open (steam|Asphalt Legends - Racing Game|Genshin Impact|eFootball|Dummynation|Forza Horizon 5) : ").lower()
    if quser14 == "steam":
    elif quser14 == "Asphalt Legends - Racing Game":
    elif quser14 == "Genshin Impact":
    elif quser14 == "eFootball":
    elif quser14 == "Dummynation":
    elif quser14 == "Forza Horizon 5":
    else:
      print("This app & web-site does not exist")
  elif quser == "chine":
    quser11 = input("open (rednote|bilibili|baidu|manga|anime) : ").lower()
    if quser11 == "rednote":
    elif quser11 == "bilibili":
    elif quser11 == "baidu":
    elif quser11 == "manga":
      quser12 = input("open (مانجا للشباب|مانجا للصغار|webtoons) : ").lower()
      if quser12 == "مانجا للشباب":
      elif quser12 == "مانجا للصغار":
      elif quser12 == "webtoons":
      else:
        print("This app & web-site does not exist")
    elif quser11 == "anime":
      quser13 = input("open (Anime Ray - انمي راي|Crunchyroll) : ").lower()
      if quser13 == "Anime Ray - انمي راي":
      elif quser13 == "Crunchyroll":
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  else:
    print("This type does not exist")
