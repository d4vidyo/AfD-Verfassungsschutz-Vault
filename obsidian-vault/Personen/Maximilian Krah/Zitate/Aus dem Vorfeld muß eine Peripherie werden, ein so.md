---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023
topic: Sonstiges
page_bfv: 703
source: 'Buch "Politik von rechts. ein Manifest"'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 2023 veröffentlicht auf: 'Buch "Politik von rechts. ein Manifest"'
> [!quote] Aussage
>Aus dem Vorfeld muß eine Peripherie werden, ein soziales Milieu an Menschen, bei denen innere Haltung und äußeres Leben zusammenfinden und die Attraktivität des Äußeren die Überzeugungskraft des Inneren induziert. Gerade in einer Epoche der Formlosigkeit und des Kulturverlustes, in der die üppig geförderte Staatskunst ja doch nur Niedergang und Häßlichkeit zu bieten hat, ist eine eigene rechte Kultur, sind Formen und Regeln, Gemeinschaft statt Masse, kurz: ist Gegenkultur unverzichtbar. Die Rechte muß von einer rein politischen zu einer sozialen Bewegung werden und braucht dazu ‚soft power‘. Die politische Rechte muß von den Grünen lernen, daß sie ihre Peripherie zu fördern hat. Nicht der jammernde CDU-Kollege wählt rechts, sondern die Aktivisten in den oft genug verfolgten und verfemten Initiativen. Sie hängen Plakate und sammeln Unterschriften. Sie müssen durch Praktika, Bildungsangebote und schließlich Jobchancen gefördert werden. Die Verzahnung von Partei und Peripherie ist generell der Schlüssel zum Erfolg, angesichts des massiven sozialen wie juristischen Drucks auf die politische Rechte und der Erosion aller Werte, die der Rechten wichtig sind, ist sie für eine rechte Bewegung unerläßlich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 703

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