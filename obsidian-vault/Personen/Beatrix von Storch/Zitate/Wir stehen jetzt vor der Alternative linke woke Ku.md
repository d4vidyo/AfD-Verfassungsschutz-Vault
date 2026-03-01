---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: 2024-10-01
topic: Menschenwürde
page_bfv: 514
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom Oktober 2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir stehen jetzt vor der Alternative linke woke Kulturrevolution oder geistig-moralische Wende, darum geht es bei der Bundestagswahl 2025. Die Linksgrünen führen einen Kulturkampf gegen alles, was wir lieben. Gegen Deutschland, gegen das christliche Abendland und gegen unsere Kultur und Identität. CDU, FDP, Wirtschaftsverbände, die Kirchen haben alle kapituliert, indem sie woke geworden sind. Aber wir führen diesen Kulturkampf nicht nur reaktiv, wir führen ihn aktiv. [...] Wir brauchen keine Brandmauer gegen die AfD, wir brauchen eine Brandmauer gegen den globalistischen Wahn. Und die Brandmauer gegen den globalistischen Wahn, das ist die AfD. Was die woken Kräfte in Brüssel, Davos und New York entscheiden, zerstört unser Leben hier in Deutschland, in Lichtenberg, in Pankow, überall. Darum führen wir den Kampf auf allen Ebenen: lokal, national und global. [...] Aktuelle Stunde zum UN-Zukunftsgipfel im Bundestag. Ich habe in meiner Rede dazu im Bundestag gezeigt, was die anderen alle verschwiegen haben: Das Ziel des UN-Generalsekretärs – eine Weltregierung installieren. Den globalen Notstand ausrufen können. Mit seinen Hintermännern von BlackRock, World Economic Forum, Gates und Co. [...] Hinter der grünen Klimapolitik steckt die globale Finanzindustrie. Es geht nicht um Klimaschutz, es geht um Macht und Geld, um sehr viel Geld.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Oktober 2024

**SPIEGEL-Notiz:** Gutachten Seite: 514. Bewerbungsrede auf dem Landesparteitag, dann am 14.10.2024 auf Instagram veröffentlicht.

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