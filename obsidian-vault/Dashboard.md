
**Alle Daten stammen aus der [Auswertung des SPIEGEL](https://www.spiegel.de/politik/deutschland/afd-ist-rechtsextrem-hier-sind-die-belege-des-verfassungsschutzes-a-b5fa40e4-a54e-410a-8cc7-ade35d09f77c).**

>[!info]- Alle Personen [[Alle Personen|➡️]]
>```dataview
>TABLE state AS "Bundesland", relevance AS "Relevanz", choice(is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>FROM "Personen"
>WHERE type = "person"
>SORT is_still_member DESC, relevance ASC, state ASC, speaker ASC

>[!todo]- Bewertete Aussagen
>> [!multi-column]
>>>[!success] Legitime Aussagen [[Legitime Aussagen|➡️]]
>>>```dataview
>>>TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>>>FROM "Personen"
>>>WHERE type = "zitat" and status = "Legitim"
>>>SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
>>
>>>[!warning] Fragwürdige Aussagen [[Fragwürdige Aussagen|➡️]]
>>>```dataview
>>>TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>>>FROM "Personen"
>>>WHERE type = "zitat" and status = "Fragwürdig"
>>>SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
>>>```
>>
>>>[!failure] Nicht legitime Aussagen [[Nicht legitime Aussagen|➡️]]
>>>```dataview
>>>TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>>>FROM "Personen"
>>>WHERE type = "zitat" and status = "Nicht legitim"
>>>SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
>>>```

>[!todo] Unbewertete Aussagen [[Unbewertete Aussagen|➡️]]
>```dataview
>TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>FROM "Personen"
>WHERE type = "zitat" and status = "Unbewertet"
>SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
>```
