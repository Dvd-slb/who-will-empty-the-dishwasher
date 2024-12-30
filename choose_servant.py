from bs4 import BeautifulSoup
import requests
import re
import random
import json
import smtplib

# Cesty k souborům, které využijeme
environment = "<path/to/file/with/variables>"
finished_list = "<path/to/file/finished_cycles_list.txt>"

auth_file = json.load(enviroment)
my_email = auth_file["callie_email"]
password = auth_file["callie_email_pass"]
to_email = ["<first@recipient.xyz", "<second@recipient.abc>"]

# Získání dat z veřejně přístupného spreadsheetu, do kterého aplikace IFTTT zapisuje, že myčka už je hotová.
resource = requests.get("<link/to/public/google/spreadsheet>")
web = resource.text
soup = BeautifulSoup(web, "html.parser")
records = soup.text
matches = re.findall(r'##(.*?)\*', records)     # Dokončený cyklus si nechávám do spreadsheetu zapsat v tomto formátu: ### September 1, 2024 at 03:25PM

# Náhodně vyber jméno jednoho nešťastníka.
servants = ["Davide", "Kajinko"]
servant = random.choice(servants)

# Zkontroluje, jestli se nepřipsal nový dokončený cyklus do našeho sheetu. Pokud ano, připíše ho i do našeho seznamu "finished_list" a oběma možným vyndavačům pošle emaily s verdiktem.
with open(finished_list, "r+") as file:
    if len(file.readlines()) < len(matches):
        file.write(f"{matches[-1]} - {servant}\n")

        msg = f"""\
Subject: Dobra zprava! Vase nadobi se zase blyska!

Byla to fakt fuska, ale podarilo se mi vypucovat to zasvineny nadobi. {servant}, dneska budes Dish-jockey ty! 

Vase Boshka"""

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(my_email, to_email, msg)


