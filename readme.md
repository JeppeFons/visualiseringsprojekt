1. Forstå datastrukturen

fokus på CO2 udslip

Starter med at danne overblik:

Hvilke typer variable er der? (numeriske, kategoriske, binære, datoer, tekst, etc.)

Hvad er antallet af rækker og kolonner?

Er der manglende værdier?

Unikke værdier per kolonne (fx antal unikke køn, eller antal unikke aldersgrupper)



2. Univariatanalyse (én variabel ad gangen)

beskriver fordelingen af hver enkelt variabel:

For numeriske variable:

Middelværdi, median, kvartiler, standardafvigelse

Histogrammer, boxplots

Er fordelingen skæv? Normal?

For kategoriske variable:
Frekvenstabeller (værditællinger)

Bar plots


3. Bivariatanalyse (to variable ad gangen)

interaktioner eller sammenhænge mellem variable. Giver ofte tidlige indsigter i interessante mønstre.

Eksempler:

Numerisk vs numerisk: scatterplots, korrelationsmatrix

Kategorisk vs numerisk: boxplots, gruppegennemsnit

Kategorisk vs kategorisk: krydstabeller, stacked bar plots

Python-eksempel på korrelationsmatrix:

import seaborn as sns
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')

4. Undersøg outliers og fejl

Finder usædvanlige værdier (ekstremværdi eller tasteslips)

Bruger boxplots eller z-score til numeriske variable

Er der værdier, som ikke giver mening (f.eks. negativ alder)?

5. Lav meningsfulde grupperinger

Hvis der er mange unikke kategorier, kan nogle grupperes?

lav numeriske variable i intervaller (fx alder i grupper)?

6. Dokumentér dine fund

Notér interessante observationer, anomalier, trends

Lav evt. en lille rapport med plots og beskrivelser



data:
https://www.kaggle.com/datasets/michaelmatta0/global-development-indicators-2000-2020 