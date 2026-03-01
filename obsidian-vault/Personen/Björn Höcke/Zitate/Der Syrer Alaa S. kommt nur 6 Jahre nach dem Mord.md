---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-25
topic: Rechtsstaatsprinzip
page_bfv: 971
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 25.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Syrer Alaa S. kommt nur 6 Jahre nach dem Mord an Daniel H. aus dem Gefängnis und wird n i c h t abgeschoben. Die Europäische Konvention der Menschenrechte wird vom Gericht für diese Entscheidung herangezogen, um das Prinzip „Täterschutz vor Opferschutz“ praktizieren zu können. Ich frage mich: Was ist mit den Menschenrechten der Deutschen und warum setzt man die Konvention nicht aus, wenn offenkundig der Staatszerfall in Deutschland droht? Letztlich ordnen die Richter- und mit ihr die Kartellparteien - die Existenz des Staates dem Recht bzw. der Auslegung des Rechtes unter. Finde den Fehler! Ich wiederhole hier eine alte Einsicht, wenn ich sage: Es gibt kein internationales Recht, das das Recht eines souveränen Volkes brechen könnte, selbst darüber zu entscheiden, mit wem es zusammenleben will und mit wem nicht!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 971

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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