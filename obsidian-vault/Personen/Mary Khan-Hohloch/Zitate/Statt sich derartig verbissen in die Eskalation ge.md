---
type: zitat
speaker: "[[Mary Khan-Hohloch]]"
date: 2024-12-04
topic: Menschenwürde
page_bfv: 922
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Mary Khan-Hohloch]] vom 4.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Statt sich derartig verbissen in die Eskalation geopolitischer #Konflikte hineinzusteigern, sollte die #EU lieber für den Schutz der eigenen Grenzen sorgen! [...] Die #Ukraine verteidigt ihre Souveränität. Aber warum verwehrt man uns dasselbe? Wer sich nicht um die #Sicherheit und #Integrität der eigenen Grenzen kümmert, sorgt für Chaos, Kriminalität und sozialen Zerfall. Und das ist keine Prognose, sondern eine Bestandsaufnahme. Grenzschutz rettet Leben! #Deutschland muss wieder handlungsfähig werden. Unsere Grenzen müssen kontrolliert und illegale Migration gestoppt werden. #Schengen ist tot und begraben. Dass die EU zum 1. Januar 2025 auch noch Bulgarien in die Freizügigkeit aufzunehmen will, zeigt: Auch das neue Kabinett von der Leyen verfolgt die radikale Migrationspakt-Agenda ungebrochen und ist fest entschlossen, unser #Europa der souveränen Nationen zu einem Siedlungsgebiet zu machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 922

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