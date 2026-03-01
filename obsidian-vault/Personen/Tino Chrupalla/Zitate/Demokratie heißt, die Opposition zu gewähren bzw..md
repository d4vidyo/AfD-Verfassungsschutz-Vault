---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-01-21
topic: Demokratieprinzip
page_bfv: 598
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 21.1.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Demokratie heißt, die Opposition zu gewähren bzw. sich mit der Opposition auseinanderzusetzen. Was macht man? Am liebsten den politisch Unwilligen verbieten, um natürlich selbst noch den warmen Sessel sich zu retten. Das erleben wir. Dann geht man natürlich mit solchen unsäglichen Kampagnen in Stasi-Manier, anders kann man es nicht sagen, wie wir es in Potsdam erlebt haben, gut vorbereitet gegen die einzig wahrnehmbare Opposition vor. [...] Wir haben es erlebt bei den Demonstrationen jetzt am Montag hier in Berlin. Zehntausende gehen auf die Straße gegen diese Regierung. Und was ist die Antwort der Regierung? Wir machen jetzt und unterstützen Demos gegen die Opposition. Also das ist schon ein Stück weit lächerlich. Und das erinnert mich wirklich an die Geschehnisse '89, '90, die hier in Deutschland auf den Straßen passiert sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 598

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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