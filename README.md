### The Google form where you can submit information

[Add biographical information of an author](https://forms.gle/rTPj8gzwJmH9cJE36)

### Snapshot of the expected KG in turtle syntax
<blockquote>
urw:1234 a prov:Person;<br>
&nbsp;&nbsp;&nbsp;&nbsp; rdfs:label 'Nora Keita Jemisin';<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:gender urw:female;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    dul:hasRole urw:Transnational;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:yearOfBirth urw:1972;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:countryOfBirth urw:USA .<br>

urw:5678 a urw:BiographicalSituation ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    dul:isSettingFor urw:USA , urw:1972 , urw:Transnational , urw:female , urw:artist1234 ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    prov:wasDerivedFrom urb:wikidata<br>
    
urb:wikidata  schema:url  "https://www.wikidata.org/wiki/Q2427544" .<br>
</blockquote>


### Graphical representation of the KG snapshot 
![the snapshot of a pattern that represents the author demographics](./img/author_demographic.png)
