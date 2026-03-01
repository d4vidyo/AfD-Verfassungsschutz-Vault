---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2024-12-30
topic: Menschenwürde
page_bfv: 918
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 30.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Aber wir sehen, das ist die Frucht der Saat, die die Altparteien über Jahre und Jahrzehnte in Deutschland gesät haben. Und wir schauen jetzt ins neue Jahr. Wir werden nicht länger ruhen. Und wir werden alles daran setzen, dass wir diese Politik der multikulturellen Umgestaltung Deutschlands beenden. Dass wir hier in Deutschland wieder Deutschland noch entdecken können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 918. Interview mit dem Deutschlandkurier, das Kotré auf X veröffentlich hat.

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