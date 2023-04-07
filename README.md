# pyfloraapp
TODO: opis aplikacije, upute


TODO:    1. Prijava u aplikaciju.
            predefinirani korisnik koji može uređivati svoje korisničke podatke
            obvezna polja, skrivanje prikaza podataka u poljima tijekom unosa
            nakon uspješne prijave, korisnik može pristupiti ostalim funkcionalnostima aplikacije

TODO:    2. Ažuriranje podataka sa senzora
            Ovisno o očitanim podacima, pokreću se aktivnosti
            Ako je vlažnost zemljišta niska, pokreće se aktivnost zalijevanja i sl.

TODO:    3. Evidencija biljaka # API https://docs.trefle.io/docs/examples/snippets/
            Aplikacija treba imati bazu podataka o biljkama 
                a. Podaci koje treba čuvati o biljci su ():
                    i. identifikacijski broj
                    ii. naziv
                    iii. fotografija
                    iiii. njega (ovi podaci se koriste za usporedbu s mjerenjima dobivenih sa senzora te se osnovom njih pokreću željene akcije):
                            1. vlažnost tla – potrebno zalijevanje jednom dnevno/tjedno/mjesečno …
                            2. tamnija ili svjetlija mjesta
                            toplija ili hladnija mjesta
                            3. preporuka za dodavanje supstrata
                b. Evidencija biljaka može se:
                i. dopunjavati podacima o novim biljkama
                ii. ažurirati mijenjanjem podataka o postojećim biljkama
                iii. ažurirati brisanjem podataka o postojećim biljkama

TODO:    4. Evidencija PyFloraPosuda
            Aplikacija treba imati podatke o svim posudama koje su dodane u aplikaciju, kao i o posađenoj biljci u toj posudi.
                a. Podaci koje treba čuvati o posudi su:
                    i. identifikacijski broj
                    ii. naziv – najbolje naziv lokacije. Primjer: „Kuhinja – polica pored prozora.“
                    iii. posađena biljka. Ako ovog podatka nema, onda se posuda smatra praznom i senzori NE šalju podatke, nego posuda ima status „PRAZNA posuda“.
                b. Dohvat podataka sa senzora u posudama.
                c. Lista svih zauzetih posuda. Postoji gumb za proširivanje prikaza na posude koje su slobodne. Klikom na neku posudu otvara se ekran s detaljima o posudi.
                d. Prikaz detalja o svakoj posudi.
                    osim detalja o posudi
                    grafički prikaz mjerenja dobivenih podataka sa senzora
                    prikaz podataka treba biti moguć u minimalno tri oblika (line chart, pie chart, histogram).
                e. Promjena statusa posude:
                    i. ukoliko se posuda pokvarila, korisnik treba moći posudu izbrisati iz sustava
                    ii. ukoliko se želi promijeniti biljka, korisnik može „isprazniti“ posudu i ako želi dodati novu biljku ili jednostavno ostaviti posudu praznom.
TODO:    5. Baza podataka u koju će biti pohranjeni svi podaci. SQLite je sasvim dovoljan za ovaj tip aplikacije, ali ako želite možete koristiti i neku drugu bazu podataka.


The admin view window could have a header with the page title, such as "User Management," and a button to log out or return to the dashboard.

Below the header, the user table could be displayed with columns for Name, Email, Role, and any other relevant information. Each row of the table would represent a different user and include an Edit button and a Delete button.

The Add User button could be located above or to the side of the user table, and be styled differently from the other buttons, perhaps using a contrasting color or a plus sign icon.

To improve navigation, you could include filters or search functionality at the top of the table, allowing the admin to quickly find specific users or groups of users.

Finally, ensure that the user interface is visually appealing and easy to navigate, using a consistent design language throughout the page and including clear and concise labeling for each button.