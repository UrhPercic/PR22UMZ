
# Naslov projekta: Analiza podatkov o prometnih nesrecah v Sloveniji

Opis problema: Prometne nesrece predstavljajo pomemben druzbeni problem, saj lahko povzrocijo veliko materialno skodo, poskodbe ali celo smrt. Namen tega projekta je analizirati podatke o prometnih nesrecah v Sloveniji, da bi lahko identificirali vorce, trende in dejavnike tveganja ter razvili smernice za izbolisanje varnosti na cestah.

Cilji/vprasanja:
1. Kateri so najpogostejsi vroki prometnih nesrec v Sloveniji?
2. Kateri so najbolj ogrozeni udelezenci v prometu?
3. Kako se stevilo prometnih nesrec spreminja skozi cas?
4. Analiza specifičnih vrst nesreč: Nabor podatkov vključuje informacije o vrsti nesreče, tako da je mogoče analizirati, katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim.
5. Kaksna je povezava med razlicnimi dejavniki tveganja (npr. alkohol, prekoractev hitrosti, slaba vidljivost) in verjetnostjo prometne nesrece?
6. Kako se razlikujejo posledice prometnih nesrec glede na dejavnike tveganja in udelezence v prometu?

Oblika podatkov:
Podatki so bili zajeti iz spletne strani OPSI (https://podatki.gov.si/dataset/mnzpprometne-nesrece-od-leta-2009-dalje), kjer so na voljo podatki o prometnih nesrecah v Sloveniji za obdobje 2009-2022. Podatki so v obliki CSV datotek, ki vsebujejo podrobne informacije o ZaporednaStevilkaPN, KlasifikacijaNesrece, UpravnaEnotaStoritve, DatumPN, UraPN, VNaselju, Lokacija, VrstaCesteNaselja, SifraCesteNaselja, TekstCesteNaselja, SifraOdsekaUlice, TekstOdsekaUlice, StacionazaDogodka. OpisKraja, VzrokNesrece, TipNesrece, VremenskeOkoliscine, StanjePrometa, StanjeVozisca, VrstaVozisca, GeoKoordinataX, GeoKoordinataY, ZaporednaStevilkaOsebeVPN, Povzrocitelj, Starost, Spol, UEStalnegaPrebivalisca, Drzavljanstvo, PoskodbaUdelezenca, VrstaUdelezenca, UporabaVarnostnegaPasu, VozniskiStazVLetih, VozniskiStazVMesecih, VrednostAlkotesta, VrednostStrokovnegaPregleda. Podatki so med seboj loceni s ";", zato ji je najprej potrebno med seboj ločiti in ustrezno oblikovati.

Analiza podatkov je potekala po oblikovanih ciljih, kjer smo z ustreznimi vizualizacijskimi orodi prikazali ugotovitve ciljev.

Spraševali smo se, kako se število nesreč spreminja skozi čas kjer smo vzeli CSV datoteke nesreč od 2009-2021. Podatke o nesrečah smo združevali po mesecih. Ugotovili smo, da se nesreče večkrat pojavljajo poleti. 

![image](https://user-images.githubusercontent.com/125819680/232486704-217a806c-8398-4e4e-8ae6-5fb1b05ae92d.png)

Spraševali smo se katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim. Podatke smo grupirali po vzroku nesreče in potem po posledici nesreče. Ugotovili smo, da se večina nesreč konča z materialno škodo, zaradi neustreznih premikov s vozilom. Največ smrti in resnih telesnih poškodb pa so posledice prehitre vožnje.

![image](https://user-images.githubusercontent.com/125819680/232487195-e5c5a0f4-1696-406a-a66a-f4734cfb2a4d.png)
