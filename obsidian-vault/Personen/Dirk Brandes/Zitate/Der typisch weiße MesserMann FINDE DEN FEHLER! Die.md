---
type: zitat
speaker: "[[Dirk Brandes]]"
date: 2024-06-28
topic: Menschenwürde
page_bfv: 304
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dirk Brandes]] vom 28.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der typisch weiße MesserMann FINDE DEN FEHLER! Die Polizei Hannover zeigt in einer an Lächerlichkeit grenzenden Show, wie sie mit einem 'Messermann' fertig wird. Der böse ,Messerstecher' ist WEISS, MÄNNLICH, heißt ,MATZE' und befolgt artig alle Befehle. Geht’s eigentlich noch unrealistische.???

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 304

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