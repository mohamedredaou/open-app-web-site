import webbrowser
import webbrowser

while True:
  quser = input("open type (system|Programming|design|drawing|internet|Freelance|games|chine) : ").lower()
#  if quser == "system":
  if quser == "Programming":
    quser1 = input("open (Visual Studio Code (vsc)|GitHub|Git|Command Prompt (cmd.exe)|app development|Game development) : ").lower()
#    if quser1 == "Visual Studio Code (vsc)" or quser1 == "Visual Studio Code" or quser1 == "vsc":
    if quser1 == "GitHub":
      webbrowser.open("https://github.com/mohamedredaou") 
      print("Opening GitHub...")
#    elif quser1 == "Git":
#    elif quser1 == "Command Prompt (cmd.exe)" or quser1 == "Command Prompt" or quser1 == "cmd" or quser1 == "cmd.exe":
#    elif quser1 == "app development":
#      quser2 = input("open (Flutter|android developer studio (ads)) : ").lower()
#      if quser2 == "android developer studio (ads)" or quser1 == "android developer studio" or quser1 == "ads":
#      elif quser2 == "Flutter":
#      else:
#        print("This app & web-site does not exist")
#    elif quser1 == "Game development":
#      quser3 = input("open (godot|Unreal Engine 5) : ").lower()
#      if quser3 == "godot":
#      elif quser3 == "Unreal Engine 5":
#      else:
#        print("This app & web-site does not exist")
#    else:
#      print("This app & web-site does not exist")
  elif quser == "design":
    quser5 = input("open (unblast|unsplash|font|freepik|dribbble|behance|sketchfab|free3d|edit video & image|design ui, ux|graphic design|3D design|Social media design) : ").lower()
    if quser5 == "unblast":
      webbrowser.open("https://unblast.com/") 
      print("Opening unblast...")
    elif quser5 == "unsplash":
      webbrowser.open("https://unsplash.com/") 
      print("Opening unsplash...")
    elif quser5 == "font":
      quser20 = input("oprn (fontshare|dafont|fonts google|fonts cn)")
      if quser20 == "fontshare":
        webbrowser.open("https://www.fontshare.com/") 
        print("Opening fontshare...")
      elif quser20 == "dafont":
        webbrowser.open("https://www.dafont.com/") 
        print("Opening dafont...")
      elif quser20 == "fonts google":
        webbrowser.open("https://fonts.google.com//") 
        print("Opening fonts google...")
      elif quser20 == "fonts cn":
        webbrowser.open("https://www.fonts.net.cn/") 
        print("Opening fonts cn...")
      else:
        print("This app & web-site does not exist")
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
#    elif quser5 == "edit video & image":
#      quser6 = input("open (davinci resolve) : ").lower()
#      if quser6 == "davinci resolve":
    elif quser5 == "design ui, ux":
      quser7 = input("open (figma) : ").lower()
      if quser7 == "figma":
        webbrowser.open("https://figma.com/") 
        print("Opening figma...")
      else:
        print("This app & web-site does not exist")
#    elif quser5 == "graphic design":
#      quser8 = input("open (Inkscape) : ").lower()
#      if quser8 == "Inkscape":
#      else:
#        print("This app & web-site does not exist")
#    elif quser5 == "3D design":
#      quser9 = input("open (blender|SketchUp) : ").lower()
#      if quser9 == "blender":
#      elif quser9 == "SketchUp":
#      else:
#        print("This app & web-site does not exist")
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
#    if quser4 == "Clip Studio Paint (csp)" or quser4 == "csp" or quser4 == "Clip Studio Paint":
#    elif quser4 == "Infinite Painter":
    if quser4 == "DeviantArt":
      webbrowser.open("https://DeviantArt.com/") 
      print("Opening DeviantArt...")
    elif quser4 == "artstation":
      webbrowser.open("https://artstation.com/") 
      print("Opening artstation...")
    elif quser4 == "tumblr":
      webbrowser.open("https://tumblr.com/") 
      print("Opening tumblr...")
    else:
      print("This app & web-site does not exist")
  elif quser == "internet":
    queser16 = input(" open (Social media|Browser|google) : ").lower()
    if queser16 == "Social media":
      queser17 = input(" open (YouTube|tumblr|x (twitter)|instagram|pinterest|behance|whatsapp|telegram|dribbble) : ").lower()
      if queser17 == "YouTube":
        webbrowser.open("https://YouTube.com/") 
        print("Opening YouTube...")
      elif queser17 == "tumblr":
        webbrowser.open("https://tumblr.com/") 
        print("Opening tumblr...")
      elif queser17 == "x (twitter)" or queser17 == "x" or queser17 == "twitter":
        webbrowser.open("https://x.com/")
        print("Opening x (twitter)...")
#      elif queser17 == "instagram":
      elif queser17 == "pinterest":
        webbrowser.open("https://pinterest.com/")
        print("Opening pinterest...")
#      elif queser17 == "whatsapp":
#      elif queser17 == "telegram":
      elif queser17 == "dribbble":
        webbrowser.open("https://dribbble.com/")
        print("Opening dribbble...")
      else:
        print("This app & web-site does not exist")
#    elif queser16 == "Browser":
#      queser18 = input("open (google chrome|firefox|Brave) : ").lower()
 #      if queser18 == "google chrome":
#      elif queser18 == "firefox":
#      elif queser18 == "Brave":
#      else:
#        print("This app & web-site does not exist")
    elif queser16 == "google":
      queser19 = input("open (google chrome|google Search|gmail|google Drive|google Docs|google Sheets|google Slides|google Keep|google Maps|google Earth|google Fonts|google translate|google Play Store|google Account) : ").lower()
#      if queser19 == "google chrome":
      if queser19 == "google Search":
        webbrowser.open("https://www.google.com/") 
        print("Opening google...")
      elif queser19 == "gmail":
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
        print("Opening mail...")
      elif queser19 == "google Drive":
        webbrowser.open("https://drive.google.com/drive/home") 
        print("Opening drive...")
      elif queser19 == "google Docs":
        webbrowser.open("https://docs.google.com/document/u/0/") 
        print("Opening docs...")
      elif queser19 == "google Sheets":
        webbrowser.open("https://docs.google.com/spreadsheets/u/0/") 
        print("Opening Sheets...")
      elif queser19 == "google Slides":
        webbrowser.open("https://docs.google.com/presentation/u/0/") 
        print("Opening Slides...")
      elif queser19 == "google Calendar":
        webbrowser.open("https://calendar.google.com/calendar/u/0/r?pli=1") 
        print("Opening Calendar...")
      elif queser19 == "google Keep":
        webbrowser.open("https://keep.google.com/") 
        print("Opening Keep...")
      elif queser19 == "google Maps":
        webbrowser.open("https://www.google.com/maps") 
        print("Opening Maps...")
      elif queser19 == "google Earth":
        webbrowser.open("https://earth.google.com/web/") 
        print("Opening google Earth...")
      elif queser19 == "google Play Store":
        webbrowser.open("https://play.google.com/store/games?hl=en") 
        print("Opening Play Store...")
#      elif queser19 == "google Photos":
      elif queser19 == "google AdSense":
        webbrowser.open("https://adsense.google.com/start/") 
        print("Opening AdSense...")
      elif queser19 == "google translate":
        webbrowser.open("https://translate.google.com/?sl=ar&tl=en&op=translate") 
        print("Opening translate...")
      elif queser19 == "google Account":
        webbrowser.open("https://myaccount.google.com/?utm_source=OGB&utm_medium=app") 
        print("Opening Account...")
      elif queser19 == "google Fonts":
        webbrowser.open("https://fonts.google.com/") 
        print("Opening Fonts...")
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  elif quser == "Freelance":
    queser15 = input("open (behance|Freelancer|dribbble|kafiil|khamsat|mostaql) : ").lower()
    if queser15 == "behance":
      webbrowser.open("https://behance.com/") 
      print("Opening behance...")
    elif queser15 == "Freelancer":
      webbrowser.open("https://Freelancer.com/") 
      print("Opening Freelancer...")
    elif queser15 == "dribbble":
      webbrowser.open("https://dribbble.com/") 
      print("Opening dribbble...")
    elif queser15 == "kafiil":
      webbrowser.open("https://kafiil.com/") 
      print("Opening kafiil...")
    elif queser15 == "khamsat":
      webbrowser.open("https://khamsat.com/") 
      print("Opening khamsat...")
    elif queser15 == "mostaql":
      webbrowser.open("https://mostaql.com/") 
      print("Opening mostaql...")
    else:
      print("This app & web-site does not exist")
  elif quser == "games":
    queser14 = input("open (steam|Asphalt Legends - Racing Game|Genshin Impact|eFootball|Dummynation|Forza Horizon 5|territorial io) : ").lower()
    if queser14 == "steam":
      webbrowser.open("https://store.steampowered.com/") 
      print("Opening steam...")
#    elif queser14 == "Asphalt Legends - Racing Game":
    elif queser14 == "territorial io":
      webbrowser.open("https://territorial.io/")
      print("Opening territorial io...")
#    elif queser14 == "Genshin Impact":
#    elif queser14 == "eFootball":
#    elif queser14 == "Dummynation":
#    elif queser14 == "Forza Horizon 5":
#    else:
#      print("This app & web-site does not exist")
  elif quser == "chine":
    quser11 = input("open (rednote|bilibili|baidu|manga|anime|Weibo) : ").lower()
#    if quser11 == "rednote":
    if quser11 == "Weibo":
      webbrowser.open("https://m.weibo.cn/") 
      print("Opening Weibo...")
    elif quser11 == "bilibili":
      webbrowser.open("https://www.bilibili.com/") 
      print("Opening bilibili...")
    elif quser11 == "baidu":
      webbrowser.open("https://www.baidu.com/") 
      print("Opening baidu...")
    elif quser11 == "manga":
      quser12 = input("open (مانجا للشباب|مانجا للصغار|webtoons) : ").lower()
#      if quser12 == "مانجا للشباب":
#      elif quser12 == "مانجا للصغار":
      if quser12 == "webtoons":
        webbrowser.open("https://webtoons.com/") 
        print("Opening webtoons...")
      else:
        print("This app & web-site does not exist")
#    elif quser11 == "anime":
#      quser13 = input("open (Anime Ray - انمي راي|Crunchyroll) : ").lower()
#      if quser13 == "Anime Ray - انمي راي":
#      elif quser13 == "Crunchyroll":
#      else:
#        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  else:
    print("This type does not exist")
  else:
    print("This type does not exist")
