---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2024-08-27
topic: Menschenwürde
page_bfv: 166
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 27.8.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>(Re-)Migration nicht auf Islam reduzieren !! Man darf nicht den Fehler begehen und die Religion zum einzigen Kriterium für bzw. gegen (Re-)Migration machen. [...] Denn es gibt neben der Religion, auch noch andere und womöglich viel gewichtigere Faktoren, die gegen die Einwanderung auch nichtmuslimischer Menschen sprechen. Einen der wichtigsten, nämlich die unterschiedlichen Vertrauensniveaus, möchte ich kurz erläutern: Lange Zeit beruhte der Aufstieg unserer Zivilisation auf Kooperation, durch die Menschen in die Lage versetzt worden sind, öffentliche Güter bereitzustellen und sozialen Ausgleich zu schaffen. Zwei der Grundbedingungen hierfür sind relative Homogenität und Vertrauen. [...] Es gab permanente Konflikte mit anderen Stämmen, die bis heute andauern. Und selbst innerhalb der Stämme ist das Vertrauen niedrig. Beispielsweise haben afrikanische Familien ihre eigenen Söhne als Sklaven verkauft. Es gab und gibt also kulturell bedingtes Misstrauen selbst innerhalb dortiger Familien. Die Folge: Besonders ausgeprägte opportunistische Verhaltensweisen, die unsere Gesellschaft gefährden. Mit Religion hat dies nur bedingt etwas zu tun. Es ist nicht sehr klug, Menschen aus Gesellschaften mit niedrigem Vertrauensniveau in unsere Gesellschaft mit immer noch relativ hohem Vertrauensniveau aufzunehmen, weil Moralvorstellungen aufeinanderprallen, die völlig inkompatibel sind. Multireligiosität kann das verstärken, aber teilweise spielt Religion hierbei keine Rolle. Prallen unterschiedliche Moralvorstellungen aufeinander, so erodiert das Vertrauensniveau in unserer Gesellschaft. Und es gibt Studien, die belegen, dass in weiterer Folge auch das Misstrauen unter den Einheimischen wächst. Massenmigration importiert also nicht bloß Misstrauensgesellschaften in unsere Gesellschaft, sondern sät auch noch Misstrauen zwischen Einheimischen, die sich zuvor gegenseitig vertraut haben. Das schwächt die gesellschaftliche Kooperation. Und eine schwache gesellschaftliche Kooperation gefährdet eine funktionierende Staatlichkeit. Es ist daher unklug, den Migrationsdiskurs auf den Islam zu reduzieren. In Wirklichkeit brauchen wir, bei allem Respekt, gar keine Syrer, Afghanen oder Afrikaner, und zwar unabhängig davon, ob sie Atheisten, Juden, Muslime, Christen oder Angehörige anderer Glaubensrichtungen sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 166

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