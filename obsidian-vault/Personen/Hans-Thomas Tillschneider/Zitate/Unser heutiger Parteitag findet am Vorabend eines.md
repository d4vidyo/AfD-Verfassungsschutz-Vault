---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-08-28
topic: Demokratieprinzip
page_bfv: 551
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 28.8.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Unser heutiger Parteitag findet am Vorabend eines großen Raubzuges statt. Die Räuber sitzen in Washington und in Brüssel, ihre Handlanger in Berlin und Magdeburg. Über eine Explosion, über eine Explosion der Energiepreise soll der letzte Rest an Wohlstand, der uns noch geblieben ist, abgesaugt werden. Die Europolitik, die Klimapolitik, die Coronadiktatur und jetzt die Russlandsanktionen - all das hatte und hat zumindest immer auch einen Zweck: die deutschen Bürger verarmen, unsere Freiheit vernichten, Deutschland klein halten. Und die AfD ist die einzige relevante politische Kraft, die noch Widerstand leistet. Wir sind die einzigen, die Deutschland verteidigen. Was 1813 ein Blücher und ein Körner war, was 1871 ein Bismarck war und was 1944 ein Stauffenberg war, das ist 2022 die AfD. Auf unseren Schultern lastet die deutsche Sache! [...] Ob CDU, FDP, SPD, Grüne oder Linke - sie sind alle gleich, sie sind die Helfershelfer der Deutschlandplünderer und wir sind die einzigen, die ihnen einen Strich durch ihre Rechnung machen wollen und deshalb hassen sie uns und grenzen uns aus. [...] Unser Partner, das ist der Widerstand in all seiner Vielseitigkeit und seinem Facettenreichtum. Ich reiche jedem, der in diesen Tagen gegen das Altparteiregime der Deutschlandplünderer auf die Straße geht, die Hand. Frieden, Freiheit, Wohlstand - an erster Stelle Deutschland!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 551

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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