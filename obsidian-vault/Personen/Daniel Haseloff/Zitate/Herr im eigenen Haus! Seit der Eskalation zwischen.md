---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2023-10-23
topic: Menschenwürde
page_bfv: 530
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 23.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Herr im eigenen Haus! Seit der Eskalation zwischen #lsrael und den #Gaza-Palästinensern spielen viele Akteure im patriotischen Lager Weltpolitik. Je nach Neigung will man mal Teheran bombardieren, mal die Zweistaatenlösung stärken, mal Friedenstruppen senden. Ich denke: Wir müssen als Opposition das stark machen, was unseren Wählern und uns selbst zuallererst am Herzen liegen sollte – Herr im eigenen Haus sein. Wir müssen dafür nicht Weltpolitik spielen. Reicht es nicht, wenn wir das Nahe, das Konkrete thematisieren? Drei Beispiele: 1. Wir haben uns immer für #Remigration eingesetzt. Das bleibt aktueller denn je: Denn mit der realexistierenden #Massenmigration importieren wir Konflikte, die nicht die unsrigen sind. 2. Wir sehen einer unfähigen Ampel-Koalition beim erneuten Scheitern zu: Die Evakuierung deutscher Staatsbürger funktioniert nur mit fremder Hilfe. Versagen der Staatsorgane heißt Kritik an den Verantwortlichen! 3. Wir beobachten eine neue Form der moralpolitischen Selbsterhöhung: Die #Ukraine-Fahne wird schnell ausgetauscht durch die nächste Nationalfahne. Hier heißt es also, das Establishment und seine willfährigen Helfershelfer zu kritisieren: Wann kümmert ihr euch um unsere Anliegen mit derselben Leidenschaft? Kurz gesagt: Herr im eigenen Haus sein. Das wäre schon was. Das heißt aber auch, Prioritäten zu klären. Für Weltpolitik sind derzeit andere zuständig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 530. abweichendes Datum in der Fußnote des Berichts

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