from colorama import Fore
import random
import string
import requests
from requests.exceptions import Timeout
from stem import Signal
from stem.control import Controller
import time
import os

toplvldomain = ".onion"
clear = lambda: os.system('cls')

print(Fore.RED + "       .---.        .-----------\n"
      "      /     \  __  /    ------\n"
      "     / /     \(  )/    -----\n"
      "    //////   ' " + Fore.YELLOW +
      "\/" + Fore.RED + "`   ---\n"
      "   //// / // :    : ---\n"
      "  // /   /  /`    '--\n"
      " //          //" + Fore.CYAN + ".."
      + Fore.RED + "\\\n"
      + Fore.BLUE + "        ====" +
      Fore.YELLOW + "UU" + Fore.BLUE +
      "====" + Fore.YELLOW + "UU" +
      Fore.BLUE + "====\n"  + Fore.RED +
      "            '//" + Fore.CYAN + "||" + Fore.RED + "\\`\n"
      "              ''``"
      + Fore.GREEN + "\n       --- TOR EAGLE ---\n"
      "       --- by deexno ---")

start = input(Fore.WHITE + "Möchten Sie mit der Suche nach .onion Links starten? (j|n): ")
clear()

try:
    #Tor Session starten / Proxies hinzufügen
    def get_session():
        session = requests.session()
        session.proxies = {"http": "socks5h://127.0.0.1:9050",
                                 "https": "socks5h://127.0.0.1:9050"}
        return session

    #Neue Identität anfordern
    def renew_connection():
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="T0r3@GlEPr0JeC7")
            controller.signal(Signal.NEWNYM)

    if(start.lower() == "j"):
        print(Fore.YELLOW + "Vergessen Sie nicht auch des Weiteren eine VPN zu nutzen!")
        time.sleep(3)
        clear()

        pathOK = True

        while(pathOK == True):
            path = input(Fore.WHITE + "Wo möchten Sie die gefundenen Links speichern? (ex. C:\\User\\You\\Desktop\\TorLinks.txt): ")
            print(Fore.GREEN + "Path: ", path)
            try:
                f = open(path, "a+")
                pathOK = False
                print("File created")
            except:
                print("Sie müssen einen existierenden Pfad eintragen!")
            time.sleep(2)
            clear()

        session = get_session()

        #Ausgeben der IP Adresse - Um zu kontrollieren ob die IP Adresse sicher geändert wurde
        print(Fore.RED + "Ihre normal IP-Address: " + ((requests.get("http://httpbin.org/ip").text).split('"'))[3].split(",")[0])
        print(Fore.GREEN + "Ihre TOR IP-Address: " + ((session.get("http://httpbin.org/ip").text).split('"'))[3].split(",")[0])

        time.sleep(3)
        clear()

        IPpool = input(Fore.WHITE + "Wie viele Links sollen generiert und gesucht werden?: ")
        clear()
        timeoutOp = input("Wie lange soll auf eine Antwort immer gewartet werden? (in sek.): ")
        clear()

        if(int(timeoutOp) < 5):
            print(Fore.YELLOW +"Info:" + Fore.RED + timeoutOp + " Sekunden könnte zu kurz sein, um tatsächlich eine Website zu finden!")

        while(int(IPpool) >= 0):
            # .onion Domain generieren
            domain = "".join(random.choice(string.ascii_letters) for x in range(16))
            URL = ("http://" + domain + toplvldomain)

            # Neue Identität anfordern
            renew_connection()
            session = get_session()
            print(Fore.WHITE + "\nIhre neue IP-Address: " + ((session.get("http://httpbin.org/ip").text).split('"'))[3].split(",")[0])

            # Kontrolliere ob die URl verfügbar ist
            try:
                response = session.get(str(URL), timeout=int(timeoutOp))
            except:
                print(Fore.RED + "'" + URL + "' ist nicht verfügbar")
            else:
                print(Fore.GREEN + "'" + URL + "' ist verfügbar")
                f.write(URL + "\n")
            IPpool = int(IPpool) - 1

        f.close()

    else:
        print("--- TOR EAGLE ---")
        print("--- BY DEEXNO ---")
except:
    INH = input("Ein Fehler ist aufgetreten. Mögliche Problemlösungen anzeigen?(j|n): ")
    if(INH.lower() == "j"):
        print("1. pip3 install colorama")
        print("2. pip3 install requests")
        print("3. pip3 install stem")
        print("4. pip3 install requests[socks]")
        print("Starten des Tor Expert Bundles")