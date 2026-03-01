---
type: zitat
speaker: "[[Rüdiger Lucassen]]"
date: 2024-02-15
topic: Sonstiges
page_bfv: 854
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Rüdiger Lucassen]] vom 15.2.2024 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Zum einen sollten wir beim Rechtsstaatsprinzip bleiben und individuelles Fehlverhalten nicht auf eine gesamte Organisation übertragen. [...] Zum zweiten sollten wir (auch organisatorisch) deutlich machen, dass die JA zur AfD gehört und von ihr auch weiterhin unterstützt wird. Ich rege an, eine engere Einbindung der Jungen Alternative in die AfD zu prüfen. Zum einen würde dies den verfassungsrechtlichen Schutz, den eine politische Partei genießt, auf die JA ausdehnen. Zum anderen würde es die Strategie des Verfassungsschutzes durchkreuzen, die eindeutig auf eine weitere Spaltung des patriotischen Lagers abzielt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 854

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