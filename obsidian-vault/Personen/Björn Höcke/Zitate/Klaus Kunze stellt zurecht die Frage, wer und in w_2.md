---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-10-30
topic: Demokratieprinzip
page_bfv: 629
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 30.10.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Klaus Kunze stellt zurecht die Frage, wer und in welchem Interesse Deutschland regiert wird. Sein Beitrag zeigt indirekt auf, wie groß der Reformbedarf ist, wenn wir in und für Deutschland wieder das Prinzip der Volkssouveränität umsetzen wollen. Lesenswert!

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Klaus Kunze stellt zurecht die Frage, wer und in w]]

**SPIEGEL-Notiz:** Gutachten Seite: 629

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