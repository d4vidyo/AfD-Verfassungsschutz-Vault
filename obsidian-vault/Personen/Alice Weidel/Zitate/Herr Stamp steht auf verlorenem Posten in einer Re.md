---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2022-12-16
topic: Menschenwürde
page_bfv: 358
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 16.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Herr Stamp steht auf verlorenem Posten in einer Regierung, die alles tut, um irreguläre Migration nach Deutschland und in die deutschen Sozialsysteme zu ermuntern und anzuheizen, die mit der Verramschung der deutschen Staatsbürgerschaft vollendete Tatsachen schafft und großzügig Aufenthaltstitel an Migranten verteilt, die von Rechts wegen längst hätten gehen müssen.[...] Trotz millionenfacher Netto-Einwanderung herrscht Arbeitskräftemangel, die mit nicht integrationsfähigen Migranten gefluteten Sozialsysteme stehen vor dem Kollaps, und die innere Sicherheit löst sich in einem Klima der alltäglichen Migrantengewalt und der Terrorisierung der Bevölkerung durch angebliche ‚Schutzsuchende‘ auf. Der Kipppunkt, hinter dem eine Korrektur dieser unhaltbaren Verhältnisse nicht mehr möglich ist, steht unmittelbar bevor.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 358

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