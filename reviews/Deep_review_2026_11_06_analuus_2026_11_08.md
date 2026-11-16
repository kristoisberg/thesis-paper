# jOOQ antimustrite artikli tagasiside analüüs

**Kuupäev: 8. november 2026.**

Artiklit tasub täiendada eelkõige uuringu piiride, katsete päritolu ja meetodite täpse kirjeldusega. Uue deterministliku baasmeetodi rakendamine, uus andmejaotus, mudelite võrdsustatud seadistustega võrdlus ja korduskäivitused ei ole selle parandusringi jaoks vajalikud, kui artikli väited piirata olemasoleva tõendusmaterjaliga. Nende puudumine jääb siiski uuringu piiranguks, mida sõnastus üksi ei kõrvalda.

Allpool on otsus kõigi tagasiside sisuliste ja väiksemate parandusettepanekute kohta. Korduvad etteheited on ühendatud ning nende asukohad tagasisides on näidatud. Ingliskeelsed tekstiplokid on artiklisse sobivad parandusettepanekud. Eestikeelne tekst põhjendab otsuseid.

Analüüs lähtub failidest **Deep_review_2026_11_06.docx** ja **LLM_Based_SQL_Antipattern_Detection_in_jOOQ_Code__An_Occurrence_Level_Evaluation_and_Repository_Study.pdf**. Asukohad tähistavad selle PDF-i lehekülgi; pärast muudatusi tuleb lähtuda jaotise nimest, tabelist ja nimetatud ankurlausest. Algfaile ei ole muudetud. Täpsustamiseks on kontrollitud ka PDF-ist viidatud avalikke külmutatud materjale ja asjakohaseid algallikaid. Olemasoleva koodi, salvestatud tulemuste ja lihtsate koondarvutuste kontroll ei ole uus detektorikatse.

## Olulised parandused tagasiside tõlgendamisel

1. **Replikatsioonimaterjalide lingid ei puudu PDF-ist.** Lk 27 commit’i tähised on klõpsatavad GitHubi lingid. Probleem on nähtavate aadresside puudumine ning ühe tähise ja lingi sihtversiooni vastuolu.
2. **Seitse tabelirida ei tõesta kaheastmelist katseplaani.** Arhiivis leidub kõigi 16 mudeli ja viibastrateegia kombinatsiooni märkmikke. Tagantjärele ei tohi kirjutada, et katse oli kaheastmeline, kui see tegelikult nii ei olnud.
3. **Maksimaalse paaride arvuga sobitamise kirjeldus on sisuliselt õige.** Avaldatud analüüs kasutab suurendavaid teid, mitte pelgalt ahnet järjestikust paaritamist. Selgitust saab täpsustada tulemusi muutmata.
4. **Klassi puudumine bootstrap-valimist ei tee F1-skoori alati määramatuks.** Kui ennustusi siiski on, on F1 null; määramatus tekib siis, kui ka ennustusi pole. Täpsus, saagis ja F1 vajavad eraldi nimetajate käsitlust.
5. **Gradle, jOOQ ja OpenRouter pole väljamõeldud allikad.** Need on tarkvara või dokumentatsiooni veebiviited, mida tagasiside automaatkontroll hindas sobimatu teadusartikli kriteeriumi järgi.
6. **Factor 2014 vaatamiskuupäev 28.08.2026 ei ole iseenesest vastuolu.** Katsetele võib järgneda kirjandusülevaate täiendamine. Aastaarvu ei tohi tõendita 2025-ks muuta.

## Üldkokkuvõte ja tugevused

Tagasiside kokkuvõte ja kolm tugevust ei nõua eraldi täiendusi. Need kirjeldavad artikli olemasolevaid panuseid: jOOQ lähtekoodi esitus, esinemistaseme märgendus ja korpuse normaliseeritud väljundianalüüs. Sama sisu uuesti lisamine kasvataks kordusi.

Neli üldist nõrkust on käsitletud järgmistes punktides: baasmeetod punktis 4; projektide vähesus punktides 8–9 ja 27; ühe märgendaja ning eelneva koodiraamatu mõju punktides 12–13 ja 25–26; mudelivaliku võrreldavus ning replikatsiooniviited punktides 20–23 ja 35. Tagasiside kaks arvulise kontrolli kokkuvõtet ei vaja artiklisse lisamist: retsensiooni kinnitus pole uuringutulemus.

## Mõisted ja varasemad tööd

### 1 ID Required võib segada võtme nime ja võtme sobimatuse

**Otsus: võtta arvesse.** Tagasiside: jaotise 2.1 ja tabeli 1 käsitlus.

Lk 22 on piirang juba osaliselt öeldud, kuid see peab olema nähtav enne tulemusi. Säilitada tuleb katsetes kasutatud definitsioon: selle asendamine kitsama definitsiooniga muudaks märgendite ja tulemuste tähendust ning eeldaks uut hindamist. Täpsustada tuleb, et nimepõhine haru on uuringu teadlikult lai sõelumisreegel. Olemasolevatest andmetest ei ole artiklis näidatud, kui suur osa juhtudest vastab kummale harule; seda osakaalu ei tohi oletada.

**Paigutus:** jaotises 2.1 lk 3 vahetult enne tabelit 1, pärast lõiku, mis algab „The detector experiments retain seven classes”.

> For ID Required, the operational rule deliberately includes a primary-key column named exactly id, irrespective of whether a suitable alternative key is visible. This naming-based condition is broader than a demonstrated redundant-surrogate-key defect. Agreement and corpus breadth for this class therefore measure application of the study rule; they do not establish that each flagged key is unsuitable for its application.

**Miks hea:** lugeja ei tõlgenda 49,7% failikatvust automaatselt vigaste võtmekujunduste levimusena. Täpsustus kaitseb konstrukti valiidsust ilma uuringut tagantjärele ümber defineerimata.

### 2 Poor Man’s Search Engine reegli ühisosa ja contains meetodid

**Otsus: võtta arvesse, kuid mitte kinnitada täielikku reeglivõrdsust.**

Koodiraamatu otsustuspuu sisaldab nii lahendamata sisendite kaasamist kui ka contains-tüüpi meetodeid. Seega on retsensiooni põhiküsimusele olemas vastus. Samas on otsustuspuu sõnastus WHERE-tingimuste LIKE/ILIKE juhtude kohta kitsam kui viiba üldine viide regulaaravaldistele. Väide, et kogu koodiraamat ja viip olid „exactly the same”, oleks liiga tugev. [S1]

**Paigutus:** asendada tabeli 1 lk 4 vastav definitsioon järgmisega.

> A jOOQ search condition performs full-text-style matching through LIKE/ILIKE, regular expressions, or substring convenience methods such as contains and containsIgnoreCase. Prefix searches are excluded. Both the annotation decision tree for LIKE/ILIKE and the detector instructions include unresolved inputs whose wildcard behaviour is not visible. This inclusion is a conservative screening convention, not confirmation that the input performs full-text search (Karwin 2023, Ch. 17).

**Täiendav paigutus:** jaotise 3.3 lk 10 viimasesse sisulisse lõiku enne seitsme klassi piirangu kirjeldust.

> The search decision tree enumerates WHERE-clause LIKE/ILIKE and substring cases, whereas the detector instruction also names regular expressions. The archived decision tree and prompt should therefore be consulted separately for their detailed boundaries.

**Miks hea:** vastab lahendamata parameetrite küsimusele, lisab tabelis 10 olulised meetodid ja ei peida võimalikku erinevust märgenduse ning detektori juhiste vahel.

### 3 Milline skeemiinfo oli tegelikult vaadeldav

**Otsus: võtta arvesse.** Siia kuuluvad eraldi 31 Flavors ja Fear of the Unknown märkused.

Ei tohi jätta muljet, et kõik andmebaasi piirangud säilivad Java-koodis või et analüüs hõlmas eraldi EnumType-faile. Avaldatud failifilter välistab muu hulgas „implements EnumType” sisaldavad failid; Keys-klassid on abikontekst, mitte iseseisvalt hinnatavad sihtfailid. Fear of the Unknown otsustuspuu kasutab createField-tüübiavaldist, nullable(false) puudumist ning mitte-NULL vaikeväärtust. See sisaldab ka äriloogika vaatamise haru, millele ühe tabelifaili ja Keys-kontekstiga detektoril ei pruugi olla ligipääsu. Vaikeväärtuse olemasolu üksi ei tõesta, et veerg ei saaks olla NULL. [S2, S3]

**Paigutus:** jaotise 2.2 lk 5 lõppu, pärast lauset „source-level detection must interpret DSL calls and generated schema representations…”.

> Schema evidence is limited to declarations present in the retained table source and, for detector requests, the attached key-definition class. Generated column declarations expose data types, nullability and default-value expressions; CHECK or ENUM evidence is usable only when represented in the supplied source. Standalone EnumType implementations are excluded from the analysed-file frame. The absence of a visible declaration does not establish the absence of the corresponding database property.

**Paigutus:** jaotise 6.1 lk 24 esimese lõigu lõppu.

> For Fear of the Unknown, the codebook treats a nullable declaration with a non-null default as one screening condition and also permits inspection of business logic. A default does not itself prevent explicit NULL values, and business-logic evidence may be unavailable in a single-file detector request. These conditions can therefore introduce both construct ambiguity and differences between the evidence available to the annotator and the detector.

**Miks hea:** kirjeldab tegelikku vaadeldavuspiiri ja tunnistab konkreetset semantilist lihtsustust. Üldine jOOQ tutvustus seda piirangut ei asenda. AST kasutamist ei tohi lisada, sest avaldatud eeltöötlus on tekstipõhine.

### 4 Deterministliku baasmeetodi puudumine ja staatilise analüüsi raamimine

**Otsus: võtta arvesse piirangu ja tasakaalustatud võrdlusena; uut baasmeetodikatset mitte teha.** See katab üldnõrkuse „Absence of a Deterministic Static Analysis Baseline”, jaotise 2.3 etteheite ning jaotiste 5.3 ja 7 korduva baasmeetodisoovituse.

Kriitika on sisuliselt põhjendatud: osa domineerivatest reeglitest sobib deterministlikuks tuvastamiseks. Uue AST-/regulaaravaldisepõhise detektori loomine ja hindamine oleks siiski uus eksperiment. Ka „semantilist järeldamist nõudvate” juhtude täpne osakaal vajaks uut juhtumite klassifitseerimist. Tabeli 10 kategooriad kirjeldavad juba leitud fragmente, mitte baasmeetodi saagist, täpsust või ülemist jõudluspiiri.

**Paigutus:** tabeli 2 lk 7 „API or AST rules” rea parempoolne lahter asendada.

> Can localise local syntactic conditions, including primary-key naming and explicit all-column projections. Broader coverage requires rules for additional jOOQ idioms and, for some classes, key context or domain interpretation.

**Paigutus:** jaotise 2.3 lk 6 lõppu, enne tabelit 2.

> The retained classes combine relatively local conditions with interpretative ones. Primary-key naming and several all-column projection forms are amenable to deterministic rules. Other decisions concern suitable candidate keys, inferred relationships, or the domain meaning of values and identifiers. Evaluating an LLM across these classes measures its agreement with the operational codebook; it does not establish that an LLM is necessary for every class.

**Paigutus:** jaotise 5.3 lk 23 baasmeetodi lõigu algusse.

> No deterministic jOOQ baseline was evaluated. The present results therefore do not quantify an LLM advantage in agreement, cost, or runtime over explicit rules, including for the two dominant classes. The fragment categories in Table 10 describe detector-returned output and cannot estimate the coverage of an independent rule-based detector.

**Miks hea:** piirab täpselt seda võrdlevat järeldust, mida olemasolevad katsed ei toeta. Artikli tegelikud RQ-d küsivad kooskõla ja väljundi jaotust, mitte LLM-i paremust. Puuduse aus avaldamine ei taga, et retsensent baasmeetodi puudumise aktsepteerib.

### 5 Varasemate ORM ja LLM uuringute käsitlus

**Otsus: võtta arvesse.** Kirjandusülevaadet saab parandada eksperimente tegemata.

Piisab kahest otseselt asjakohasest, kontrollitud tööst. Chen jt uurivad ORM-i liigset andmekasutust staatilise ja dünaamilise analüüsi kombinatsiooniga. Seda ei tohi esitada puhtalt staatilise jOOQ-detektorina. Silva jt ESEM 2024 artikkel hindab ChatGPT-ga Java koodilõhnade tuvastamist ning sobib eelretsenseeritud täienduseks bakalaureusetöö kõrvale. Teadustöö väärtust ei määra üksnes väljaande piirkondlikkus. [S4, S5]

**Paigutus:** jaotises 2.3 lk 6 pärast SQLChecki ja Eessaare töid käsitlevat lõiku, enne „Prior LLM studies…”.

> Host-language database analysis also extends beyond SQL-string extraction. Chen et al. (2016) combine static identification of database-accessing methods with execution traces and generated SQL to locate redundant ORM data access. Their runtime-dependent objective differs from the present source-only jOOQ localisation task. For general Java code smells, Silva et al. (2024) evaluate ChatGPT using generic and smell-specific prompts. Their study provides peer-reviewed evidence on prompt-sensitive recognition, while the present evaluation matches multiple class-labelled line spans within files.

**Tabel 2:** lisada rida „Hybrid ORM analysis”; esituseks „Host-language access methods, execution traces and generated SQL”; väljundiks „Redundant-access locations”; seoseks „Requires execution evidence; addresses redundant access rather than the seven jOOQ operational classes”. Viide Chen jt.

**Kirjanduskirjed:**

- Chen TH, Shang W, Jiang ZM, Hassan AE, Nasser M, Flora P (2016). *Finding and Evaluating the Performance Impact of Redundant Data Access for Applications that are Developed Using Object-Relational Mapping Frameworks*. IEEE Transactions on Software Engineering 42(12), 1148–1161. DOI: [10.1109/TSE.2016.2553039](https://doi.org/10.1109/TSE.2016.2553039).
- Silva LL, Silva JR, Montandon JE, Andrade M, Valente MT (2024). *Detecting Code Smells using ChatGPT: Initial Insights*. ESEM 2024, 400–406. DOI: [10.1145/3674805.3690742](https://doi.org/10.1145/3674805.3690742).

**Miks hea:** parandab võrdlusraami ilma mahukat kõrvalteemalist ülevaadet lisamata. Bakalaureusetöö võib jääda, kui sellel on artiklis konkreetne roll.

### 6 Karwini peatüki viide tabelis 1

**Otsus: võtta arvesse.**

**Paigutus:** tabeli 1 lk 4 „Implicit Columns” definitsiooni lõpp.

Asendada „(Karwin 2023; jOOQ 2025f, Ch. 19)” tekstiga **„(Karwin 2023, Ch. 19; jOOQ 2025f)”**.

**Miks hea:** peatükinumber seostub õige allikaga; tegemist on üheselt parandatava viitamisveaga.

## Uuringu kavand ja meetodid

### 7 Andmejaotuse täpne sihifunktsioon

**Otsus: võtta arvesse.** Valem on säilinud märkmikus; seda pole vaja oletada. [S6]

**Paigutus:** jaotises 3.5 lk 12 asendada lõigu „We then evaluated all 1000000 integer seeds…” keskmine osa, mis kirjeldab varieeruvust ja tulemust.

> For class c and split s, let n_cs be the occurrence count and let μ_c = (n_c,train + n_c,val + n_c,test)/3. We minimised the sum of squared coefficients of variation, J = Σ_c [(1/3)Σ_s(n_cs − μ_c)²]/μ_c², using the population standard deviation across the three splits. Candidates required at least eight training occurrences and at least one validation and one test occurrence for every retained class. Seed 767573 achieved J = 0.5168, reported as 0.52.

Valem tuleks lõplikus LaTeX-versioonis esitada eraldi võrrandina. Tabeli 3 arvud annavad J ≈ 0,516773925, mis kinnitab olemasolevat väärtust.

**Miks hea:** muudab valiku korratavaks ja taastab ka seni välja jäetud kandidaadipiirangud. Toorhälvete ruutude summa ei annaks artiklis esitatud skaalat.

### 8 Klasside vähene projektitugi

**Otsus: võtta arvesse tõlgenduse piiranguna; andmejaotust mitte muuta.**

Artikkel näitab projektide arvu juba tabelis 3 ja arutab vähest tuge jaotises 6.4. Täpsustada tasub tulemuste juures, sest 31 Flavors F1 = 0,974 võib muidu näida laiapõhjalise tõendina. Uus jaotus muudaks arenduse, valiku ja hindamise andmerolle ning nõuaks uusi katseid.

**Paigutus:** jaotises 4.2 lk 17 pärast makro- ja kaalutud tulemusi käsitlevat lõiku.

> Project support differs markedly across classes. The 39 test references for 31 Flavors come from one repository, and the 16 Rounding Errors references come from two. Their scores describe performance on these observed project cases and provide limited evidence about transfer to other projects. Implicit Columns and ID Required have support in 20 and 16 test repositories, respectively.

**Miks hea:** seab suurima ja väiksema projektitoega klassid õiglasesse võrdlusraami. Täiendavat põhjendust, miks ajalooliselt projektipiirangut ei kehtestatud, ei tohi tagantjärele välja mõelda: piisab tegeliku optimeerimiskriteeriumi kirjeldusest punktis 7.

### 9 Bootstrap ja nullnimetajad

**Otsus: võtta arvesse parandatud matemaatilise selgitusena.**

Avaldatud programm jätab iga mõõdiku protsentiilidest välja selle mõõdiku lõplikku väärtust mitte andvad kordused. See ei asenda neid nulliga. Tagasiside arutelu vajab täpsustust: kui TP + FN = 0, on saagis määramata; kui FP > 0, võib F1 siiski olla null. F1 on määramata juhul, kui 2TP + FP + FN = 0. [S7]

**Paigutus:** jaotises 3.7 lk 15 bootstrap-lõigu lõppu.

> For each metric, bootstrap percentiles use only replicates with a non-zero denominator; undefined values are not replaced by zero. Recall is undefined when TP + FN = 0, precision when TP + FP = 0, and F1 when 2TP + FP + FN = 0. A replicate without reference occurrences can still have F1 = 0 if it contains unmatched predictions. Class-specific output records the number of defined replicates.

**Miks hea:** dokumenteerib tegeliku käitumise. Retsensiooni ligikaudsed klassi puudumise tõenäosused ei ole automaatselt kõigi kolme mõõdiku määramatuse tõenäosused.

### 10 Paaritamismeetodi võimalik ahnus

**Otsus: võtta arvesse selgitusena; algoritmi muuta pole vaja.**

Avaldatud match_count-funktsioon järjestab kandidaadid IoU järgi, kuid otsib seejärel rekursiivselt suurendavaid teid ja võib varasemaid paare ümber paigutada. Seega sobib tagasiside variant b: maksimaalse paaride arvuga kaalumata sobitamine, mille läbimisjärjekord on määratud. See ei optimeeri paaride IoU-de kogusummat. [S7]

**Paigutus:** jaotises 3.7 lk 14 asendada „Candidate lists are ordered…” lause.

> The implementation uses augmenting paths to obtain a maximum-cardinality matching. Adjacency lists are ordered by descending IoU and predicted span, with source order resolving remaining ties. This ordering makes the procedure deterministic; it does not define a greedy assignment or an optimisation of total matched IoU.

**Miks hea:** kõrvaldab reprodutseeritavuse küsimuse olemasolevat korrektset meetodit muutmata.

### 11 Korduskatsete eelarve ja ebaõnnestunud failid

**Otsus: võtta arvesse, kuid mitte kinnitada 100% õnnestumist.**

1000 ja kahe lubatud korduskatse erinevus on õigustatud küsimus. Säilinud andmed ei sisalda täielikku lõplike vigade ega negatiivsete vastuste registrit. Koondpäringute arv ei tõesta, et iga fail andis korrektse vastuse. Pelk väide „kõik failid töödeldi edukalt” oleks tõendamata. [S8]

**Paigutus:** jaotises 3.6 lk 14 kohe pärast kahte korduskatsete arvu kirjeldavat lauset.

> The retained archive does not contain a complete file-level ledger of successful empty responses and terminal failures. It therefore cannot establish a 100% successful-response rate for the corpus run. The 17988-file denominator is the eligible source frame; an absence of archived positive output does not independently verify a successful negative detection.

**Paigutus:** jaotises 6.2 lk 24 viimase lõigu ette.

> Any terminal request failures among eligible files would reduce observed flag breadth and density. Their contribution cannot be separated from negative detections using the preserved positive-output archive.

**Miks hea:** nimetab võimaliku kallutatuse suuna ja ulatuse määramatuse. Uus käivitus ei parandaks algse käivituse puuduvat sündmusregistrit.

### 12 Koodiraamatu loomine enne projektide jaotamist

**Otsus: võtta arvesse kõrge prioriteediga.**

Projektide lahusus ei tähenda, et kogu otsustusreeglistik oleks kujunenud testprojektidest sõltumatult. Kõigi 61 projekti põhjal täiendatud koodiraamat mõjutas viipu. Puudub alus kinnitada, et iga lõplik erand oli ka treeningandmetes olemas. Artiklit tuleb täpsustada ilma tõendamata reegli päritolu väitmata.

**Paigutus:** jaotises 3.4 lk 11 koodiraamatu iteratiivse täiendamise lõigu lõppu.

> Codebook refinement preceded project partitioning and could therefore incorporate variants from repositories later assigned to validation or test. Project-disjoint evaluation separates prompt iteration and configuration selection from test execution, but it does not make operational-definition development independent of the complete annotated sample.

**Paigutus:** jaotises 3.6 lk 13 lause „The resulting instructions stated…” järel.

> The prompts inherited this sample-informed codebook. Although prompt iteration used the training partition, the study does not establish that every inherited variant or exclusion was independently represented in training projects.

**Miks hea:** eristab testväljundi järgi viiba häälestamist ja varasemat mõistete kohandamist. Ei nimetaks kogu uuringut automaatselt kehtetuks, kuid ei kasutaks absoluutset väidet, et test oli kõigis uurimisetappides puutumatu.

### 13 30 päeva järel tehtud kordusmärgenduse ulatus

**Otsus: võtta arvesse.** Vajalik teave on olemasolevates CSV-failides.

128 faili kordusmärgenduse võrdlus ei olnud piiratud seitsme hiljem valitud klassiga. Algse ja kordusmärgenduse ühendatud sündmustes esineb 15 erinevat klassi; see on 19 klassiga koodiraamatu põhine kontroll. 64 algselt märgendamata failist 63 jäid märgendamata ja ühes lisandus vähemalt üks sündmus. Need on salvestatud kirjete koondid, mitte uus märgendus. [S9]

**Paigutus:** jaotises 3.4 lk 11 enne „We compared the original and repeated records…”.

> The repeat-annotation check used the original 19-class annotation scope, rather than restricting records to the seven subsequently retained detector classes. Fifteen classes occur in the union of the two passes. Of the 64 files without original annotations, 63 remained unannotated and one received an annotation in the repeated pass.

**Miks hea:** piiritleb, mille korduvust F1 = 0,925 mõõdab. Seda tulemust ei saa üksüheselt esitada seitsme klassi märgenduse usaldusväärsusena.

### 14 Failifiltrid ja lähtekoodi rollid

**Otsus: võtta arvesse.** Artiklis piisab lühikirjeldusest ja täpse koodiviite lisamisest; kogu välistusloetelu põhiteksti kopeerida pole vaja.

**Paigutus:** jaotises 3.8 lk 15 asendada „Files containing the detector’s generated-table indicators…” lause.

> The reconstructed source frame uses lexical file-content tests. A selected file is assigned the generated-schema role when it contains at least one of “This class is generated by jOOQ”, “extends TableImpl”, or “extends org.jooq.impl.TableImpl”; remaining selected files form the application/query role. These indicators classify files for analysis and are not resolved Java type relationships.

**Paigutus:** jaotise 3.3 lk 10 failivälistuste lõigu lõppu.

> File selection combines case-sensitive path-fragment exclusions, a requirement for at least one of org.jooq, Tables or tables in the file contents, and exclusions for listed generated-artifact signatures. The exact lists are preserved in the released file-discovery implementation and the source-frame reconstruction script.

Lisada viited [S3] ja [S10].

**Miks hea:** lugeja saab aru, et tegemist pole AST ega tüüpide lahendamisega. Versioonid tuleb eristada: avaldatud rekonstruktsioonifilter ei tõesta automaatselt kõigi ajalooliste käivituste filtreid.

### 15 Lähima Keys klassi valik ning konteksti piirid

**Otsus: võtta arvesse valikureegli osas; tokenipiiride kohta mitte leiutada tulemust.**

Avaldatud teostus valib „public class Keys ” sisaldavate failide seast sihtfaili suhtelise teega pikima ühise märgiprefiksiga faili. See pole paketinimede ega kataloogisegmentide semantiline kaugus. Võrdse tulemuse korral jääb esimene sorteeritud teega kandidaat. [S3]

**Paigutus:** jaotises 3.6 lk 13 kohe pärast „The request for generated source also received the closest generated key-definition class.”

> In the released implementation, Keys candidates are files containing the literal signature “public class Keys ”. Selection maximises the character-level common prefix of the candidate and target relative paths. Paths are sorted before selection, so the first candidate resolves ties. No Keys candidate yields empty attached context; this is a lexical proximity heuristic rather than Java symbol resolution.

**Konteksti piiramine:** artiklis nimetatud korpuseversiooni `245b50a` kood sisaldab ka automaatset märgipõhist viibaeelarvet ja kärpimist. Vaikimisi annab Claude'i mudelimuster 240 000 märgi eelarve; kasutaja määratud väärtus saab selle asendada. Kood eelistab sihtfaili ning lisab Keys-konteksti alles ülejäänud eelarve ulatuses. Üle eelarve sihtfaili korral säilitatakse algus ja lõpp ning märgitakse väljajätt. Tegemist on teostuse reegli, mitte tõendiga, mitu faili käivituses kärbiti. [S17]

**Paigutus:** jaotises 3.6 lk 13 lähtekoodi nummerdamise lõigu lõppu lisada:

> The corpus-source revision also implements character-budget truncation. Without an override, its Claude model rule allocates 240000 prompt characters, prioritises target-file content and fits Keys context into the remaining budget. Oversized target files retain beginning and ending lines with an omission marker. This is a character heuristic rather than exact token accounting; retained records do not establish how many original requests were truncated.

**Tokenipiirid:** lk 26 jaotise 6.5 lõppu lisada:

> Complete request records and per-file token accounting were not retained, so the archive does not establish whether every assembled request stayed within the applicable context and output limits.

**Miks hea:** taastab rakendatava reegli. Väidet „ükski fail ei ületanud piirangut” ei saa positiivsete väljundite olemasolust järeldada. Ajaloolise versiooni erinevuse korral tuleb kirjeldada just selle teostust.

### 16 Identse sisu kaalumise valem

**Otsus: võtta arvesse.** Failikoopia kaal ja sündmusekoopia kaal on eraldi nimetajatega. [S10]

**Paigutus:** jaotises 3.8 lk 16 asendada lause „We weight each unique content and event once across its physical copies…”.

> For content hash h with k_h physical file copies, each copy contributes 1/k_h to eligible-file weight. For an exact-content event e, let m_e be the number of canonical file occurrences reporting that event; each such occurrence contributes 1/m_e to event weight. Repository totals sum the corresponding contributions. Thus each unique content and each observed union event contributes one unit globally, without assignment to an arbitrary representative repository.

**Miks hea:** erinevate väljunditega identsete failide korral ei pruugi sündmus esineda kõigis k_h koopias. Seetõttu oleks üksnes ühise 1/k valemi lisamine mõlemale suurusele ebatäpne.

### 17 Sõnastus was recorded as using

**Otsus: soovitatud kategoorilist asendust mitte võtta; lauset siiski täpsustada.**

Retsensendi soovitus kirjutada lihtsalt „used the same … templates” on liiga tugev, kui täielikud päringud ei ole säilinud. PDF ütleb, et 80f3ff4 ja 245b50a viibad on identsed, kuid viidatud README-versioon kirjeldab algse käivitusbinaari päritolu ettevaatlikumalt. Seda dokumentatsioonierinevust tuleb korrastada, mitte keeletoimetamisega peita. [S8]

**Paigutus:** jaotises 3.6 lk 14 asendada „The corpus execution was recorded as using…” ja jaotises 3.8 lk 16 kustutada selle kordus.

> The execution records identify the selected model, settings and Zero-Shot prompt family for the corpus run. The cited source revisions preserve matching embedded prompt templates; incomplete request records nevertheless prevent verification of every submitted payload and backend configuration.

**Kontroll:** kahe artiklis nimetatud versiooni `src/prompts.ts` sisu on identne. Samuti on neis identsed viiba koostamise failid; faililugemise teostus erineb kodeeringu käsitluse poolest. Hilisem avaldatud `cf82fe5` versioon erineb nii viibafaili kui ka kärpimisloogika poolest, mistõttu tuleb ajaloolise käitumise selgitamisel viidata õigetele versioonidele. README vananenud väited käivitusversioonide puudumise kohta tuleb nende leidudega kooskõlastada. [S17]

**Miks hea:** eristab kontrollitud lähtekoodisarnasust ja tegelikult saadetud päringuid. Viipade identsus ei tähenda kogu eeltöötluse või päringute identsust.

### 18 Korduvuse suhtarvu nullnimetaja

**Otsus: võtta arvesse.**

**Paigutus:** jaotise 3.8 lk 15 kolme valemi järel lisada.

> Breadth and density are defined for F_rc > 0. Within-file repetition is defined only for A_rc > 0; it is undefined, rather than zero, when no eligible file is flagged.

**Miks hea:** täiendab valemite määramispiirkonda; tulemusi pole vaja muuta.

### 19 Ülemise detsiili võrdsed piirväärtused

**Otsus: võtta arvesse väikese selgitusena.**

**Paigutus:** jaotises 3.8 lk 16 asendada lauseosa „with repository name breaking cutoff ties” ja sellele järgnev piiride selgitus järgmisega.

> Repository name breaks cutoff ties when a single reproducible membership list is required. Reported sensitivity bounds additionally consider every admissible selection among repositories tied at the cutoff.

**Miks hea:** üks määratud nimekiri ja kõigi võimalike nimekirjade tundlikkusanalüüs saavad üheaegselt kehtida.

## Mudelivalik ja tulemused

### 20 Mudelite erinevad arutlusrežiimid

**Otsus: võtta arvesse; võrdsustatud seadistustega võrdlust mitte teha.**

See oli konfiguratsioonide praktiline võrdlus, mitte kontrollitud katse arutlusrežiimi või mudeli sisemise kiiruse mõju eraldamiseks. Samuti mõjutavad aega marsruutimine, teenusepakkuja, korduspäringud ja võimalik koormus. Uute seadistustega käivitamine oleks uus eksperiment.

**Paigutus:** jaotises 4.1 lk 16 enne valitud konfiguratsiooni põhjendavat lõpulauseid.

> Table 4 compares the observed model–configuration combinations, not models under matched reasoning budgets. Cost and wall-clock time jointly reflect reasoning settings, provider routing, retries and service conditions. These observations support a practical configuration choice but do not isolate an intrinsic model-speed or reasoning-mode effect.

**Miks hea:** väldib põhjendamata põhjuslikku tõlgendust. Seadistuste kirjeldus jaotises 3.6 jääb alles.

### 21 Kas tehti seitse või kuusteist konfiguratsioonikatset

**Otsus: võtta arvesse aruandluse selguse osas; tagasisides oletatud kaheastmelist katseplaani mitte automaatselt omaks võtta.**

Arhiivis on 16 kombinatsiooni märkmikud. Tabeli 4 allkiri ütleb juba, millised seitse kombinatsiooni seal esitatakse. Vajalik on eristada kogu katsemaatriksit, tabeli valikut ning täpselt nende arvude päritolu. Viidatud README hoiatab, et säilinud 1159-failised märkmikud ei kinnita üksüheselt varem raporteeritud valideerimistabeli failiarvu, kulu ja aega. Seetõttu ei saa puuduvaid ridu või kolmandat komakohta lihtsalt teise arhiiviversiooni tulemuste järgi täita. [S8]

**Paigutus:** jaotises 4.1 lk 16 asendada esimese lõigu lause „The comparison also included…” järgmisega.

> The archived validation material contains all 16 combinations of four models and four prompting strategies. Table 4 presents a compact subset: all four Zero-Shot configurations and the three alternative prompts for Claude Opus 4.5. This presentation should not be interpreted as evidence of a two-stage screening design.

**Enne lõplikku versiooni:** lisada tabeli 4 juurde täpne viide selle seitsme rea lähteväljunditele. Kui säilinud väljundeid ja nende failiraami ei saa siduda, lisada:

> The surviving validation notebook copies do not establish an exact reconstruction of the file frame, costs and runtimes underlying every reported Table 4 entry; these values are retained as historical selection records.

**Miks hea:** täpsustab katsekatvuse ilma ajaloolist katseplaani välja mõtlemata. See on dokumenteerimise küsimus, mida uus katse ei lahendaks tagasiulatuvalt.

### 22 Valiku kompromiss ja valideerimismõõdikute täpsus

**Otsus: võtta arvesse valiku põhjenduse osas; uusi mõõdikuid ega näilist täpsust mitte nõuda.**

Valikut ei saa nimetada parimaks täpsuse ega madalaima kulu järgi. Olemasolev tabel näitab praktilist kompromissi. Eelnevalt fikseeritud kaaludest või lävenditest pole tõendit; neid ei tohi tagantjärele esitada eelmääratud otsustusreeglina. Kolmas komakoht ja makro-F1 sobivad ainult samade algsete väljundite juba olemasolevate kokkuvõtete põhjal. Kahe komakoha ümardatud arvust täpsemat tulemust ei taasta.

**Paigutus:** jaotise 4.1 lk 16 viimase lause „We therefore selected…” asemele.

> We made a pragmatic selection that prioritised the short observed batch runtime and the simpler Zero-Shot prompts over the additional displayed agreement obtained with reasoning-oriented prompts. The selected configuration was neither the least expensive nor the highest-scoring configuration in Table 4. This was an observed trade-off, not an optimum under a prespecified weighted decision rule; equal displayed scores also need not be equal before rounding.

**Miks hea:** selgitab tegelikult nähtavat valikut ja ei varja GLM-5 madalamat kulu või CoT kõrgemat tulemust. Ei lisaks uusi valideerimisanalüüse üksnes tabeli laiendamiseks.

### 23 Kogu korpuse maksumus ja kestus

**Otsus: võtta arvesse olemasolevate dokumenteeritud väärtuste piires.**

Säilinud kestusmärkmiku väljund annab projektide analysis_runtime summaks 12 391 sekundit ehk 3 h 26 min 31 s. See pole automaatselt kogu käivituse seinakellaaeg. Corpus-käivituse dollarikulu ei saa hinnata testkulu failide arvuga korrutades, sest sisendimahud ja korduspäringud erinevad. [S11]

**Paigutus:** jaotises 4.3 lk 19 esimese lõigu järel.

> The archived per-repository analysis_runtime values sum to 12391 seconds. This aggregate is not a separately verified end-to-end wall-clock measurement. A corpus-run API cost is not reported because no verified total is available in the cited execution summary.

**Miks hea:** lisab olemasoleva kasuliku suuruse ja eristab seda mõõdikust, mida ei saa kinnitada. Kui autoril on tegelik arve- või juhtpaneeli väljavõte, asendada viimane lause selle kontrollitud summaga; uut käivitust pole vaja.

### 24 Kaheksa erineva väljundiga identse sisuga failirühma

**Otsus: võtta arvesse ettevaatliku seosena; põhjuste arvulist jaotust mitte oletada.**

SHA-256 võrdsus kehtib Java-faili kohta, mitte kogu päringu, võtmekonteksti, failitee ega täitmistingimuste kohta. Ka võimalike põhjuste loend pole ammendav: erinevused võivad hõlmata päringu muid välju ja täitmisseisundit. Täielike päringute puudumisel ei saa kaheksat rühma jagada tõendatud kontekstierinevuse ja API juhuslikkuse rühmadeks. Need pole ka kontrollitud korduskatse ega mudeli varieeruvuse statistiline piir.

**Paigutus:** jaotises 4.3 lk 20 pärast lauset „Eight groups of byte-identical files have inconsistent sets of detector events.”

> These groups establish inconsistency across identical target-file contents, not across verified identical complete requests. Attached key context, other request fields or execution conditions may differ. The retained archive does not support a causal allocation of the eight groups to context differences or inference variability.

**Paigutus:** jaotises 6.5 lk 25 pärast lauset „leaving run-to-run variance unmeasured”.

> The eight inconsistent exact-content groups in Table 9 provide an additional warning about output stability within the corpus execution, but they are not controlled repeated calls with verified identical payloads and do not estimate run-to-run variance.

**Miks hea:** ühendab olemasolevad tähelepanekud ülehindamata nende põhjuslikku või statistilist tõendusjõudu.

### 25 Tabeli 6 jääkvead ja puuduv Keyless Entry FN

**Otsus: võtta arvesse tabeli eesmärgi täpsustamisena; uut täielikku veataksonoomiat mitte koostada.**

Tabel 6 lubab juba „Dominant disagreement mechanisms”, mitte ammendavat jaotust. Seetõttu ei pea selle iga rea selgitused liituma kõigi FP/FN arvudeni. Kasulik on siiski jäägid nähtavaks teha. Põhjuste täpne jaotus vajaks kõigi juhtumite auditeeritavat ümberkodeerimist; ainult koondtulemuste põhjal ei saa omistada igale juhtumile põhjust.

**Paigutus:** tabeli 6 lk 18 allkirja lõppu.

> Mechanisms are illustrative rather than a mutually exclusive, exhaustive coding of every disagreement. Residual counts below are not assigned a more specific cause unless supported by the retained review record.

**Tabeli 6 ridade täiendused:**

- Implicit Columns: „The remaining seven disagreements comprise four false positives and three false negatives.”
- ID Required: „The remaining 22 disagreements comprise 12 false positives and ten false negatives.”
- Keyless Entry: „The remaining disagreements comprise 14 false positives and one false negative; the table does not provide a separate causal classification for that false negative.”

**Miks hea:** teeb lugejale nähtavaks, mida tabel katab ja mida mitte, põhjuseid leiutamata. Täielikku arvulist põhjuste jaotust võib lisada ainult olemasoleva juhtumipõhise ülevaatuse tõendite alusel. Punktis 32 kirjeldatud failitee lahknevus on konkreetne näide, mida saab pärast lähtefailiga kinnitamist kasutada üldsõnalise „reference errors” asemel.

### 26 Parandatud võrdlusandmestiku klassipõhised tulemused

**Otsus: võtta arvesse.** Need tulemused on säilinud; uut mudelikatset ega uut märgendusvooru pole vaja. [S12]

**Paigutus:** jaotises 4.2.1 lk 18 pärast lõiku „We treat this result as an optimistic sensitivity analysis.” Lisada järgmine kompaktne tabel.

| Class | Original-reference F1 | Revised TP | Revised FP | Revised FN | Revised-reference F1 |
|---|---:|---:|---:|---:|---:|
| Implicit Columns | 0.960 | 256 | 1 | 15 | 0.970 |
| ID Required | 0.860 | 101 | 1 | 7 | 0.962 |
| Keyless Entry | 0.693 | 49 | 16 | 0 | 0.860 |
| Fear of the Unknown | 0.481 | 42 | 1 | 17 | 0.824 |

**Tabeli allkiri:**

> Detector-informed reference sensitivity for the four classes whose counts changed. The predictions are unchanged. These exploratory values are not independent validation and do not replace Table 5.

Ülejäänud kolme klassi arvud ei muutu. Arvutused kasutavad F1 = 2TP/(2TP + FP + FN). Üldine micro-F1 = 0,932 ei ole sama mis märkmikus leiduv toetusega kaalutud F1 = 0,9309; neid ei tohi segada.

**Miks hea:** näitab, milliseid klasse võrdlusandmete puudused enim mõjutavad. „Optimistlik tundlikkusanalüüs” on põhjendatud nimetus; „tõelise täpsuse ülemine piir” või „parandatud tõde” ei oleks.

### 27 Makro ja klassipõhiste bootstrap intervallide lisamine

**Otsus: põhiteksti uut intervallikomplekti mitte lisada.**

Makro- ja kaalutud punktihinnangud on tabeli 5 juures juba olemas. Mikrotulemuste projektitundlikkus on olemas. Harva esinevate klasside puhul ei lahenda uus intervallitabel ühe või kahe projekti probleemi; määramata korduste valik võib tõlgendust hoopis raskendada. Makrointervallide lisamiseks oleks vaja valida ja dokumenteerida puuduvate klasside käsitlus ning teha uus järelanalüüs. See pole praeguste RQ-de vastamiseks hädavajalik.

**Täiendus olemasolevale tekstile:** jaotises 6.4 lk 25 pärast lauset „Many resamples contained no annotated occurrences of some rare classes…” lisada.

> Bootstrap resampling cannot create additional independent project support for a sparse class. We therefore emphasise the observed class counts and scores rather than treating rare-class resampling intervals as evidence of broad cross-project generalisation.

**Miks hea:** vastab sisulisele murele vähese projektitoe ülehindamiseta. Kui klassipõhine salvestatud bootstrap-väljund on juba avalikus lisas, võib sellele viidata, kuid põhiteksti laiendamine pole vajalik.

### 28 61 märgendatud projekti kuulumine 602 projekti korpusesse

**Otsus: võtta arvesse tõlgenduse täpsustusena; 541 projekti lisaanalüüsi mitte nõuda.**

Artikkel ütleb kattuvuse juba välja jaotistes 3.8 ja 6.3. RQ2 sihtpopulatsioon on kogu tuvastatud korpus, mitte eraldi ülekandekatse. Seetõttu pole nende 61 projekti kaasamine iseenesest viga. Pelgalt olemasolevate tabelite ümberkoondamine 541 projektile ei oleks küll uus detektorikatse, kuid kõigi katvuste, detsiilide ja fragmendiosakaalude uuesti esitamine muudaks analüüsi mahtu märgatavalt. Seda pole vaja, kui vastupidavust sellele eraldusele ei väideta.

**Paigutus:** jaotises 4.3 lk 19 esimese lõigu lõppu.

> This corpus includes the 61 annotated repositories and is not an independent transfer set. Tables 8–10 describe the complete identified population; stability of these distributions in the 541 repositories outside the annotation sample has not been established separately.

**Miks hea:** annab otsese vastuse sellele, mida olemasolevad koondtulemused lubavad öelda. „541 täiesti nägemata projekti” oleks liiga tugev ka seetõttu, et kaevandamise ja korpuse ettevalmistamise käigus oli nende struktuur nähtav.

### 29 Few Shot 352 sekundit ja Zero Shot 367 sekundit

**Otsus: uut eraldi parandust selle näilise vastuolu tõttu mitte teha.**

Lause „the shortest runtime among the Zero-Shot configurations” on õige: Few-Shot ei kuulu Zero-Shot konfiguratsioonide hulka. 15-sekundiline erinevus ühe käivituse põhjal ei tõenda kindlat viibapikkuse mõju ega teadaolevat võrguviivitust. Võrgu või API kõikumist ei tohi nimetada mõõdetud põhjuseks.

Punkti 20 üldine selgitus, et ajad on konfiguratsiooni ja täitmistingimuste ühisvaatlused, on piisav. Eraldi põhjenduse lisamine muudaks väikese korrektse tulemuse tarbetult problemaatiliseks.

### 30 Vahemiku kriips

**Otsus: võtta arvesse väikese tüpograafilise ühtlustusena.**

**Paigutus:** jaotise 4.2.1 lk 18 lauses „within the 0.863-0.873 range” kasutada vahemikku **0.863–0.873**. LaTeX-lähtefailis tavaliselt `0.863--0.873`, kui olemasolev arvuvorminduspakett ei anna teist kokkulepet.

**Miks hea:** parandab ühtlust, sisulist mõju pole. PDF-ist eraldatud teksti kriips üksi ei tõesta alati lähtekoodi viga; kontrollida tuleb ka lähtefaili.

### 31 Tabeli 10 ümardamine

**Otsus: võtta arvesse allkirja täpsustusena.**

**Paigutus:** tabeli 10 lk 21 allkirja lõppu.

> Percentages and combined shares are calculated from the underlying counts before rounding. Displayed percentages may therefore sum to 99.9% or differ from sums of rounded category shares.

**Miks hea:** 9,1% + 3,8% ja ühendatud 13,0% ei ole vastuolu. Õigeid arve ei tohi näilise liituvuse saavutamiseks muuta.

## Arutelu ja valiidsus

### 32 Kolm andmetöötluse kõrvalekallet

**Otsus: võtta arvesse kõrge prioriteediga.** Üldine kirjeldus jaotises 6.2 ei asenda arvulist kooskõlastust.

#### 32a Liiga laia filtriga vahele jäetud testtabel

Olemasolevas testandmestikus on projekti jOOQ/jOOQ-mcve faili `jOOQ-mcve-java-mysql/src/main/java/org/jooq/mcve/java/mysql/tables/Test.java` real 55 üks ID Required viide. Avaldatud filter välistab teefragmendi `mysql/tables`, kuigi siin on tegu rakenduse tabeliga. 536 ennustuse hulgas sellele failile ennustust pole; viide on 523 testviite hulgas ja jääb seega üheks FN-iks. [S3, S13]

**Paigutus:** jaotises 6.2 lk 24 asendada „An over-broad file-exclusion rule also skips…” lause.

> The mysql/tables path exclusion also removed the application table jOOQ-mcve-java-mysql/…/mysql/tables/Test.java from the jOOQ/jOOQ-mcve test repository. Its single ID Required reference at line 55 remains among the 523 test spans and contributes one false negative. The primary end-to-end evaluation retains this selection failure. Excluding this reference only would yield 460 TP, 76 FP and 62 FN, with micro F1 = 0.870 instead of 0.869.

Viimane arv on olemasolevate koondite aritmeetiline tundlikkus, mitte uuesti käivitatud detektori tulemus. See ei näita, kas detektor oleks faili kaasamisel juhtumi leidnud. 502 faili tuleb nimetada filtriga valitud failide arvuks; 523 viidet ei pärine tingimata ainult neist failidest.

**Täiendav tähelepanek:** viidatud CSV ja korpuse manifesti võrdlus näitas ka `NotificationsTable.java` teelahknevust: testviites on moodul `game-overgo-service`, ennustuses ja manifestis `game-miner-service`. Seda ei tohi pidada teiseks tõendatud filtriveaks. See on konkreetne võrdlusandmete failitee kontrollimise koht enne tabeli 6 üksikasjalikumat põhjendamist. Esmane tulemus peab jätkuvalt kajastama algset võrdlusandmestikku.

#### 32b Kas kõik 15 931 leidu kuuluvad nimetaja failiraami

Avaldatud esimese faasi kontrollkirje kinnitab, et kõik leiud lahenduvad lubatud lähtefailidesse ning kuuluvad 17 988 faili raami. Seega pole retsensiooni oletatud lugeja-nimetaja lahknevus selle avaldatud rekonstruktsiooni põhjal kinnitatud. [S14]

**Paigutus:** jaotises 3.8 lk 15 pärast allikaraami esimest lõiku.

> Source-frame reconciliation verified that all 15931 retained flags resolve to files within the reconstructed 17988-file frame. Correcting the file frame did not retain flag numerators from files outside that denominator.

**Miks hea:** annab otsese auditeeritava vastuse ilma uut mudelikatset tegemata. Seda ei tohi segada punktis 11 käsitletud päringute edukuse küsimusega.

#### 32c Hiljem eemaldatud duplikaatprojekt

603- ja 602-projektilise loendi erinevus on `Davincii254/Stroom`. Seda nime ei ole treeningu, valideerimise ega testi märgendatud projektide hulgas. Kõik 61 valimiprojekti sisaldasid märgendeid, seega ei olnud eemaldatud nimi selles valimis. See kontroll ei tõesta, et ühegi muu nime all pole jagatud koodi või kloone. [S15]

**Paigutus:** jaotises 3.2 lk 9 pärast lauset „A further duplicate found before corpus execution…”.

> The late removal was Davincii254/Stroom, which was not part of the 61-repository annotated sample and did not belong to any of its three partitions. This removal changed the corpus frame without changing the annotated project split.

**Miks hea:** kõrvaldab konkreetse võimaliku jaotuste kattuvuse kahtluse, väitmata üldist kloonivabadust. Uut kihijaotuse tabelit pole vaja, sest eemaldatud projekt ei muutnud 61 projekti valimit.

### 33 Väiksema täpsusega klasside korpuseleiud

**Otsus: võtta arvesse, kuid mitte kanda testtäpsust korpusele üle.**

Keyless Entry ja Fear of the Unknown madalam kooskõla väärib RQ2 arutelus meeldetuletust. Samas 23 Fear of the Unknown näilist FP-d olid võrdlusandmete puudujäägid. Seetõttu oleks vale öelda, et 55,8% selle klassi korpuseleidudest on valepositiivsed, või korrigeerida korpusearve testtäpsusega.

**Paigutus:** jaotise 5.2 lk 22 lõppu.

> Keyless Entry and Fear of the Unknown coverage should also be read alongside their lower original-reference precision, 0.538 and 0.442. Keyless Entry disagreements included audit-log relationships, while most apparent Fear of the Unknown false positives exposed missing reference annotations. These mechanisms make corpus counts particularly dependent on operational boundaries and review context; the test precision values are not estimates of the fraction of valid corpus flags.

**Miks hea:** seob RQ1 ja RQ2 konkreetsete veamehhanismidega, ilma tulemustele valideerimata veakorrektsiooni rakendamata.

### 34 Minevikuvorm skipped

**Otsus: võtta arvesse.**

Kui punktis 32a pakutud asendust ei tehta, muuta jaotises 6.2 lk 24 **„also skips” → „also skipped”**. Punkti 32a asendustekst lahendab küsimuse juba.

**Miks hea:** joondab ajavormi ülejäänud käivituskirjeldusega. Mõlemat parandust pole vaja eraldi rakendada.

## Replikatsioonimaterjalid ja viited

### 35 Väidetavalt puuduvad repositooriumilingid ja DOI

**Otsus: võtta osaliselt arvesse; linkide täieliku puudumise väide tagasi lükata.** See katab nii üldnõrkuse kui ka lk 27 korduva etteheite.

PDF-i lk 27 kuus lingiannotatsiooni viivad andmete, analüüsi, detektori ja README GitHubi asukohtadesse. Nähtav tekst on siiski peamiselt commit’i lühitähis. Peale selle kuvab esimene andmeviide `d9b35e3`, kuid sihtaadress lõpeb versiooniga `9913a7670fce52b135651f95ff18cd505c61b142`. See tuleb üheseks teha. DOI oleks arhiveerimiseks kasulik, kuid selle puudumine ei tee olemasolevaid GitHubi materjale olematuks. DOI-d ei tohi välja mõelda ega avaldamist selle ülesande raames algatada.

**Paigutus:** lk 27 „Data availability” ja „Code and materials availability” asemele lühike ühtne kirjeldus, säilitades ajakirja nõutud alapealkirjad.

> Study data, annotation rules and experimental materials are available in the masters-thesis repository at https://github.com/kristoisberg/masters-thesis/tree/d9b35e398a6deb544f913bdbc0b211ab38474a44. Article-analysis scripts and tables are available at https://github.com/kristoisberg/thesis-paper/tree/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis. The released detector is available at https://github.com/kristoisberg/jooq-antipattern-detector/tree/cf82fe56acb728f076df67279ff4a78a138996f3. The replication guide is https://github.com/kristoisberg/thesis-paper/blob/4a3b4d55073adbb38325ca43872852d2a75649c9/analysis/README.md. The guide distinguishes preserved analysis inputs from limitations on replaying the original hosted-model executions.

Lõplikus küljenduses vormistada aadressid URL-käskudega või loetavate „repository + revision” viidetena. Ülal kasutatakse artiklis nimetatud külmutatud `d9b35e3` versiooni, mille materjalid on kontrollitavad. Kui autor soovib uuemat `9913a76` versiooni, tuleb korraga muuta nähtavat tähist ja selgitada versioonivahetust.

**Miks hea:** materjalid on leitavad ka prindist ja PDF-ist eraldatud tekstist, ning viite tähis vastab sihtobjektile. Avaldatud juhend tuleb kooskõlastada artikli käivitusprovenientsi väidetega, vt punktid 17 ja 21.

### 36 Magistritöö täielik bibliograafiline kirje

**Otsus: võtta arvesse.** Tööd kasutatakse meetodite lisaselgitusena, mistõttu pelgalt pealkirjast deklaratsioonis ei piisa.

**Paigutus:** lk 28–30 kirjandusse lisada ning jaotises 3.3 lk 10 „the original thesis’s dataset-creation chapter” järel viidata kirjele.

> Isberg K (2026) Detecting SQL Antipatterns in jOOQ Database Access Code Using Large Language Models. Master’s thesis, Tallinn University of Technology. https://digikogu.taltech.ee/en/Item/37cea9cf-3d0f-4aef-935c-ecdab7db0dcd

**Paigutus:** lk 26 deklaratsiooni esimene lause muuta kujule:

> This article is based on Kristo Isberg’s master’s thesis at Tallinn University of Technology (Isberg 2026).

**Miks hea:** autor, aasta, asutus ja konkreetne digikogu püsiva üksuse aadress on kontrollitud. Digikogu kirje kinnitab 25.05.2026 kaitsmist. [S16]

### 37 OpenAI 2025 kirjete eristamine

**Otsus: võtta arvesse.**

**Paigutus:** lk 30 kahe 2025. aasta kirje eristamine ja lk 13 ning 16 tekstiviidete vastav muutmine. Praeguses järjestuses sobiks:

- **OpenAI 2025a** – gpt-oss-120b & gpt-oss-20b model card.
- **OpenAI 2025b** – Update to GPT-5 system card: GPT-5.2.

Seega GPT-5.2 järel „OpenAI 2025b”, gpt-oss-120B järel „OpenAI 2025a”. Bibliograafia tööriista genereeritud lõplik tähtede järjekord on ülimuslik, kui kõik tekstiviited vastavad õigetele kirjetele.

**Miks hea:** sama autor-aasta enam kahele allikale ei osuta. Uusi allikaid ega mudelite kohta uusi väiteid pole vaja.

### 38 Factor 2014 vaatamiskuupäev

**Otsus: automaatset aastaarvu muutmist mitte võtta arvesse.**

Tagasiside järeldus „näib olevat 2025 trükiviga” ei tulene esitatud andmetest. Artikkel sisaldab pärast katseid koostatud analüüse ning november 2026 on hilisem kui 28.08.2026. Allika vaatamine augustis on võimalik ka aprillis tehtud katsete puhul. Vaatamiskuupäev ei ole katsekuupäev.

**Parandus:** puudub, kui algne kirje kajastab tegelikku vaatamisaega. Muuta ainult autori brauseri-, viitehalduri- või tööversiooni kirje alusel, mitte teiste allikate kuupäevadega ühtlustamiseks.

**Miks nii:** väldib õige bibliograafilise info asendamist oletusega. Artikli sisulised väited sellest ei sõltu.

## Automaatse viitekontrolli kolm märkust

### 39 Gradle build tool on märgitud väljamõeldud publikatsiooniks

**Otsus: mitte võtta arvesse.**

Kirje lk 29 on URL-iga tarkvaraveebi viide, mitte teadusartikli väide. [Gradle ametlik veeb](https://gradle.org/) on olemas ja sobib selgitama manifesti/build-süsteemi nimetust. Seetõttu ei tõenda teadusartikli puudumine viite väljamõeldust.

Artiklit pole selle märkuse tõttu vaja muuta. Soovi korral võib viite tüübiks bibliograafias märkida „software website”, kuid see on vormistusvalik, mitte vea parandus.

### 40 jOOQ SQL building on märgitud väljamõeldud publikatsiooniks

**Otsus: mitte võtta arvesse.**

Lk 29 viide osutab [jOOQ ametliku käsiraamatu SQL building jaotisele](https://www.jooq.org/doc/latest/manual/sql-building/). Tarkvaradokumentatsioon on esmane allikas API toimimise kirjeldamiseks; sellelt ei pea nõudma eraldi ajakirjaartikli staatust.

Artiklit pole selle märkuse tõttu vaja muuta. Versioonitud dokumentatsiooniviide oleks korratavuse seisukohalt parem kui „latest”, kui kasutatud versioon on dokumenteeritud, kuid ajaloolist versiooni ei tohi arvata praeguse veebilehe põhjal.

### 41 OpenRouter on märgitud väljamõeldud publikatsiooniks

**Otsus: mitte võtta arvesse.**

Lk 30 viide nimetab kasutatud [OpenRouteri teenust](https://openrouter.ai/), mitte olematut teadusartiklit. Tarkvara- ja teenuseviited on kasutatud infrastruktuuri kirjeldamisel asjakohased.

Artiklit pole selle märkuse tõttu vaja muuta. Kõigi kolme automaatkontrolli probleemi ühine põhjus on allikatüübi vale eeldus; neid ei saa lugeda tõendiks, et artikli kolm viidet on hallutsineeritud.

## Soovitatav paranduste järjekord

| Järjekord | Tegevus | Punktid |
|---|---|---|
| 1 | Kooskõlastada ajalooliste käivituste, valideerimistabeli ja README päritolu ning nähtavad versiooniviited | 17, 21, 35 |
| 2 | Piiritleda mõisted ja testandmete sõltumatuse tähendus | 1–3, 12 |
| 3 | Lisada täpne jaotusfunktsioon, sobitamise ja kaalumise reeglid ning andmetöötluse kõrvalekallete arvestus | 7, 9–10, 14–16, 32 |
| 4 | Piirata võrdlevaid ja üldistavaid järeldusi | 4, 8, 11, 20, 22, 24, 28, 33 |
| 5 | Avaldada juba olemasolevad kasulikud detailid | 13, 23, 26 |
| 6 | Täiendada seotud töid ja parandada viited ning vormistus | 5–6, 18–19, 30–31, 34, 36–37 |

Praeguses parandusringis ei ole vaja uut baasmeetodit, uut valimit või jaotust, kordusmärgendamist, võrdsustatud mudelikatseid, uusi API-käivitusi ega 541 projekti eraldi tulemuste kogumit. Kõige olulisem lahtine küsimus on olemasolevate käivitus- ja valideerimisandmete dokumentaalne kooskõla: selle puudumisel tuleb piirang avaldada, mitte asendada seda tugevama kindlusega.

## Kontrollimiseks kasutatud avalikud allikad

Allikad on siin versioonitud, kui artikli materjalide puhul on vastav versioon teada. Need lingid toetavad ülal nimetatud arhiivikontrolle; need ei asenda analüüsitava PDF-i leheküljeviiteid.

- **S1** [Poor Man’s Search Engine otsustuspuu](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/diagrams/decision/poor-mans-search-engine.puml) ja [Zero-Shot päringuviip](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/zero-shot/dml-dql.md).
- **S2** [Fear of the Unknown otsustuspuu](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/diagrams/decision/fear-of-the-unknown.puml) ja [skeemiviip](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/prompts/zero-shot/ddl.md).
- **S3** [Avaldatud failivaliku ja Keys-konteksti teostus](https://github.com/kristoisberg/jooq-antipattern-detector/blob/cf82fe56acb728f076df67279ff4a78a138996f3/src/file-discovery.ts).
- **S4** [Chen jt autoriversioon](https://petertsehsun.github.io/papers/peter_tse2016.pdf), eriti meetodi ülevaade ja staatilise ning dünaamilise analüüsi roll.
- **S5** [Silva jt ESEM 2024 väljaandja kirje](https://doi.org/10.1145/3674805.3690742) ja [autoriversioon](https://homepages.dcc.ufmg.br/~mtov/pub/2024-esem-code-smells-llm.pdf).
- **S6** [Projektide jaotamise märkmik](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/07-split-ground-truth-into-sets.ipynb).
- **S7** [Sobitamise ja bootstrap-analüüsi programm](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/localisation_robustness.py).
- **S8** [PDF-is viidatud replikatsioonijuhendi versioon](https://github.com/kristoisberg/thesis-paper/blob/4a3b4d55073adbb38325ca43872852d2a75649c9/analysis/README.md). Erilist tähelepanu vajavad „Original model executions” ja säilinud valideerimistulemuste päritolu piirangud.
- **S9** [Algmärgendus](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/ground-truth.csv), [kordusmärgendus](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/reannotated-ground-truth.csv) ja [128 valitud faili](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/files-to-reannotate.csv).
- **S10** [Korpuse normaliseerimise programm](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_normalization.py) ja [identse sisu tundlikkusanalüüsi meetodikirjeldus](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase4_summary.json).
- **S11** [Kestuse koondamise märkmiku säilinud väljund](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/22-calculate-analysis-duration.ipynb).
- **S12** [Parandatud võrdlusandmestiku klassipõhiste koondite märkmik](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/15-calculate-tool-localisation-corrected.ipynb).
- **S13** [523 algset testviidet](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/test-set.csv), [536 säilinud ennustust](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/scripts/14-evaluate-tool-localisation.ipynb) ja [korpuse lähtefailide manifest](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_source_manifest.csv).
- **S14** [Failiraami kooskõlastuse kontrollkirje](https://github.com/kristoisberg/thesis-paper/blob/bb3bf6056cc7bbda29bb0fb5f0b720e7f9d06028/analysis/corpus_phase1_summary.json), eelkõige `all_flags_are_in_source_frame` ja `all_flags_resolve_to_allowlisted_source_files`.
- **S15** [Esialgne projektide loend](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/final-repositories.csv), [parandatud loend](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/final-repositories-corrected.csv), [treeningjaotus](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/training-set.csv) ja [valideerimisjaotus](https://github.com/kristoisberg/masters-thesis/blob/d9b35e398a6deb544f913bdbc0b211ab38474a44/datasets/validation-set.csv); testjaotus S13.
- **S16** [Isbergi magistritöö TalTechi digikogu kirje](https://digikogu.taltech.ee/en/Item/37cea9cf-3d0f-4aef-935c-ecdab7db0dcd).
- **S17** Artiklis nimetatud [testversiooni viibad](https://github.com/kristoisberg/jooq-antipattern-detector/blob/80f3ff4/src/prompts.ts), [korpuseversiooni viibad](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50a/src/prompts.ts), [korpuseversiooni viiba koostamine](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50a/src/prompt-builder.ts), [märgieelarve](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50a/src/model.ts), [testversiooni faililugemine](https://github.com/kristoisberg/jooq-antipattern-detector/blob/80f3ff4/src/file-discovery.ts) ja [korpuseversiooni faililugemine](https://github.com/kristoisberg/jooq-antipattern-detector/blob/245b50a/src/file-discovery.ts).
