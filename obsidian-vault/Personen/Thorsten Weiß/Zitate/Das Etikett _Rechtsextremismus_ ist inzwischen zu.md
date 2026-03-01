---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2024-02-07
topic: Sonstiges
page_bfv: 837
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 7.2.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Das Etikett "Rechtsextremismus" ist inzwischen zu einer inhaltsleeren Diffamierung verkommen. Nun hat das Kölner Verwaltungsgericht einen Eilantrag gegen die Einstufung der Jungen Alternative abgewiesen. Der Beschluss ist noch nicht rechtskräftig, aber es zeigt, dass es in unserem Land gefährliche Defizite in der demokratischen Gewaltenteilung gibt. Es war ein politisches Urteil und folgt der groß angelegten Kampagne zur Kriminalisierung der Opposition. Man spekuliert darauf, dass Repressionen gegen unsere Parteijugend leichter umzusetzen sind und natürlich ist das nur der erste Schritt. Umso wichtiger ist es, dass wir uns nicht gegen einander ausspielen lassen. Niemand in der JA verfolgt Umsturzpläne, wir stehen geschlossen für die Werte der freiheitlichen demokratischen Grundordnung. Dazu gehört aber eben auch zwingend die freie Debatte – ohne diese ist eine Demokratie nicht möglich! An der lächerlichen Urteilsbegründung sehen wir, dass der "Rechtsextremismus"-Begriff aufwendig uminterpretiert werden musste, damit die Vorwürfe überhaupt aufrechterhalten können. Nach diesen Maßstäben wäre die CDU vor der Ära Merkel genau "rechtsextremistisch" gewesen. Lassen wir uns nichts einreden und verteidigen wir gemeinsam unsere demokratischen Rechte! Nie war es so wichtig wie heute!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 837

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