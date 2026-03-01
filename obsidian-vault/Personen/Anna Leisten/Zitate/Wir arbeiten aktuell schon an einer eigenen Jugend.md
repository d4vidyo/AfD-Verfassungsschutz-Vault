---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2025-01-08
topic: Sonstiges
page_bfv: 842
source: 'YouTube; Interview mit COMPACTTV'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 8.1.2025 veröffentlicht auf: 'YouTube; Interview mit COMPACTTV'
> [!quote] Aussage
>Wir arbeiten aktuell schon an einer eigenen Jugendkampagne für den Winterwahlkampf. Wir haben uns jetzt relativ schnell auch überlegt, dass wir da genauso wie im Sommer, wie wir in Brandenburg die Kampagne mit sehr wenig Ressourcen, sehr wenig Manpower auf die Beine gestellt haben, genau das gleiche jetzt auch im Bund tun werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 842

**Verfassungsschutz Kategorisierung:** Sonstiges.

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