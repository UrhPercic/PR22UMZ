
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

1. Zanimalo nas je, kateri so najpogostejši vzroki za nastanek prometne nesreče. Ugotovili smo, da so to premiki z vozilom, neprilagojena hitrost in neupoštevanja pravil o prednosti.

![Top 10 vzrokov nesrec](https://user-images.githubusercontent.com/56612694/232814758-0d2b1ba5-52b8-40a0-b777-ccbec0b12e8b.png)

2.1. Ugotovili smo, da so največji ogroženci v prometu po starosti med 25 in 29 let, med 30 in 34 ter med 20 in 24. Glede na raziskavo bi lahko rekli, da so največji
udeleženci prometnih nesreč med starostjo 21 in 30 let.
![NajOgrozenciStarost](https://github.com/UrhPercic/PR22UMZ/assets/56612694/2229aab7-f74a-4781-ba30-980837850f58)

2.2. Ugotiili smo, da je za skoraj polovico več udeležencev v prometnih nesrečah v Sloveniji med letom 2009 in 2022 bilo moškega spola.

![NajOgrozen![NajOgrozenciSpol](https://github.com/UrhPercic/PR22UMZ/assets/56612694/aa2e8b1a-1594-4e3e-8aee-927ebed17325)


2.3. Glede na vrsto udeležencev v prometnih nesrečah je bilo daleč največ udeležencev v voznikov osebnih avtomobilov, voznikov tovornih vozil ter potnikov.

![NajOgrozenciVrstaUdel](https://user-images.githubusercontent.com/56612694/232815058-ca73975e-1829-461e-ba69-14c6beabedcf.png)


Spraševali smo se, kako se število nesreč spreminja skozi
i čas kjer smo vzeli CSV datoteke nesreč od 2009-2021. Podatke o nesrečah smo združevali po mesecih. Ugotovili smo, da se nesreče večkrat pojavljajo poleti. 

![image](https://user-images.githubusercontent.com/125819680/232486704-217a806c-8398-4e4e-8ae6-5fb1b05ae92d.png)

Ugotovili smo tudi, da se čez poleten čas se nesreče dogajajo zaradi neupoštevanja pravil prednosti, med tem, ko se pozimi dogajajo zaradi neprilagojene hitrosti.

![image](https://user-images.githubusercontent.com/125819680/232504617-90d88b4f-3c9a-4b22-8d77-a67f1b8a9e02.png)


Spraševali smo se katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim. Podatke smo grupirali po vzroku nesreče in potem po posledici nesreče. Ugotovili smo, da se večina nesreč konča z materialno škodo, zaradi neustreznih premikov s vozilom. Največ smrti in resnih telesnih poškodb pa so posledice prehitre vožnje.

![image](https://user-images.githubusercontent.com/125819680/232487195-e5c5a0f4-1696-406a-a66a-f4734cfb2a4d.png)


Ugotavljali smo tudi vpliv alkohola na nesreče glede na preteklo prisotnost alkohola pri nesrečah, kjer opazimo, da je relativno majhen procent nesreč pod vplivom alkohola.

<img width="866" alt="Screenshot 2023-04-18 at 18 24 47" src="https://user-images.githubusercontent.com/126070502/232864917-a6a340f3-5a53-49ea-8f26-3f3bd9169d01.png">

Pregledovali so tudi povezavo vozne podlage z pogostostjo nesreč.

<img width="918" alt="Screenshot 2023-04-18 at 19 00 28" src="https://user-images.githubusercontent.com/126070502/232865297-056fe2fa-9e03-4c3b-8f0a-96f33cc3976a.png">

Pri opazovanju nesreč glede na stanje cestišča presenetljivo ugototivmo da se večino nesreč zgodi na suhih cestah.

<img width="967" alt="Screenshot 2023-04-18 at 19 50 25" src="https://user-images.githubusercontent.com/126070502/232865466-995838a0-4658-4680-8926-41324259b38a.png">

Za promet pa smo ugotovili da ne vliva veliko na verjetnost nesreče, saj je relativno dobro razporejeno čez vse kategorije.

<img width="788" alt="Screenshot 2023-04-18 at 20 01 15" src="https://user-images.githubusercontent.com/126070502/232865626-54da58ed-a544-4c40-858f-b40b62bf6d79.png">

