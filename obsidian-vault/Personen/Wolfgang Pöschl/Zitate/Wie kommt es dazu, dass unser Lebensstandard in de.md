---
type: zitat
speaker: "[[Wolfgang Pöschl]]"
date: 2022-11-24
topic: Demokratieprinzip
page_bfv: 575
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Wolfgang Pöschl]] vom 24.11.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wie kommt es dazu, dass unser Lebensstandard in den letzten Jahrzehnten so dramatisch gesunken ist? Weil wir von einer ideologieverseuchten Räuberbande regiert werden. Lobbyisten der Kartellparteien und vor allem voran der Grünen stopfen sich die Taschen voll, indem sie uns mit Steuern auf Energie CO2 und auf unser Vermögen unser Hab und Gut schleichend enteignen. [...] Während euer Bankkonto geplündert wird, fließt das Geld in die Taschen der globalistischen Superreichen, der globalistischen Eliten, wie Klaus Schwab, George Soros, Bill Gates, König Charles III von Großbritannien und so weiter. Und deren korrupten Handlanger wie früher schon Merkel und jetzt unsere rot-grünen Politdarsteller in München, Berlin und Brüssel. [...] Mit allen Mitteln suchen sie nun nach Sündenböcken, um die Schuld am finanzwirtschaftlichen Zusammenbruch von sich abzuwenden. Die Zerstörer der freiheitlichen wirtschaftlichen und politischen Ordnung des Westens, die unermesslichen Reichtum gesammelt haben, wollen jetzt ihrer Verantwortung entkommen. [...] Wir lassen uns von den Lügen dieser Gauner nicht mehr irreführen! Zum Teufel mit ihnen! [...] Das haben wir übrigens auch den korrupten, verlogenen Rundfunkmedien zu verdanken. Um ihre Macht und ihr durch Unrecht gerafftes Geld vor einem Crash wie 1929 zu schützen, wollen die Profiteure eine neue Ordnung der Welt und des Wirtschaftssystems den Menschen auferlegen. In einer unheiligen Allianz mit machtgierigen Neomarxisten wollen die globalen Spieler ihre Macht in einer globalen, totalitären Herrschaft sichern, der sogenannten Global Governance. [...] Sie haben uns Bürger dabei ausgenutzt und uns unseren Wohlstand genommen. Unsere Freiheit, unsere Demokratie, der Rechtsstaat, unsere Kultur, alles das wollen sie uns nehmen! Jetzt wollen sie uns auch noch eine neue, totalitäre Weltordnung aufzwingen, um uns zu unterwerfen und zu knechten. Werdet ihr das wirklich zulassen? Wir sind die große Mehrheit, wir sind bereit, unsere Bestimmung für die Freiheit zu verteidigen. Nach Artikel 20 GG haben wir das Recht und die Pflicht dazu. Stehen wir jetzt gemeinsam auf, nehmen wir unser Schicksal in die Hand und holen wir uns unsere Freiheit, unsere Selbstbestimmung und unsere Zukunft wieder zurück! [...] Stoppen wir den globalen Totalitarismus dieser Akteure und Volksverräter!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 575

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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