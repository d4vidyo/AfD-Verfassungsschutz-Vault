---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-09-09
topic: Menschenwürde
page_bfv: 235
source: 'Beitrag auf afd-fraktion-sachsen.de'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 9.9.2023 veröffentlicht auf: 'Beitrag auf afd-fraktion-sachsen.de'
> [!quote] Aussage
>Verdrängung durch Massenmigration – Deutschland, das Land der Deutschen? [...] Deutschland hat sich in den letzten Jahren allerdings zum zweitgrößten Einwanderungsland der Welt entwickelt, nur knapp hinter den USA. Allein im vergangenen Jahr, 2022, wurde laut Statistischem Bundesamt mit knapp 1,5 Millionen Zuzügen die höchste Nettozuwanderung seit 1950 verzeichnet Die meisten Zuzüge entfielen auf Migranten aus Syrien, Afghanistan und dem Irak. Also aus Ländern mit komplett anderen Kulturen als der unseren. Ihre Religion, den Islam, bringen die Einwanderer mit. Inzwischen werden in Deutschland Moscheen gefühlt schneller gebaut, ab marode Schulen Brücken und Straßen saniert werden. in vielen Städten ruft bereits der Muezzin zum Gebet, das Straßenbild wird zunehmend von verschleierten Frauen geprägt. Freiheitsrechte der Frauen gibt es im Islam so gut wie nicht, Homosexualität wird in diesen Ländern brutal, teils mit dem Tode bestraft. [...] Einwanderer die sich in Deutschland integrieren, die unsere Sprache sprechen und unsere kulturellen Regeln annehmen, sind in Deutschland willkommen. Leider sind solche Einwanderer- gerade wenn sie aus muslimischen Ländern kommen - in der Minderheit, wie die sich entwickelnden Parallelgesellschaften beweisen. 'Der rosarote Elefant im Raum' ist eine Metapher für ein offensichtliches Problem, das zwar mitten im Raum steht, aber dennoch nicht angesprochen wird. Dieser Elefant ist die Frage nach dem Erhalt unseres deutschen Volkes als Kulturnation.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 235

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```