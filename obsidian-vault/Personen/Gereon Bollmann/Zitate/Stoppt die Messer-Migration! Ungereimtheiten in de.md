---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2024-06-20
topic: Menschenwürde
page_bfv: 283
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 20.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Stoppt die Messer-Migration! Ungereimtheiten in den offiziellen Zahlen zur Messer-Kriminalität: Ist alles noch viel schlimmer? Die Messer-Kriminalität in Deutschland explodiert. Dies ist inzwischen ein offenes Geheimnis. Selbst die offiziellen Polizeistatistiken sprechen Bände, so daß die dramatische Entwicklung nicht unter den Tisch gekehrt werden kann. [...] Der #AfD-Abgeordnete Gereon Bollmann, Mitglied im Rechtsausschuss des Deutschen Bundestages, erklärt dazu: 'Die heimtückischen Messerattacken der vergangenen Tage haben das Problem dieses Deliktbereichs einmal mehr verdeutlicht. Die Statistiken sprechen Bände, die Realität noch viel mehr: der exorbitant hohe Anstieg von Messerangriffen ist unmittelbar mit der ausufernden Masseneinwanderung seit 2015 verbunden. Deshalb muss und kann es nur heißen: Schützt die Bürger unseres Landes! Stoppt die Messer-Migration!'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 283

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