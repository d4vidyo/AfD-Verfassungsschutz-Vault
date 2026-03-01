---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-09-18
topic: Rechtsstaatsprinzip
page_bfv: 657
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 18.9.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ja, wie Sie wissen, haben wir im Land Brandenburg eine immense Anzahl von vollziehbar ausreisepflichtigen Ausländern, circa 4.500. Rund die Hälfte davon sind vollziehbar ausreisepflichtige Ausländer, bei denen kein Abschiebehindernis besteht. Das bedeutet, sie könnten heute Abend ins Flugzeug gesetzt und außer Landes gebracht werden. Das ist aber nicht gewollt oder nicht gekonnt. Wenn der Staat versagt bei seiner Pflicht, diese Menschen außer Landes zu bringen, dann muss man Alternativen ins Auge fassen. Eine Alternative ist die Privatisierung von Abschiebungen, indem man Abschiebeunternehmen mit ins Boot holt. Das soll so stattfinden, die Unternehmen können sich nach einer öffentlichen Ausschreibung bewerben und wer das beste, das günstigste und das wirtschaftlich am ansprechendste Konzept uns vorlegen kann, der kriegt dann den Zuschlag und darf im Auftrag des Staates Abschiebungen durchführen. Warum dieses Konzept? Wie gesagt, der Staat kann es nicht schaffen. Durch private Abschiebeunternehmen haben wir eine Effizienzsteigerung. Es sind spezialisierte Unternehmen, sie können sich also auch den veränderten Gegebenheiten immer wieder anpassen und vor allem ist es ein optimierter Ressourceneinsatz. Man kann die staatlichen Ressourcen, die offenbar nicht ausreichen, dann sowieso komplett streichen und anderweitig im Staat unterbringen und für anderes ausgeben. Wir haben eine Kostenoptimierung, indem wir einen Wettbewerb stattfinden lassen zwischen diesen Unternehmen. Wer das beste Konzept vorlegt, das habe ich eben schon gesagt, kriegt den Zuschlag und dieser Wettbewerb ist für den Staat Gold wert. Wir werden die besten Anbieter zu den besten Konditionen ins Boot holen können. [...] Wir haben also Punkt 1, die Ausschreibung und die Vergabe an spezialisierte Unternehmen. Wir haben Punkt 2, die Zusammenarbeit, das ist auch wichtig und die Koordination mit staatlichen Stellen, was bedeutet: Natürlich werden Abschiebeunternehmen, private Abschiebeunternehmen nicht im Stich gelassen damit. Sie arbeiten weiterhin mit staatlichen Stellen zusammen und auch so kann natürlich eine Qualitätsüberwachung dieser Unternehmen stattfinden. Wir haben 3. die effizienzorientierten Prozesse und 4. die kontinuierliche Optimierung. Auch das habe ich schon gesagt, man kann sich an veränderte Gegebenheiten anpassen und somit immer wieder tagesaktuell diese Abschiebungen anpassen. Warum das Ganze? Ich habe es eben schon erwähnt, wir haben eine wahnsinnig hohe Zahl von vollziehbar ausreisepflichtigen Ausländern im Land, das wird auch weiterhin zunehmen. Die angekündigten Grenzkontrollen sind Augenwischerei der Altparteien, das ist Wahlkampfgeplänkel, nichts anderes. Wir haben es hier mit einem Ausverkauf der inneren Sicherheit zu tun, seit Jahren schon, so wird es auch weitergehen und deshalb müssen wir jetzt einen Beitrag zur Erhaltung der öffentlichen Sicherheit und Ordnung beitragen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 657

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