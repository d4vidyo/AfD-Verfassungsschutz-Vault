---
type: zitat
speaker: "[[Sven Kachelmann]]"
date: 2025-01-12
topic: Sonstiges
page_bfv: 866
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Sven Kachelmann]] vom 12.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Man kann so einen Reformprozess, eine tiefgreifende Veränderung, nur mit, und damit meine ich allen Mitgliedern der Jugendorganisation gestalten und nicht ohne sie oder gegen deren Willen. [...] Diese Idee wurde nie ausgereift und dieser Antrag des AfD-Bundesvorstands hat mit einem Juso-Modell nichts zu tun. Nichts, aber auch gar nichts. Denn er geht viel weiter über das Ziel hinaus als die Jusos es wollten. [...] Wir erleben staatliche Repressionen noch und nöcher. Wenn man die Sorge hat, es kommt ein Vereinsverbot der JA, die Sorge kann ich euch gerne in Teilen nehmen. Denn Folgendes ist doch der Fall. Was wird denn passieren, wenn wir heute sagen: Nicht die Junge Alternative ist die Jugendorganisation der AfD, die JA wird es am Montag immer noch geben [...]. Wenn man sagt, wir wollen die Jugend schützen, dann muss man auch sagen: Dieser Entwurf, der zahlt auf das Konto, unsere Jugend, die jetzt besteht, zu schützen nicht ein. Er macht den aktuellen Zustand noch schlechter.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 866

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