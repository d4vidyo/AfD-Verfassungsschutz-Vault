---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-09-12
topic: Menschenwürde
page_bfv: 124
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 12.9.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir sind Volkspartei, weil wir als einzige Partei noch am Volk festhalten. Wir sagen, das Volk ist kein Konstrukt. Das Volk ist eine Realität. Das Volk ist eine lebendige Realität. [...] Und wir halten auch am Volk, am ethnischen Volksbegriff und am Volk fest. Das Volk ist eine Wirklichkeit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 124

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