---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-08-25
topic: Menschenwürde
page_bfv: 392
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 25.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Kein Schüler, der kein Deutsch kann, wird jemals wieder eine deutsche Klasse mehr von innen sehen, liebe Freunde! Wir werden eine Migrationsobergrenze von 10 Prozent einführen. Und noch wichtiger: Wir werden diesen Schülern, die rauben, die klauen, die deutsche Schüler drangsalieren, [...] als 'scheiß Deutsche' bezeichnen und den Schulfrieden stören, diesen Schülern werden wir das Recht auf Bildung aberkennen, sie von der Präsenzpflicht entbinden [...] und auch diese Schüler werden auf Dauer eine deutsche Schule nicht mehr von innen sehen und es ist nicht unser Problem, wie diese Eltern ihre Kinder beschulen. [...] Damit die Eltern auch mal einen Anreiz haben, ihren Mohammed und ihren Ali ordentlich zu erziehen, werden wir diesen Eltern das Kindergeld und die Sozialhilfe so lange kürzen, bis der nicht in der Lage ist an einer deutschen Schule unterrichtet zu werden [...] und dann wollen wir mal sehen, wie lange wir noch Probleme an unseren Schulen haben, die so aussehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 392. vom AfD Familienfest in Brandenburg (Havel)

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