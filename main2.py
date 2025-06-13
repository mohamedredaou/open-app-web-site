import webbrowser
import os
import subprocess

while True:
  quser = input("open type (system|programming|design|drawing|internet|freelance|games|chine) : ").lower()
  if quser == "programming":
    quser1 = input("open (visual studio code (vsc)|github|git|command prompt (cmd.exe)|app development|game development) : ").lower()
    if quser1 == "visual studio code (vsc)" or quser1 == "visual studio code" or quser1 == "vsc":
      vsc_path = r"C:\Users\Réda\AppData\Local\Programs\Microsoft VS Code\Code.exe" 
      try:
        subprocess.Popen([vsc_path]) 
        print("Visual Studio Code (VSC) has been opened successfully.")
      except FileNotFoundError:
        print(f"Error: Visual Studio Code file not found in specified path: {vsc_path}")
        print("Please make sure the path is correct or that VS Code is installed..")
      except Exception as e:
        print(f"Error opening Visual Studio Code (VSC): {e}")
    elif quser1 == "github":
      webbrowser.open("https://github.com/mohamedredaou")
      print("Opening github...")
#    elif quser1 == "git":
    elif quser1 == "command prompt (cmd.exe)" or quser1 == "command prompt" or quser1 == "cmd" or quser1 == "cmd.exe":
      cmd_path = r"C:\Windows\System32\cmd.exe" 
      try:
        subprocess.Popen([cmd_path]) 
        print("has been opened successfully.(CMD)")
      except FileNotFoundError:
        print(f"Error: cmd file not found in specified path {cmd_path}")
        print("Please make sure the path is correct or that cmd is installed..")
      except Exception as e:
        print(f"Error opening (cmd): {e}")
#    elif quser1 == "app development":
#      quser2 = input("open (flutter|android developer studio (ads)) : ").lower()
#      if quser2 == "android developer studio (ads)" or quser1 == "android developer studio" or quser1 == "ads":
#      elif quser2 == "flutter":
#      else:
#        print("This app & web-site does not exist")
#    elif quser1 == "game development":
#      quser3 = input("open (godot|unreal engine 5) : ").lower()
#      if quser3 == "godot":
#      elif quser3 == "unreal engine 5":
#      else:
#        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
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
    elif quser5 == "social media design":
      quser10 = input("open (photopea) : ").lower()
      if quser10 == "photopea":
        webbrowser.open("https://photopea.com/") 
        print("Opening photopea...")
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  elif quser == "drawing":
    quser4 = input("open (clip studio paint (csp)|infinite painter|deviantArt|artstation|tumblr) : ").lower()
#    if quser4 == "clip studio paint (csp)" or quser4 == "csp" or quser4 == "clip studio paint":
#    elif quser4 == "infinite painter":
    if quser4 == "deviantArt":
      webbrowser.open("https://DeviantArt.com/") 
      print("Opening deviantArt...")
    elif quser4 == "artstation":
      webbrowser.open("https://artstation.com/") 
      print("Opening artstation...")
    elif quser4 == "tumblr":
      webbrowser.open("https://tumblr.com/") 
      print("Opening tumblr...")
    else:
      print("This app & web-site does not exist")
  elif quser == "internet":
    queser16 = input(" open (social media|browser|google) : ").lower()
    if queser16 == "social media":
      queser17 = input(" open (youTube|tumblr|x (twitter)|instagram|pinterest|behance|whatsapp|telegram|dribbble) : ").lower()
      if queser17 == "youTube":
        webbrowser.open("https://youTube.com/") 
        print("Opening youTube...")
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
#    elif queser16 == "browser":
#      queser18 = input("open (google chrome|firefox|Brave) : ").lower()
 #      if queser18 == "google chrome":
#      elif queser18 == "firefox":
#      elif queser18 == "Brave":
#      else:
#        print("This app & web-site does not exist")
    elif queser16 == "google":
      queser19 = input("open (google chrome|google search|gmail|google drive|google docs|google Sheets|google slides|google keep|google maps|google earth|google fonts|google translate|google play store|google account|calendar) : ").lower()
#      if queser19 == "google chrome":
      if queser19 == "google search":
        webbrowser.open("https://www.google.com/") 
        print("Opening google...")
      elif queser19 == "gmail":
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
        print("Opening mail...")
      elif queser19 == "google drive":
        webbrowser.open("https://drive.google.com/drive/home") 
        print("Opening drive...")
      elif queser19 == "google docs":
        webbrowser.open("https://docs.google.com/document/u/0/") 
        print("Opening docs...")
      elif queser19 == "google Sheets":
        webbrowser.open("https://docs.google.com/spreadsheets/u/0/") 
        print("Opening Sheets...")
      elif queser19 == "google slides":
        webbrowser.open("https://docs.google.com/presentation/u/0/") 
        print("Opening slides...")
      elif queser19 == "google calendar":
        webbrowser.open("https://calendar.google.com/calendar/u/0/r?pli=1") 
        print("Opening calendar...")
      elif queser19 == "google keep":
        webbrowser.open("https://keep.google.com/") 
        print("Opening keep...")
      elif queser19 == "google maps":
        webbrowser.open("https://www.google.com/maps") 
        print("Opening maps...")
      elif queser19 == "google earth":
        webbrowser.open("https://earth.google.com/web/") 
        print("Opening google earth...")
      elif queser19 == "google play store":
        webbrowser.open("https://play.google.com/store/games?hl=en") 
        print("Opening play store...")
#      elif queser19 == "google Photos":
      elif queser19 == "google adsense":
        webbrowser.open("https://adsense.google.com/start/") 
        print("Opening adsense...")
      elif queser19 == "google translate":
        webbrowser.open("https://translate.google.com/?sl=ar&tl=en&op=translate") 
        print("Opening translate...")
      elif queser19 == "google account":
        webbrowser.open("https://myaccount.google.com/?utm_source=OGB&utm_medium=app") 
        print("Opening account...")
      elif queser19 == "google fonts":
        webbrowser.open("https://fonts.google.com/") 
        print("Opening fonts...")
      else:
        print("This app & web-site does not exist")
    else:
      print("This app & web-site does not exist")
  elif quser == "freelance":
    queser15 = input("open (behance|freelancer|dribbble|kafiil|khamsat|mostaql) : ").lower()
    if queser15 == "behance":
      webbrowser.open("https://behance.com/") 
      print("Opening behance...")
    elif queser15 == "freelancer":
      webbrowser.open("https://freelancer.com/") 
      print("Opening freelancer...")
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
    queser14 = input("open (steam|asphalt legends - racing game|genshin impact|EA SPORTS FC™ Mobile Soccer|Dummynation|Forza Horizon 5|web-site) : ").lower()
    if queser14 == "steam":
      webbrowser.open("https://store.steampowered.com/") 
      print("Opening steam...")
#    elif queser14 == "asphalt legends - racing game":
    elif queser14 == "web-site":
      queser20 = input("open (territorial io|crazygames|oskarstalberg planet|oskarstalberg townscaper|slowroads) : ").lower()
      if queser20 == "territorial io":
        webbrowser.open("https://territorial.io/")
        print("Opening territorial io...")
      elif queser20 == "crazygames":
        webbrowser.open("https://www.crazygames.com/") 
        print("Opening crazy games...")
      elif queser20 == "oskarstalberg planet": 
        webbrowser.open("https://oskarstalberg.com/game/planet/planet.html")
        print("Opening oskarstalberg planet...")
      elif queser20 == "oskarstalberg townscaper":
        webbrowser.open("https://oskarstalberg.com/Townscaper/#GSB0RARueC6Snc9E0lO5B")
        print("Opening oskarstalberg townscaper...")
      elif queser20 == "slowroads":
        queser21 = input("open (race|free) : ").lower()
        if queser21 == "free":
          webbrowser.open("https://slowroads.io/")
          print("Opening slowroads free...")
        elif queser21 == "race":
          webbrowser.open("https://driftmas.slowroads.io/")
          print("Opening slowroads race...")
        else:
          print("This app & web-site does not exist")
      else:
        print("This app & web-site does not exist")
#    elif queser14 == "genshin impact":
#    elif queser14 == "eFootball":
#    elif queser14 == "Dummynation":
#    elif queser14 == "Forza Horizon 5":
#    else:
#      print("This app & web-site does not exist")
  elif quser == "chine":
    quser11 = input("open (rednote|bilibili|baidu|manga|anime|weibo) : ").lower()
#    if quser11 == "rednote":
    if quser11 == "weibo":
      webbrowser.open("https://m.weibo.cn/") 
      print("Opening weibo...")
    elif quser11 == "bilibili":
      webbrowser.open("https://www.bilibili.com/") 
      print("Opening bilibili...")
    elif quser11 == "baidu":
      webbrowser.open("https://www.baidu.com/") 
      print("Opening baidu...")
    elif quser11 == "manga":
      quser12 = input("open (1 = مانجا للشباب = 2|مانجا للصغار|webtoons) : ").lower()
#      if quser12 == "1":
#      elif quser12 == "2":
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
