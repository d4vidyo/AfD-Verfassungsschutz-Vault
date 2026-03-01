---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2025-02-11
topic: Menschenwürde
page_bfv: 923
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 11.2.2025 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Sie müssen sich jetzt auch vorstellen, Sie sagten jetzt gerade, wir sind an vielen Asylunterkünften, Sie sind gar nicht an Asylunterkünften vorbeigefahren, das waren schlichtweg normale Mietswohnungen. Sie haben einen Ausschnitt aus der Lebensrealität hier, vor allem aus dem Gelsenkirchener Süden gesehen, also viel Müll, der einfach schlichtweg abgelagert wird von Menschen, die den Müll teilweise einfach aus dem Fenster rauswerfen. Wenn jetzt wärmere Bedingungen wären, würden Sie sehen, wie es dann vor den jeweiligen Eingangstüren aussieht, man grillt dann gerne, plötzlich auf dem Bürgersteig, also alles das, was für Sie kulturfremd ist, wird dann hier gelebt, weil schlichtweg bestimmte Bevölkerungsethnien hierin einer Masse angekommen sind und wir kennen das Problem, keine Wohnsitzauflage, dann fährt man dahin, wo man eben jemanden kennt und dann passiert das, was wir da hinten wahrnehmen, es ist ein Straßenzug an arabischen Geschäften. [...] Sie müssen sich vorstellen, wir reden vom Bevölkerungsaustausch, dafür landen wir im Verfassungsschutzbericht. [...] Das ist eine reine Umvolkung, die man hier erlebt. Sie sehen teilweise zu bestimmten Uhrzeiten, dass Kinder von sechs, sieben Jahren kleine Mädchen schon Kopftücher tragen. Sie können auch gerne durch die Innenstadt, Sie sehen allein die Masse, die Masse, ich kenne das von früher nicht. Es ist die Masse von immer jünger werdenden Mädchen, die Kopftuch tragen. Das ist nicht die deutsche Kultur. [...] Diese völlige enthemmte Respektlosigkeit, die in dieser Gesellschaft Einzug erhalten hat. Und ich sage Ihnen das ganz deutlich, das hat sehr wohl mit einer bestimmten Kultur zu tun. Das ist so. Das hat mit einer Kultur zu tun und das wollen einige aber hier einfach schlichtweg ignorieren. [...] Aber ich erlebe immer wieder in dieser Gesellschaft, dass Menschen tatsächlich so einen Bogen machen, weil sie einfach immer wieder den Konflikten aus dem Weg gehen. Das ist so spürbar, wie die Deutschen und das sind dann die Bio-Deutschen, von denen Sie gerade gesprochen haben, die gehen den Konflikten aus dem Weg. Sie meiden, sie wechseln lieber die Straßenseite, weil sie sagen, das ist mir zu heikel. Und ich finde, das ist so traurig, wie die Selbstbehauptung in diesem Land so dermaßen nachgelassen hat. Aber wen wundert es? Es wird von dieser Politik vorgelebt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 923

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