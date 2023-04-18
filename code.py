
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Kako se stevilo prometnih nesrec spreminja skozi cas?
# Analiza specifičnih vrst nesreč: Nabor podatkov vključuje informacije o vrsti nesreče, tako da je mogoče analizirati,
# katere vrste nesreč so najpogostejše, katere so najbolj nevarne in kateri dejavniki prispevajo k njim.

datoteke = ["pn2009", "pn2010", "pn2011", "pn2012", "pn2013", "pn2014", "pn2015", "pn2016", "pn2017", "pn2018", "pn2019", "pn2020", "pn2021", "pn2022"]
def nesrece_skozi_cas():
    nesrece_datum = {}
    for datoteka in datoteke:
        with open(f'C:\\Users\\urhpe\\PycharmProjects\\Seminarska_TUP\\nesrece\\{datoteka}.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                mesec = int(row[0].split(";")[3].split(".")[1])
                nesrece_datum[mesec] = nesrece_datum.get(mesec, 0) + 1

    nesrece_datum_sorted = {k: v for k, v in sorted(nesrece_datum.items(), key=lambda item: int(item[0]))}
    meseci = list(nesrece_datum_sorted.keys())
    stevila_nesrec = list(nesrece_datum_sorted.values())

    meseci_str = [str(m).zfill(2) for m in meseci]

    plt.bar(meseci_str, stevila_nesrec)
    plt.title("Število nesreč po mesecih (2009-2022)")
    plt.xlabel("Mesec")
    plt.ylabel("Število nesreč")
    plt.show()


def vzroki_skozi_cas():
    vzroki_datum = {}
    for datoteka in datoteke:
        with open(f'C:\\Users\\urhpe\\PycharmProjects\\Seminarska_TUP\\nesrece\\{datoteka}.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                row_split = (row[0] + row[1]).split(";")
                mesec = int(row_split[3].split(".")[1])
                Vzrok = row_split[14]
                count = 1
                if mesec in vzroki_datum and Vzrok in vzroki_datum[mesec] and Vzrok != "PREMIKI Z VOZILOM":
                    count = vzroki_datum[mesec][Vzrok] + 1
                vzroki_datum.setdefault(mesec, {}).update({Vzrok: count})

    max_vzrok_mesec = {}
    for mesec, vzroki in vzroki_datum.items():
        max_vzrok = max(vzroki, key=lambda k: vzroki[k])
        max_vzrok_mesec[mesec] = max_vzrok

    max_vzrok_mesec_sorted = {k: v for k, v in sorted(max_vzrok_mesec.items(), key=lambda item: int(item[0]))}
    meseci = {1:"januar", 2:"februar", 3:"marec", 4:"april", 5:"maj", 6:"junij", 7:"julij", 8:"avgust", 9:"november", 10:"oktober", 11:"november", 12:"december"}
    for mesec, vzrok in max_vzrok_mesec_sorted.items():
        print(f"{meseci[mesec]}: {vzrok}")


def nesrece_vzroki():
    vzroki = {}
    klasifikacije = set()
    for datoteka in datoteke:
        with open(f'C:\\Users\\urhpe\\PycharmProjects\\Seminarska_TUP\\nesrece\\{datoteka}.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                row_split = (row[0] + row[1]).split(";")
                Vzrok = row_split[14]
                KlasifikacijaNesrece = row_split[1]
                klasifikacije.add(KlasifikacijaNesrece)

                if (Vzrok, KlasifikacijaNesrece) not in vzroki:
                    vzroki[(Vzrok, KlasifikacijaNesrece)] = 1
                else:
                    vzroki[(Vzrok, KlasifikacijaNesrece)] += 1

    vzroki_df = pd.DataFrame(list(vzroki.items()), columns=['Vzrok, KlasifikacijaNesrece', 'Število nesreč'])
    vzroki_df[['Vzrok', 'KlasifikacijaNesrece']] = pd.DataFrame(vzroki_df['Vzrok, KlasifikacijaNesrece'].tolist(), index=vzroki_df.index)

    plt.figure(figsize=(12, 26))
    sns.set_style("darkgrid")
    ax = sns.barplot(x="Vzrok", y="Število nesreč", hue='KlasifikacijaNesrece', hue_order=list(klasifikacije), data=vzroki_df)
    ax.set_title("Vzroki prometnih nesreč")
    ax.set_xlabel("Vzrok")
    ax.set_ylabel("Število nesreč")
    plt.xticks(rotation=90)
    plt.show()

vzroki_skozi_cas()
