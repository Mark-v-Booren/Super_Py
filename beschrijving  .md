Amsterdam 19-05-2023

     _____  __  __  _____  _____  _____  _____  __  __
    /    /|/ /|/ /|/    /|/    /|/    /|/    /|/ /|/ /|
   /  __/ / / / / /  / / /  __/ /  / / /  / / / / / / |
  /__  /|/ / / / /  / / /  __/|/  / / /  / / / /_/ / /
 /    / / /_/ / / ___/ /    /|/   _/ / ___/ /__   / /
/____/ /_____/ /_/|  |/____/ /_/|_| /_/|  | | /_ / /
|    | |     | | ||__||    | | || | | ||__|/|_| | /
|____|/|_____|/|_|/   |____|/|_||_|/|_|/      |_|/



Technische Elementen van Superpy:

Command-Line Interface (CLI) met Argument Parsing:
De code maakt gebruik van de argparse-module om een command-line interface (CLI) te creëren voor het beheren van producten in het in_stock.csv-bestand. Hiermee kunnen gebruikers verschillende commando's uitvoeren, zoals het toevoegen van producten, het verkopen van producten, het genereren van rapporten en het controleren van verlopen producten. De argparse-module helpt bij het parseren van command-line argumenten en opties, waardoor de code interactiever en gebruiksvriendelijker wordt.
De keuze om een CLI met argument parsing te implementeren biedt een gestructureerde en gestandaardiseerde manier voor gebruikers om met het programma te communiceren. Het maakt het eenvoudig om verschillende functionaliteiten uit te voeren zonder de code rechtstreeks te hoeven wijzigen. Door gebruik te maken van command-line argumenten kunnen gebruikers invoer en opties opgeven voor diverse operaties, waardoor de flexibiliteit en bruikbaarheid van het programma worden vergroot.

CSV-bestandshandling en Gegevensmanipulatie:
De code bevat functies om CSV-bestanden (in_stock.csv en sold.csv) te maken en te beheren waarin productgegevens worden opgeslagen. Functies zoals create_csv, display_csv_in_stock en display_csv_sold tonen het verwerken en weergeven van CSV-gegevens in tabelvorm met behulp van de csv-module en de Table-klasse van de rich-library.
Door CSV-bestanden als opslagformaat voor gegevens te gebruiken, maakt de code het eenvoudig om productinformatie op te slaan en te manipuleren. Het maakt efficiënt lezen, schrijven en wijzigen van gegevens mogelijk. Het gebruik van tabulaire weergave met behulp van de rich-library verbetert de visuele presentatie van productinformatie.

Over het geheel genomen tonen deze technische elementen de mogelijkheid van de code om een command-line interface te bieden voor het beheren van productgegevens, het verwerken van CSV-bestanden en het effectief manipuleren van datums. Ze verbeteren de functionaliteit, flexibiliteit en bruikbaarheid van het programma, waardoor het een veelzijdige tool is voor het beheren van productinventaris en het genereren van rapporten.

De opdracht Super-py was een mooie uitdaging.
Omdat er veel requirements bij kwamen kijken duurde het even voor het mij duidelijk werd wáár te beginnen.
Ik had een lange start om de eerste argsparse opdracht werkende te krijgen : dit kwam waarschijnlijk door mijn configuratie op mijn eigen pc.
Vanuit de de terminal van visual studio moet ik toch steeds het hele path aanmaken voor elk command :

in plaatse van:  
python main.py --report profit
Moet ik schrijven:
C:/Users/Foxlox/AppData/Local/Programs/Python/Python311/python.exe c:/Winc/superpy/main.py --report profit

Omdat deze opdracht gebruikt maakt van CSV files wist ik dat ik de code zó wilde schrijven dat de csv files aangemaakt worden
wanneer de .py file gestart worden. 

De logica van argparse en subparser kostte veel tijd maar eenmaal werkende ging de coderen al sneller.
De opdracht kent veel 'mogelijkheden' en daardoor was het erg moeilijk het simpel te houden en de opdracht toch af te ronden en in te leveren. 
Bij de expire date functie heb ik gekozen dat er een datum kan worden opgegeven zodat er ook eventueel gekeken kan worden wat er morgen of overmorgen 
als houdbaarheidsdatum geldt. Zo kan de supermarkt kiezen wat er wél en niet in de aanbieding zou kunnen!

 def check_expired_products(file):
    print ('hi')
    # # Read the contents of the CSV file
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        # field_names = reader.fieldnames
        products = list(reader)
    # # Get the current date or a date in the future
    date_now = input("Enter the current date (YYYY-MM-DD): ")

    expired_products = []
    for product in products:
        expire_date_str = product['exp-date']
        if expire_date_str < date_now:
            expired_products.append(product)
            print(f'product {expired_products} == expired! ')
        else:
            print('all good!')


