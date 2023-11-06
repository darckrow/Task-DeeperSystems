import requests
from bs4 import BeautifulSoup
from pychromedevtools import ChromeDevTools

def get_all_odds():
    

   
    chrome_devtools = ChromeDevTools()
    chrome_devtools.connect()

    
    chrome_devtools.page.evaluate("document.querySelector('#event-simulator').click()")

    
    chrome_devtools.wait_for_selector(".game")

   
    odds_list = []
    for game in chrome_devtools.page.querySelectorAll(".game"):
        
        game_id = game.querySelector(".data-event-id").textContent
        team1 = game.querySelector(".team-name").textContent
        team2 = game.querySelector(".team-name.away").textContent
        sport_league = game.querySelector(".sport-league").textContent

        
        odds = game.querySelectorAll(".odd")
        for odd in odds:
            line_type = odd.querySelector(".line-type").textContent
            price = odd.querySelector(".price").textContent
            side = odd.querySelector(".side").textContent
            spread = odd.querySelector(".spread").textContent

            
            odds_dict = {
                "sport_league": sport_league,
                "event_date_utc": datetime.datetime.now().isoformat(),
                "team1": team1,
                "team2": team2,
                "line_type": line_type,
                "price": price,
                "side": side,
                "spread": spread,
            }

            
            odds_list.append(odds_dict)

    
    with open("odds.json", "w") as f:
        json.dump(odds_list, f, indent=4)

    return odds_list


odds_list = get_all_odds()


for odds in odds_list:
    print(odds)
