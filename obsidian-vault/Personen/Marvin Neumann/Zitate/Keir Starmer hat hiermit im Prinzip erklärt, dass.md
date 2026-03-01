---
type: zitat
speaker: "[[Marvin Neumann]]"
date: 2024-11-29
topic: Menschenwürde
page_bfv: 891
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Marvin Neumann]] vom 29.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Keir Starmer hat hiermit im Prinzip erklärt, dass der Große Austausch – also die Transformation Großbritanniens in eine mit Massenmigration demographisch und ethnographisch transformierte, globalistische ("global Britain") Siedlungszone – absichtliche Politik der Konservativen und Motiv hinter Brexit gewesen sei. Ausgerechnet Starmer, der Mann, dessen Regierung vor wenigen Wochen noch etliche Engländer für genau solche Meinungen eingesperrt hat. Das ist natürlich vor allem nur der Versuch, sich und seine Partei von der Verantwortung für das Migrationschaos reinzuwaschen, aber dass jetzt von links (!) mit diesem Narrativ gearbeitet wird, ist schon eine Zäsur.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 891

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