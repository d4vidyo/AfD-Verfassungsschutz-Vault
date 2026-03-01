---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2021-11-30
topic: Demokratieprinzip
page_bfv: 624
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 30.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bundesverfassungsgericht macht sich wieder mal zum #Büttel der Regierenden! [...] Was aber soll man anderes erwarten von einem Bundesverfassungsgericht, das eng verbandelt mit der Regierung ist, sich sogar in vollständiger Besetzung zum Essen mit der Kanzlerin trifft und dort Vorträgen von Ministern lauscht? Ein Gericht, dessen Präsident ein enger Parteifreund von Merkel ist, der hoher Funktionär der Kanzlerpartei war und der sich schon vor Monaten öffentlich zustimmend zur Coronapolitik äußerte? Dass bei diesen Voraussetzungen keine seriöse juristische Prüfung, sondern Büttelrechtssprechung zu erwarten war, dürfte niemanden überraschen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 624

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