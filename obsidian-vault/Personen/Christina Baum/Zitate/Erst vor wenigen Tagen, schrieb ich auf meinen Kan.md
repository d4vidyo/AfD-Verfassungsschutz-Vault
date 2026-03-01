---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-04-25
topic: Menschenwürde
page_bfv: 456
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 25.4.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Erst vor wenigen Tagen, schrieb ich auf meinen Kanälen, dass die Integration von den meisten muslimischen Zuwanderern in unser christliches Abendland gescheitert ist. Wie hart trifft mich nun die Aussage des Staatsschutzes, dass selbst er eingestehen muss, dass nicht mal mehr unsere Kinder in den Schulen vor der Scharia sicher sind. [...] Deutsche Mädchen ohne Kopftuch werden von radikalen Muslimen ermahnt, regelrechte Parallelgesellschaften tummeln sich auf den Schulhöfen, sehr drohende und teilweise gewalttätige Muslime testen ihre Grenzen aus.[...] Wollt ihr ein Kalifat in Deutschland, archaische Kulturen, Frauen, die sich auf unseren Straßen nicht mehr sicher fühlen können? [...] Solange der Anteil islamischer Bürger die Minderheit darstellt, mag das Zusammenleben funktionieren. Doch jetzt, wo sich die Verhältnisse ändern, zeigt der Islam sein wahres Gesicht. Andersgläubige werden nicht geduldet. Das Ziel ist die Unterwerfung unter den Islam. [...] Jetzt muss unserer Toleranz ein Ende gesetzt werden, wenn wir in unserem eigenen Land wieder Herr über unsere Kultur, Tradition und Identität sein wollen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 456

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