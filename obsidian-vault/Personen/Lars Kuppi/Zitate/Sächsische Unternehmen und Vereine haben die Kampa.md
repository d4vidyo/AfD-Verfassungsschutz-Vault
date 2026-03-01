---
type: zitat
speaker: "[[Lars Kuppi]]"
date: 2024-07-11
topic: Demokratieprinzip
page_bfv: 592
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Lars Kuppi]] vom 11.7.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sächsische Unternehmen und Vereine haben die Kampagne '#stabilbleiben' zur Landtagswahl gestartet. Angesichts einer zunehmenden gesellschaftlichen Spaltung wollen sie ein 'Zeichen für mehr Miteinander' und 'Vielfalt' setzen und hoffen auf eine hohe Wahlbeteiligung. Beteiligt sind mehrere Staatsunternehmen und Vereine, die die Regierung mit Steuergeldern finanziert

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 592. Kombination mit einem nachfolgendem Bild

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