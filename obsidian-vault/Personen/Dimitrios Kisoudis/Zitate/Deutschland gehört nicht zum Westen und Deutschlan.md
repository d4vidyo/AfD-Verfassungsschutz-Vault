---
type: zitat
speaker: "[[Dimitrios Kisoudis]]"
date: 2023-07-30
topic: Menschenwürde
page_bfv: 353
source: 'Rede Europawahlversammlung, Magdeburg'
status: Unbewertet
---

# Zitat: [[Dimitrios Kisoudis]] vom 30.7.2023 veröffentlicht auf: 'Rede Europawahlversammlung, Magdeburg'
> [!quote] Aussage
>Deutschland gehört nicht zum Westen und Deutschland gehört nicht zum Osten. Deutschland ist das Herz von Mitteleuropa und muss zwischen Westen und Osten vermitteln. [...] Und solange wir das nicht erkennen, solange taumeln wir weiter besinnungslos unter der Regenbogenfahne. Solange knien wir nieder vor einem afro-amerikanischen Drogendealer und stammeln ,Black lives matter‘! Schluss damit, wir wollen wieder aufrecht gehen! Europas Zukunft heißt nicht ‚Multikulti‘ und ,Melting Pot', sondern Stolz auf das Eigene und Multipolarität.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 353

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