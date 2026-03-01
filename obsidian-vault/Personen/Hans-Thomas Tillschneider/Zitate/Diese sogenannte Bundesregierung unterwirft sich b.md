---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-09-16
topic: Demokratieprinzip
page_bfv: 552
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 16.9.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Diese sogenannte Bundesregierung unterwirft sich bedingungslos den USA. Um den Herren in Washington sogar noch was besser zu gefallen, beschimpft und beleidigt sie Russland am laufenden Band. So vergiftet die Bundesregierung unser Verhältnis zu Russland. [...] Diese Bundesregierung verhält sich wie eine abgetakelte weinerliche Dirne.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 552

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