---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 566
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und was bieten uns die Kartellparteien an Lösungen an? Sie haben keine Lösung. Sie versuchen uns Schlafsand in die Augen zu träufeln, jetzt zu streuen, jetzt gerade wieder vor den anstehenden Wahlen morgen. Aber ich kann mich erinnern, 2015, 2016 war es nicht anders und ich möchte vor allen Dingen vor der Wahl der CDU warnen, die jetzt hier durchs Land zieht und wieder rechts blinkt und jeder weiß, dass sie links abbiegen wird nach der Wahl. Die hier groß plakatiert 'Illegale Migration stoppen'. Ja, wer ist denn hauptverantwortlich als älteste Partei, Regierungspartei im Land und im Bund? Es ist die CDU. Das ist keine deutsche Partei, das ist eine transatlantische Vasallenpartei. Ich muss das nicht weiter ausführen. [...] Und dann sind die Kartellparteien, und ich war ja nun auch in einigen Talkshows, immer auf der symptompolitischen Ebene unterwegs. Ja, jetzt haben wir das Desaster, dass die Kartellparteien eingerichtet haben. Wir wissen, die Problemverursacher können niemals die Problemlöser sein. [...] Das Problem ist, dass die Kartellparteien Millionen haben einwandern lassen, die aus archaischen Kontexten kommen, wo das Recht des Stärkeren gilt, wo das Faustrecht und das Messerrecht gilt. [...] Freunde, die Kartellparteien haben das Fundament unseres Staates durch ihre Multikulturalisierungspolitik erodieren lassen. Sie haben unsere über Jahrhunderte gewachsene Vertrauensgemeinschaft mehr oder weniger zerstört. Es hat Jahrhunderte gedauert, bis wir Deutschen als Volk durch viele Konflikte sind wir gegangen. Viele Konflikte mussten wir austragen. Es gelernt haben, gemeinschaftsorientiert zu leben, uns aufeinander zu verlassen und zu vertrauen. Und das ist die Grundlage für Staatlichkeit. Diese Grundlage, dieses Fundament erodiert gerade. Und die Kartellparteien multikulturalisieren und schaffen sich damit die Ursache, um einen Kl-generierten Überwachungsstaat aufzubauen. Und da sagen wir als AfD, als freiheitliche Partei, als Partei der freiheitsliebenden Bürger, nicht mit uns!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 566

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