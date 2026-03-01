---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-10-28
topic: Menschenwürde
page_bfv: 466
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 28.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Jeder Migrant ,Flüchtling' oder Asylant, der zu uns kommt, weiß genau, dass wir ein christlich geprägtes Land sind. Wer also seine eigene Religion ausleben möchte, darf sich deshalb gerne ein kultur- und religionsnahes Land für seine Entfaltung aussuchen. Die bewußte Entscheidung der vorwiegend muslimischen Migranten für Deutschland kann deshalb nur eines bedeuten: wir sollen unterwandert und unterworfen werden. [...] Für uns Deutsche, aber auch für alle anderen europäischen Völker, die in ähnlicher Weise islamisiert werden sollen, bleibt allein die Frage: wollen wir es einfach hinnehmen oder wollen wir uns endlich dagegen auflehnen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 466

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