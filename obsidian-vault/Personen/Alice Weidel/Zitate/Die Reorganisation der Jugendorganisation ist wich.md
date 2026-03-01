---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 860
source: 'Presserklärung'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 3.12.2024 veröffentlicht auf: 'Presserklärung'
> [!quote] Aussage
>Die Reorganisation der Jugendorganisation ist wichtig, um die Jugendorganisation zukünftig näher an die Partei einzubinden. Und zwar wollen wir, dass die Mitglieder der Jugendorganisation auch zeitgleich Mitglied der AfD sind. Und das haben wir momentan nicht. Und dementsprechend streben wir eine Reorganisation hier an, dass wir eine größere Schnittmenge zu den Mitgliedern auch der Jugendorganisation haben zu der zukünftigen, die deutlich anders aufgestellt sein wird als die jetzige. [...] Das ist deshalb so wichtig, damit die Mutterpartei, die Alternative für Deutschland, auch Durchgriffsmöglichkeiten hat auf die Jugendorganisation, die sie derzeit nicht innehat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 860

**Verfassungsschutz Kategorisierung:** Sonstiges.

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