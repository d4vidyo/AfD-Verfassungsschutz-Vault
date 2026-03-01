---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-10-08
topic: Menschenwürde
page_bfv: 507
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 8.10.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Liebe Wähler, wenn Sie nicht Teil derer sein wollen, die zulassen, dass Deutschland immer stärker in eine Scheindemokratie abdriftet können Sie am heutigen Sonntag nur AfD wählen. Ich appellieren besonders inständig an alle Nichtwähler. Geben Sie uns, der Alternative für Deutschland, eine Chance, den Systemwechsel zu vollziehen: Weg von Filzokratie und Tiefem Staat, hin zu Rechtsstaat mit funktionierender Gewaltenteilung. Freiheitlich Demokratischer Grundordnung. Hin zu einem souveränen Deutschland, dessen Regierung deutsche Interessen vertritt. Werden Sie Teil des demokratischen Widerstands gegen Entrechtung. Verarmung und Menschenverachtung. Liebe Nichtwähler, Sie sind mit Abstand die größte Gruppe. Sie können an diesem den entscheidenden Unterschied machen zwischen einer Zukunft für sich und Ihre Kinder in Demokratie, Frieden, Freiheit- in Sicherheit und selbst erwirtschaftetem Wohlstand oder eben in sozialistischer Zwangs-, Verbots-, Entrechtungs- und Verarmungspolitik der globalen Eliten und ihren Willingen Vollstreckern in den deutschen Parlamenten nämlich der vergrünten AntideutschlandEinheitspartei bestehend aus CDUCSUFDPSPDBündins90dieGrünenDielinke. Stemmen Sie sich mit uns zusammen gegen die dritte sozialistische Diktatur auf Deutschem Boden. Auch wenn sie im netten grünen Kleidchen mit Heilsversprechen daherkommt. Wir, die AfD, sind keine Systempartei. Wir sind nicht fremdgesteuert, weder von Putin noch sonstwem, haben keine Young Global Leaders an Bord. Wir dienen Deutschland. Geben Sie uns eine Chance. Wählen Sie am heutigen Sonntag in Bayern und in Hessen die AfD. Wir alle wollen freie Bürger sein. Keine Untertanen. Werden Sie Teil des demokratischen Widerstands und bringen Sie mit uns Demokratie und Freiheit zurück nach Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 507

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