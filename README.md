# who-will-empty-the-dishwasher

Konec nenápadného vyčkávání na to, jestli se myčka vyklidí sama, nebo je to na vás. Tento skript po skončení mycího cyklu povolá osud (rozuměj náhodu), který rozhodne o tom, který člen domácnosti má dnes tuto činnost na starost. 

Skončení mycího cyklu --> IFTTT připíše do Google Sheets nový řádek --> Skript choose_servant.py zjistí nový řádek --> Spustí se proces vybrání pracovníka --> Připsání nového řádku do srovnávacího seznamu

Nezbytné je mít chytrou myčku nádobí, která vás skrze aplikaci upozorní, že už má svou práci hotovou. Tuto aplikaci spárujte s aplikací IFTTT. Ačkoliv free funkce IFTTT, které by umožňovaly spouštění vlastních skriptů, byly před pár lety téměř eliminovány, tak stále umožňuje připsání dat do dokumentu Google Sheets ve vašem Google Drivu. V aplikaci IFTTT nastavte, aby se do dokumentu G. Sheets zanesl nový řádek pokaždé, když myčka domyje. Skript předpokládá, že text na přidaných řádcích bude začínat ## a končit ** (např. ##CreatedAt**). Tento jeden dokument je nutné nastavit jako veřejně přístupný, aby do něj mohl skript nahlédnout a zjistit, jestli do něho nepřibyl nový řádek. V cronu mám nastaveno, aby se skript spouštěl každých 10 minut. Výsledek rozhodovacího procesu je zaslán na email všech adeptů.
