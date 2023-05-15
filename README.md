# pyfloraapp
    skinuti MongoDB bazu i MongoDB Compass
    kreirati bazu s imenom "pyflora"
    kroz VSC otvoriti file "pyflora_mongodb.py" pokrenuti run da se obrisu sve kolekcije u bazi i da se kreira samo  "admin" korisnik
    
    racunalo mora biti spojeno na internet
    pokrenuti file "main.py" otvara se login screen
    USERNAME: admin
    PASSWORD: admin

    ADMIN VIEW
        nakon ulogiravanja kao admin, otvara se aplikacija
        dodavanje usera u bazu - klikom na "Add new user" otvara novi prozor u koji se upisuju podatci o korisniku
        brisanje usera - prvo oznaciti usera kojeg zelimo obrisati klikom bilo gdje na redak toga usera, nakon toga kliknuti na "Delete Selected User"
        admin view se gasi na "Close Admin View"

    USER VIEW
        pokrenuti file "main.py" otvara se login screen
        ulogirati se sa dodanim korisnikom koji smo unjeli kroz admin view

        nakon pokretanja aplikacije otvara se prozor u kojem imamo header, sensor & chart frame i plant list & pot list
        
        HEADER
            imamo trenutni datum i vrijeme, te trenutnu temperaturu u gradu Zagrebu, kroz weather api.

        SENSOR & CHART FRAME
            
            SENSOR DATA
                prvi frame prikazuje SENSOR DATA, gdje sam generirao neke podatke i svaki puta pritiskom na tipku "SYNC" generiraju se novi podatci (ideja je da su to trenutni podatci prostorije)

            CHART FRAME
                kod prvog pokretanja imamo dva charta, LIGHT CHART i HUMIDITY CHART, podatci se random generiraju svaki puta kada se pokrene aplikacija iznova, kasnije kada se doda biljka iz baze pojavljuje se jos jedan PIE CHART sa realnim prikazom omjera biljaka koje korisnik posjeduje i koje je korisnik posadio u teglu.

        PLANT LIST
            pritiskom na "Add New Plant" otvara se novi prozor koji povlaci podatke o biljkama iz baze
            da bi dodali biljku iz baze korisniku, oznacimo redak biljke i kliknemo na "Add Plant", mozemo dadavati sve biljke koliko god puta hocemo
            zatvaramo prozor klikom na "Close"

            nakon sto smo dodali nekoliko biljaka u plant listi se pojavljuju biljke sa osnovnim podatcima
            u bazi je kreiran novi collection "user_plant" sa "user_id", "plant_id" i "planted" koji moze biti True (biljka je posađena) ili False (biljka nije posađena)
        
        POT LIST
            dodavanje biljke u pot(sađenje) vrsimo na nacin tako da u prozoru biljke kliknemo na "Add to Pot"
            ta biljka se automatski prebacuje u POT LIST i tretira se kao da je posađena
            u pot listi imamo osnovne podatke biljke i sensor data koji povlaci podatke bas iz te tegle u kojoj se nalazi biljka(podatci se nasumicno generiraju)
            klikom na "Remove From Pot" biljka se brise iz pot liste i vraća u plant listu iz koje je opet mozemo dodati ili obrisati skroz sa trenutnog korisnika

