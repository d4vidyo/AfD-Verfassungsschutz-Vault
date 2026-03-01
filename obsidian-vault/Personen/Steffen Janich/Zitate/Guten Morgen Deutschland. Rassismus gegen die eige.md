---
type: zitat
speaker: "[[Steffen Janich]]"
date: 2023-09-03
topic: Demokratieprinzip
page_bfv: 640
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Steffen Janich]] vom 3.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Guten Morgen Deutschland. Rassismus gegen die eigene Bevölkerung ist das Ergebnis und der Auswuchs einer völlig verfehlten Migrationspolitik in unserem Land durch die Bundesregierung und die Regierungen der Länder. Während durch die desaströse Innenpolitik der Nancy Faeser täglich neue Menschen illegal in unser Land eindringen, grenzen mittlerweile links-grüne Organisationen Menschen im eigenen Land aus. Wir sagen, Schluss mit diesem sozialistischen Kurs dieser Deutschland-Hasser, holen wir unser Land zurück.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 640

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