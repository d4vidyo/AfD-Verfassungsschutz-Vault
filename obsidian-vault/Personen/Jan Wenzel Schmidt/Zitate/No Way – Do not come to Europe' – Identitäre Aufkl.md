---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-05-09
topic: Sonstiges
page_bfv: 782
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 9.5.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>No Way – Do not come to Europe' – Identitäre Aufklärungskampagne in Afrika gestartet Die Identitäre Bewegung hat in zahlreichen afrikanischen Staaten und Regionen eine Aufklärungskampagne zur Verhinderung der Masseneinwanderung nach Europa gestartet. In Ländern wie Uganda, Ghana, Somalia und vielen mehr platzierten unsere Aktivisten mit örtlichen Agenturen mehrere Großflächenplakate und setzten ein deutliches Zeichen gegen den zunehmenden Ansturm aus Afrika in die europäischen Länder. Wir zeigen mit unserer Aktion, was die Regierung tatsächlich unternehmen müsste, um die Wanderungsbewegungen nach Europa schon in den Herkunftsländern der Migranten zu stoppen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 782

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