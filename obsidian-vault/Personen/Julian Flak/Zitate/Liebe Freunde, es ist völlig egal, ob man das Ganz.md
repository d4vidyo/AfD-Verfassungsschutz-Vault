---
type: zitat
speaker: "[[Julian Flak]]"
date: 2023-08-04
topic: Menschenwürde
page_bfv: 416
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Julian Flak]] vom 4.8.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Freunde, es ist völlig egal, ob man das Ganze jetzt Abschiebeoffensive nennt, Negativeinwanderung oder schlicht Remigration und damit ein natürlich ganz aufgeregtes Rechtsruck-Tourette beim obersten Regierungsschützer Haldenwang auslöst und bei irgendwelchen GEZ-Experten. Wichtig ist nur, wer in Deutschland nichts zu suchen hat, der soll Deutschland verlassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 416. Bewerbungsrede auf der Europawahlversammlung der AfD

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