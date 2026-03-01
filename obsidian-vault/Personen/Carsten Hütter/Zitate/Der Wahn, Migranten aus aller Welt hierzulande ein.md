---
type: zitat
speaker: "[[Carsten Hütter]]"
date: 2023-02-28
topic: Menschenwürde
page_bfv: 365
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carsten Hütter]] vom 28.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Wahn, Migranten aus aller Welt hierzulande ein Nest auf Steuerzahlerkosen zu bauen und dafür die eigenen Bürger mit Füßen zu treten, hat damit einen neuen, traurigen Höhepunkt erreicht. [...] Die Verdrängung von Mietern zugunsten von vermeintlichen Flüchtlingen gewinnt System. Dass es auch die Schwächsten trifft, ist besonders bitter. Denn die rausgeworfenen Senioren haben dieses Land mit aufgebaut - und sie haben den Wohlstand erarbeitet, der nun von der Ampel und ihren Mittätern so großzügig an andere verschenkt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 365

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