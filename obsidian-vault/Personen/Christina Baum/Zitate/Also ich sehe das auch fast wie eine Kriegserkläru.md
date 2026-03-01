---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-12-21
topic: Rechtsstaatsprinzip
page_bfv: 662
source: 'Interview auf auf1.tv'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 21.12.2021 veröffentlicht auf: 'Interview auf auf1.tv'
> [!quote] Aussage
>Also ich sehe das auch fast wie eine Kriegserklärung. Ich war ja im Plenum. Ich habe das ja gehört. [...] Er hat geschworen, für das Wohl des deutschen Volkes sich einzusetzen und leider habe ich ja auch diese Polizeigewalt verfolgt. Ich war selber auch mittendrin bei solchen Demonstrationen und habe mit Entsetzen gesehen, dass es tatsächlich Polizisten gibt, die bereit sind, solche Gewalt anzuwenden. Und ich möchte damit auch gleichzeitig einen Aufruf starten, sozusagen an alle Polizisten, an alle Bundeswehrsoldaten, an alle Ordnungskräfte, dass sie sich das sehr gut überlegen müssen, wie sie in Zukunft mit solchen Bewegungen umgehen. Die Bewegungen sind absolut friedlich bisher. Die Bevölkerung ist sehr diszipliniert, und es kann nicht sein, dass die Polizei zu solchen harten Maßnahmen greift. Denn nach jeder Demonstration, wenn ich eine Rede halte, richte ich meine Worte auch an die Polizei, und ich sage ihnen, dass sie sich sehr gut überlegen müssen, auf welcher Seite sie stehen. Denn eines Tages werden sie diese Entscheidung treffen müssen: Erhebe ich die Hand gegen mein eigenes Volk oder geh ich mit ihm auf die Straße sozusagen, ja. Und diese Exekutive, die wird die Entscheidung bringen, in welche Richtung sich das Ganze entwickelt. Wenn die sagen, wenn die Polizei sagt 'Wir machen da nicht mehr mit', dann können die in Berlin alle nach Hause gehen. Und auf diesen Zeitpunkt warte ich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 662

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