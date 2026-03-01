---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2024-12-21
topic: Menschenwürde
page_bfv: 942
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 21.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir trauern um die Opfer des Terroranschlags auf dem Weihnachtsmarkt in Magdeburg. Und wenn sich nun die Politiker jeder Couleur der Altparteien, hier auch in Trauer üben, dann ist das heuchlerisch. Denn sie haben diesen Zustand herbeigeführt, in dem sowas möglich ist. Die Sicherheitsbehörden, die wollten diesen Anschlag nicht verhindern, sie hatten genügend Hinweise. [...] Die AfD möchte ein Deutschland, wie es von der inneren Sicherheit und von den Interessen der Bevölkerung vor 30, 40 Jahren gegeben hat, wo man die Bevölkerung geschützt hat, wo man solche Leute aus dem Verkehr gezogen hat, und vor allem ganz wichtig, wo man die Grenzen kontrolliert hat und auch die Leute, die hier reinkommen. Wir haben es wieder mit einem Phänomen zu tun, dass Kulturfremde hier entsprechend Terror reinbringen ins Land. Und das ist unverständlich. Und wir werden alles dafür tun, dass sowas nicht passiert, wenn wir denn in der Macht sind. Islamistische Anschläge oder einfach Anschläge wie dieser hier, der mit dem Islam zu tun hat, sind unverständlich. Denn die Scharia, der Islam, gehören nicht zu Deutschland. Und auch hier wieder sehen wir, dass wir eingeschleppte Probleme haben und dass wir Deutsche friedlich miteinander umgehen, aber die Aggressivität, die Morde und auch der Verlust der inneren Sicherheit auf das Konto von Ausländern gehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 942

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