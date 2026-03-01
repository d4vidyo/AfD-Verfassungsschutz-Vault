---
type: zitat
speaker: "[[Günter Geng]]"
date: 2021-05-24
topic: Menschenwürde
page_bfv: 526
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Günter Geng]] vom 24.5.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gerade war ich auf der Gaß, wollte was essen. Es war so, wie mir meine Großeltern erzählten, wie es damals vor über 80 Jahren war. Man wollte eine Art 'Ariernachweis' von mir sehen - es klang auch wie 'man verkaufe nichts an Juden'. Auf NEUDEUTSCH meint das natürlich den Impfausweis, den Corona-Test oder die Genesenen- Bescheinigung. Ohne sowas gibt es keinen Sitzplatz - keine Speisen oder Getränke. Ich sehe da kaum einen Unterschied mehr, zwischen der 'Merkulatur' und dem Dritten Reich. Was kommt als Nächstes? Wenn doppelt Geimpfte erneut an Corona erkranken, Geimpfte an den Folgen versterben - was ist denn das für eine RNA-Vakzin-Plörre? Oder ist es gar eine Art 'Euthanasie- Programm'?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 526

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