
# Naslov projekta: Analiza podatkov o prometnih nesrecah v Sloveniji

Opis problema: Prometne nesrece predstavljajo pomemben druzbeni problem, saj lahko povzrocijo veliko materialno skodo, poskodbe ali celo smrt. Namen tega projekta je analizirati podatke o prometnih nesrecah v Sloveniji, da bi lahko identificirali vorce, trende in dejavnike tveganja ter razvili smernice za izbolisanje varnosti na cestah.

Cilji/vprasanja:
1. Kateri so najpogostejsi vroki prometnih nesrec v Sloveniji?
2. Kateri so najbolj ogrozeni udelezenci v prometu?
3. Kako se stevilo prometnih nesrec spreminja skozi cas?
4. Analiza specifičnih vrst nesreč: Nabor podatkov vključuje informacije o vrsti nesreče, tako da je mogoče analizirati, katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim.
5. Kaksna je povezava med razlicnimi dejavniki tveganja (npr. alkohol, prekoractev hitrosti, slaba vidljivost) in verjetnostjo prometne nesrece?

Oblika podatkov:
Podatki so bili zajeti iz spletne strani OPSI (https://podatki.gov.si/dataset/mnzpprometne-nesrece-od-leta-2009-dalje), kjer so na voljo podatki o prometnih nesrecah v Sloveniji za obdobje 2009-2022. Podatki so v obliki CSV datotek, ki vsebujejo podrobne informacije o ZaporednaStevilkaPN, KlasifikacijaNesrece, UpravnaEnotaStoritve, DatumPN, UraPN, VNaselju, Lokacija, VrstaCesteNaselja, SifraCesteNaselja, TekstCesteNaselja, SifraOdsekaUlice, TekstOdsekaUlice, StacionazaDogodka. OpisKraja, VzrokNesrece, TipNesrece, VremenskeOkoliscine, StanjePrometa, StanjeVozisca, VrstaVozisca, GeoKoordinataX, GeoKoordinataY, ZaporednaStevilkaOsebeVPN, Povzrocitelj, Starost, Spol, UEStalnegaPrebivalisca, Drzavljanstvo, PoskodbaUdelezenca, VrstaUdelezenca, UporabaVarnostnegaPasu, VozniskiStazVLetih, VozniskiStazVMesecih, VrednostAlkotesta, VrednostStrokovnegaPregleda. Podatki so med seboj loceni s ";", zato ji je najprej potrebno med seboj ločiti in ustrezno oblikovati.

Analiza podatkov je potekala po oblikovanih ciljih, kjer smo z ustreznimi vizualizacijskimi orodi prikazali ugotovitve ciljev.

Raziskava prometnih nesreč v Sloveniji med leti 2009 in 2022 je temeljila na analizi zbranih podatkov.

V raziskavi so bili analizirani vzroki prometnih nesreč, udeleženci nesreč in njihove starostne skupine ter različne vrste udeležencev v prometu. Podrobna analiza podatkov je razkrila, da so najpogostejši vzroki nesreč premik z vozilom, neprilagojena hitrost, nepravilna smer vožnje, neupoštevanje pravil prednosti in neustrezna varnostna razdalja.

1. Zanimalo nas je, kateri so najpogostejši vzroki za nastanek prometne nesreče. Najpogostejši vzrok nesreče je bil premik z vozilom, ki je prispeval k 25% vseh nesreč. Ta vzrok je lahko povezan s preveliko hitrostjo, neupoštevanjem pravil prednosti, neustrezno varnostno razdaljo ali nepravilno smerjo vožnje. Neprilagojena hitrost je bila drugi najpogostejši vzrok (18%), kar lahko nakazuje na prehitro in nevarno vožnjo ter pomanjkanje spoštovanja cestnih predpisov. Na tretjem mestu je bila nepravilna smer vožnje (16%), kar kaže na potrebo po večjem poznavanju prometnih predpisov in pravilne uporabe cest. Neupoštevanje pravil prednosti (15%) in neustrezna varnostna razdalja (11%) sta prav tako pogosti vzroki, ki lahko kažejo na slabo poznavanje cestnih predpisov in nespoštovanje drugih udeležencev v prometu.
![Top 10 vzrokov nesrec](https://github.com/UrhPercic/PR22UMZ/assets/56612694/81e0529d-53c9-4cdc-8622-d98da0bbffcb)


Nadaljnja analiza podatkov je pokazala, da so najpogostejši povzročitelji prometnih nesreč stari med 19 in 33 leti, najpogostejši udeleženci pa so stari med 19 in 48 let. Moški so se v nesreče vpleli dvakrat pogosteje kot ženske. Osebni avtomobili so bili daleč najpogostejša vrsta udeležencev v nesrečah, nato vozila tovornjakov, potniki, kolesarji in vozniki motornih koles.

2.1. Najpogostejši povzročitelji nesreč so bili v starostnih skupinah med 19 in 23 leti ter med 24 in 28 leti. To nakazuje, da mlajši vozniki morda potrebujejo več usposabljanja in izkušenj za varno vožnjo, ki bi jim lahko pomagale preprečiti nesreče. Starostne skupine med 29 in 33 leti, med 34 in 38 leti ter med 44 in 48 leti so bile tudi pogosti povzročitelji nesreč, kar kaže, da lahko nevarne vožnje vplivajo na vse starostne skupine, ne le na mlajše.
![povzrocitelji v pn po starosti](https://github.com/UrhPercic/PR22UMZ/assets/56612694/a07bda4c-98c5-4b7b-a255-1fde2ca2305c)

2.2. Najpogostejši udeleženci nesreč so bili v starostnih skupinah med 29 in 33 leti, med 34 in 38 leti ter med 24 in 28 leti. To kaže na potrebo po večji ozaveščenosti in usposabljanju teh starostnih skupin za varno vožnjo ter upoštevanje cestnih predpisov. Starostne skupine med 39 in 43 leti ter med 44 in 48 leti so tudi pogosti udeleženci nesreč, kar kaže na to, da je varna vožnja pomembna za vse starosti.
![udelezenci v pn po starosti](https://github.com/UrhPercic/PR22UMZ/assets/56612694/155381a9-cdec-4300-ad12-cc79cfbd053a)

2.3. Iz naše raziskave smo ugotovili, da so moški okoli 75% časa povzročitelji prometnih nesreč, prav tako pa so večkrat le udeleženi v prometne nesreče (okoli 65%). 
![NajPovzrociteljiSpol](https://github.com/UrhPercic/PR22UMZ/assets/56612694/f07aa5c4-f7f8-4731-b06b-8d0e9617d542)
![NajOgrozenciSpol](https://github.com/UrhPercic/PR22UMZ/assets/56612694/a22c6ee5-2877-48e5-87fb-08a1410eee23)

2.4. Daleč največ vrst udeležencev v prometnih nesrečah je bilo osebnih avtomobilov, nato vozniki tovornega vozila, potniki, ostalo, kolesarji, vozniki motornega kolesa.
Iz podatkov lahko vidimo, da so osebni avtomobili najpogostejši udeleženci prometnih nesreč v Sloveniji. Vozniki osebnih avtomobilov predstavljajo največjo skupino udeležencev, kar ni presenetljivo, saj je ta vrsta vozila najbolj razširjena v Sloveniji. Sledijo jim vozniki tovornih vozil, ki so pogosto prisotni na naših cestah zaradi dejstva, da Slovenija leži na pomembni tranzitni poti med zahodno Evropo in vzhodno Evropo. Prav tako so pogosto prisotni tudi potniki, ki potujejo z osebnimi avtomobili ali tovornimi vozili. Kolesarji in vozniki motornih koles so manjši delež v prometnih nesrečah, vendar pa so zaradi svoje ranljivosti bolj izpostavljeni tveganju resnih poškodb ali smrti.
![NajOgrozenciVrstaUdel](https://github.com/UrhPercic/PR22UMZ/assets/56612694/093cb58f-e817-4a05-85aa-46fd6d779ace)


3. Spraševali smo se, kako se število nesreč spreminja skozi
i čas kjer smo vzeli CSV datoteke nesreč od 2009-2021. Podatke o nesrečah smo združevali po mesecih. Ugotovili smo, da se nesreče večkrat pojavljajo poleti. 

![image](https://user-images.githubusercontent.com/125819680/232486704-217a806c-8398-4e4e-8ae6-5fb1b05ae92d.png)

Ugotovili smo tudi, da se čez poleten čas se nesreče dogajajo zaradi neupoštevanja pravil prednosti, med tem, ko se pozimi dogajajo zaradi neprilagojene hitrosti.

![image](https://user-images.githubusercontent.com/125819680/232504617-90d88b4f-3c9a-4b22-8d77-a67f1b8a9e02.png)


4. Spraševali smo se katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim. Podatke smo grupirali po vzroku nesreče in potem po posledici nesreče. Ugotovili smo, da se večina nesreč konča z materialno škodo, zaradi neustreznih premikov s vozilom. Največ smrti in resnih telesnih poškodb pa so posledice prehitre vožnje.

![image](https://user-images.githubusercontent.com/125819680/232487195-e5c5a0f4-1696-406a-a66a-f4734cfb2a4d.png)


5. Ugotavljali smo tudi vpliv alkohola na nesreče glede na preteklo prisotnost alkohola pri nesrečah, kjer opazimo, da je relativno majhen procent nesreč pod vplivom alkohola.

<img width="866" alt="Screenshot 2023-04-18 at 18 24 47" src="https://user-images.githubusercontent.com/126070502/232864917-a6a340f3-5a53-49ea-8f26-3f3bd9169d01.png">

Pregledovali so tudi povezavo vozne podlage z pogostostjo nesreč.

<img width="918" alt="Screenshot 2023-04-18 at 19 00 28" src="https://user-images.githubusercontent.com/126070502/232865297-056fe2fa-9e03-4c3b-8f0a-96f33cc3976a.png">

Pri opazovanju nesreč glede na stanje cestišča presenetljivo ugototivmo da se večino nesreč zgodi na suhih cestah.

<img width="967" alt="Screenshot 2023-04-18 at 19 50 25" src="https://user-images.githubusercontent.com/126070502/232865466-995838a0-4658-4680-8926-41324259b38a.png">

Za promet pa smo ugotovili da ne vliva veliko na verjetnost nesreče, saj je relativno dobro razporejeno čez vse kategorije.

<img width="788" alt="Screenshot 2023-04-18 at 20 01 15" src="https://user-images.githubusercontent.com/126070502/232865626-54da58ed-a544-4c40-858f-b40b62bf6d79.png">

