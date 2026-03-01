---
type: zitat
speaker: "[[Petr Bystron]]"
date: 2023-07-29
topic: Menschenwürde
page_bfv: 497
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Petr Bystron]] vom 29.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und sie [Anm.: die Menschen] haben erkannt, dass sie von den Altparteien verraten wurden, für Rüstungskonzerne, für die Pharmaindustrie, eben an die Globalisten. Und sie haben begriffen, dass wir da sind für die Mittelschicht, für die Menschen, die arbeiten und Steuern zahlen, die Familie mit Kindern, die dieses Land tragen, für die Unternehmer, die Arbeitsplätze schaffen und Wohlstand sichern. Und zwar, dass wir kämpfen gegen die Kriegstreiber, die uns in Kriege aufhetzen wollen. Gegen die Globalisten, die uns zwangsimpfen wollten, die uns enteignen wollen, uns ja im Prinzip versklaven wollen. Und die Menschen haben verstanden, dass wir die Einzigen sind, die den Mut haben, gegen die Schwabs, Gates und Soros dieser Welt anzukämpfen. [...] Aber aus Brüssel kommt das Gift. Dort werden von den Globalisten still und heimlich Vorgaben gemacht, die nachher nur in den nationalen Parlamenten nur noch durchgewunken werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 497

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