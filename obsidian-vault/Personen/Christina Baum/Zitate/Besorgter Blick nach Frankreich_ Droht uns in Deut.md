---
type: zitat
speaker: "[[Christina Baum]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 275
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom None veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Besorgter Blick nach Frankreich: Droht uns in Deutschland ein Bürgerkrieg? Angesichts der aktuellen massiven Ausbrüche an Migrantengewalt in Frankreich müssen wir uns fragen, ob solche bürgerkriegsähnlichen Zustände nicht auch bei uns künftig drohen können. Die vorsätzlich forcierte Massenmigration nach Deutschland bei gleichzeitiger ebenso vorsätzlicher Demontage unserer Wirtschaft wird in absehbarer Zeit zwangsläufig zu eskalierenden Verteilungskämpfen führen. Da eine Integration kulturfremder Bevölkerungen in dieser Größenordnung nicht leistbar und damit illusorisch ist und von der herrschenden Klasse auch gar nicht mehr angestrebt wird, werden die Verteilungskämpfe entlang der ethnokulturellen Bruchlinien der Parallelgesellschaften und der einheimischen Bevölkerung erfolgen. Kombiniert mit der zunehmenden Erosion der öffentlichen Sicherheit und den wachsenden No-Go-Areas für deutsche Polizisten braut sich in unserem Land ein explosives Gemisch zusammen, das sich eines Tages entladen wird. Wenn wir hier nicht schleunigst das Ruder um 180° herumreißen und eine umfassende, humane Remigration illegaler und nichtintegrierbarer Migranten in Gang setzen, sind die schrecklichen Szenen in Frankreich auch bei uns nur eine Frage der Zeit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 275

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