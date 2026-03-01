---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-10-18
topic: Menschenwürde
page_bfv: 359
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 18.10.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Zahl der Sozialmigranten, die in das gelobte Land Deutschland strömen, ist in den letzten Monaten sprunghaft angestiegen. [...] Hinzu kommen noch rund 1 Millionen Flüchtlinge aus der Ukraine, von denen viele echten Schutz suchen, einige aber leider aktiven Sozialtourismus betreiben und sich am Selbstbedienungsladen der Bundesrepublik bereichern [...] Während Millionen Deutsche in diesem Winter vermutlich frieren müssen, werden die Migranten wieder von der Bundesregierung voll versorgt. Deshalb machen sich täglich tausende kulturfremde Menschen über den Balkan auf den Weg in die Bundesrepublik. [...] Die Grenzen müssen endlich dichtgemacht werden, unser Grenzschutz muss massiv verstärkt werden. [...] Wir müssen von einem Sozialparadies für Nicht-Schutzbedürftige zu einer Asylwüste werden - Festung Europa!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 359

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