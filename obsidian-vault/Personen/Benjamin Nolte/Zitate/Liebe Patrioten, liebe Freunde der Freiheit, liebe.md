---
type: zitat
speaker: "[[Benjamin Nolte]]"
date: 2025-02-18
topic: Demokratieprinzip
page_bfv: 963
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Benjamin Nolte]] vom 18.2.2025 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Liebe Patrioten, liebe Freunde der Freiheit, liebe User und Zuseher des Deutschland-Kuriers, mein Name ist Benjamin Nolte und ich bin Abgeordneter für die AfD im Bayerischen Landtag. Unser Brauchtum und unsere Traditionspflege, einst Zeichen unserer Identität und unseres Stolzes, wurde von den Kartellparteien in den letzten Jahren zur Zielscheibe ihrer Kulturvergessenheit gemacht. Allen voran von den Deutschlandabschaffern von CDU und CSU. Einst konservative Wertebewahrer sind CDU und CSU heute nur noch kulturmarxistische Marionetten. Von Heimatliebe und Respekt für unsere Traditionen ist nichts mehr übrig, außer vielleicht in Wahlkampfreden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 963

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