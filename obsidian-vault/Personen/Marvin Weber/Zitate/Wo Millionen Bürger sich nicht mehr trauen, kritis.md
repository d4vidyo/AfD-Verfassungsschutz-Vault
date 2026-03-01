---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-07-24
topic: Demokratieprinzip
page_bfv: 560
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 24.7.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wo Millionen Bürger sich nicht mehr trauen, kritische Themen anzusprechen, ohne gesellschaftlich mit allen totalitären Mechanismen dieser staatlich alimentierten Denunziantenrepublik im Kulturkampf gegen Rechtstaatlichkeit und Rechtschaffenheit, also kurz gesagt: der ewige Kampf gegen rechts, als Staatsfeind gebrandmarkt werden und vollkommen ausgeschlossen werden. [...] Es waren nämlich in den letzten zwei Jahren totalitäre Mechanismen und Maßnahmen, die unser aller Grundrecht, das Demonstrationsrecht ad absurdum getrieben haben, während die linksterroristische ANTIFA, die rassistische Blackpower-Bewegung - kurz: Black Lives Matter - und die konformen Hedonisten der LGBTQ-Bewegung hier absolute Narrenfreiheit genießen! Sie sind ja Handlanger der Herrschenden Germanophobie, also der Auflösung alles Deutschen, der Kultur, der Nation, der Sprache und sie fungieren natürlich als Katalysator der schwarz-rot-grünen Deutschen-Feinde. [...] Aber im Transformationsprozess gen allerbestes Deutschland aller Zeiten sind und waren diese Maßnahmen natürlich nicht dafür da, die Bevölkerung vor einer Grippe zu schützen, von der 99 Prozent der Infizierten wieder genesen sind, sondern zu schauen, wie leidensfähig und manipuliert dieses Volk auch die Aushebelung der Demokratie gen Postdemokratie beklatschen wird. [...] Aber auch das ist ja nichts Neues im besten Deutschland aller Zeiten, wo die quasi gleichgeschaltete Kartellpresse immer der Agenda der Herrschenden folgt [...] mit all ihren staats- und kulturzersetzenden Folgen für uns Einheimische gebetsmühlenartig mit den perfektionierten Propagandamechanismen aus zwei vergangenen sozialistischen Diktaturen im digitalen Zeitalter herunterbetet und die Kritik der Regierung oder die Kritik an der Regierung besser gesagt als Blasphemie erklärt. [...] Man rettet und verteilt das Steuergeld im Weltretter-Wahn und der kollektiv-historischen Zwangsneurose an den Rest der Welt und vergisst mit voller Absicht das eigene Volk, die eigenen Deutschen, seine Nächsten. Die Herrschaft der Schlechtesten in Deutschland hilft allen Völkern auf dieser Welt aufopferungsvoll und mit ewigem historischen Schuld-Kult überweist gerne mal 10 Milliarden deutsches Steuergeld nach Indien aus vermeintlichen Klimaschutzgründen und lässt die eigenen Bürger im zerstörten Ahrtal alleine, um wiederum von Indien überteuertes Gas und Öl zu kaufen, welches diese wiederum aus Russland beziehen! Das ist die Idiotenherrschaft in Deutschland in Reinform, meine Damen und Herren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 560

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