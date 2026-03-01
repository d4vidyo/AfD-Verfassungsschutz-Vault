---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2024-02-01
topic: Menschenwürde
page_bfv: 494
source: 'Artikel'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom Februar 2024 veröffentlicht auf: 'Artikel'
> [!quote] Aussage
>Als die Mitglieder der AfD ihr erstes Grundsatzprogramm beschlossen und in allen Politikfeldern, alternative Lösungsansätze anboten, schäumten die Altparteien und ihnen hörigen Medien vor Wut. Da wagten es doch freie Bürger, den als alternativlos bezeichneten Weg von Sozialisten und Globalisten in eine neue Weltordnung zu hinterfragen und einen alternativen Weg hin zu Souveränität, Freiheit, Frieden und Wohlstand aufzuzeigen. [...] Und natürlich geraten alle Menschen, die die Politik der Altparteien kritisieren, ins Fadenkreuz der Drahtzieher in den Planungsbüros des Great Resets, den Schreibstuben der Hypermoralisten und den vom Staat alimentierten Schlägertrupps der Faschisten unserer Zeit, die sich realitätsverdrehend auch noch Antifa nennen. [...] Die Planer des Great Resets dulden keine Kritik, sie versuchen jedwede Bindungen zwischen Menschen, sei es familiär, regional oder national zu zerstören, um ihnen widerstandslos ihre neue Ordnung überzustülpen. [...] Die Hoffnung der Globalisten ist, wenn die freiheitlichen Parteien verschwänden, verschwindet auch der Drang nach Freiheit und Vernunft.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Februar 2024

**SPIEGEL-Notiz:** Gutachten Seite: 494

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