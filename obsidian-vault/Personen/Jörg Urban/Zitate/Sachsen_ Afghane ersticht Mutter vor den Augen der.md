---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-02-15
topic: Menschenwürde
page_bfv: 387
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 15.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sachsen: Afghane ersticht Mutter vor den Augen der gemeinsamen Kinder. Multikultureller Alltag in Deutschland: In einer sozialen Einrichtung in Crimmitschau erstach vergangenen Samstag ein mutmaßlich 36-jähriger Mann seine 33-jährige Frau und Mutter von 5 Kindern. Verwunderlich ist das leider schon lange nicht mehr: Weil Politiker und Aktivisten unser Land zum Einwanderungsland erklärten, erhalten archaische Bräuche durch kulturfremden Zuzug, insbesondere aus dem arabischen Raum, Einzug in Deutschland. Wer als Kind gelernt hat, dass Frauen das Eigentum ihres Mannes sind und die Ermordung einer nicht hörigen Ehefrau von der dortigen Gesellschaft toleriert wird, der verlernt dies in Deutschland nicht nach ein paar Integrationskursen. Dass die Altparteien von Linke bis CDU das zu glauben scheinen, kostet nun nicht zum ersten Mal Menschenleben. Nur die AfD stellt sich gegen die Einwanderung von völlig kulturfremden Menschen nach Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 387

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