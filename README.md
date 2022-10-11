# [Information Density of Old East Slavic](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic/)

This is a small Python program that:
1. contains a [corpus of 83 Old East Slavic texts](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#corpus-of-old-east-slavic-texts);
2. separates text into [syllables](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#syllable-separator);
3. calculates [Shannon entropy (ShE) and information density (ID)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#shannon-entropy-and-information-density).

***

# Corpus of Old East Slavic texts

This program contains a corpus of 83 Old East Slavic literary texts from the 11th to 13th centuries. All the texts were taken from the same source: [Library of Literature of Ancient Rus'](http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070) (the Institute of Russian Literature of the Russian Academy of Sciences, [Lihačev et al. (1997)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). This corpus contains texts from the first 5 volumes of the library (that is, up to and including the 13th century). The choice is limited to this time interval since the 14th century is usually considered as the end of the existence of Old East Slavic language as something relatively unified and as the beginning of its splitting into three closely related East Slavic languages. There are several advantages of choosing this (and only one) source:
- It is the most extensive collection of texts of Old East Slavic literature. Several copies of the same work are used (in case they are preserved and available). Flaws in the manuscript taken as the basis for the edition were corrected from other manuscript copies;
- All texts were written according on the same principles, which is important for comparing them;
- All texts have the same standardized orthography, which is crucial for automatic processing and syllable separation. For example, certain simplifications are permitted in the transmission of texts: all letters missing in the modern script are replaced  (except for the yat (Ѣ)).

***

# Syllable Separator

**Why syllables?**

Today many linguists use syllables as a basic metric for language analysis (see e.g. [Fenk-Oczlon & Fenk (2005)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references), [Bane (2008)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references), [Pellegrino et al. (2011)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references), [Oh (2015)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references), etc., but [Port & Leary (2005)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) for a criticism). Usually the first step in analyzing language data is to determine some size (chunk) to be used as a "unit of speech" to calculate something (e.g. speech rate, amount of information, complexity, etc.). Sentences or phrases are often too ambiguous to be separated and establish clear boundaries (especially in spoken language). Certainly *words* are one of the most logical and popular units in language segmentation, which is also used in studies with information measures (e.g. [Montemurro & Zanette (2010) & (2011)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). However, there are some problems in using word-level segments that are especially relevant for languages with rich morphology (which are most of the Slavic languages). First of all, it is necessary to lemmatize the words to calculate their probabilities. Obviously, as far as we know, there is no lemmatizer for Old East Slavic language yet (honestly, the advisability of creating such a program is also questionable since the number of known texts is strictly limited and creating new ones is no longer possible). The second reason for using syllables is to allow cross-linguistic comparison. For example, no syllabification is required for Sino-Tibetan languages since each ideogram corresponds to a single syllable ([Coupé et al., 2019, p. 7](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). Furthermore, while word-level text analysis can provide insight primarily into lexical diversity, syllable-level analysis can reflect morphological complexity because syllables often correlate with morphemes. [Pellegrino et al. (2011, p. 545)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)) claim that "in addition to the methodological advantage of the syllable for counting, numerous studies have suggested its role either as a cognitive unit or as a unit of organization in speech production or perception (e.g. Schiller (2008), Segui & Ferrand (2002); but see Ohala (2008)". Thus, it is demonstrated that the use of syllables reflects not only morphological but also semantic information of texts. [Coupé et al. (2019, p. 2)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) later confirm this by comparing the ID (which uses syllables) and the syntagmatic density of information ratio (SDIR), which is based on the semantic information. They obtain a very high correlation between ID and SDIR, which suggests that their ID is a "good estimate of the average amount of information per syllable" ([ebd.](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)).

**How to break words into syllables?**

Syllabification is a huge topic in itself. In Russian, as in many other languages, there are several approaches and no single universally accepted standard. As an example, you can consider the word *"hokkej"* (hockey), which, depending on school, can be separated as *"hok|kej"* (traditional school) or as *"ho|kkej"* (according to the sonority scale: voiceless obstruents, voiced obstruents, sonorants, vowels). [Coupé et al. (2019)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) in their study rely on the thesis of [Oh (2015)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references), who in his turn breaks words into syllables, classifying them into three groups according to WALS ([Dryer & Haspelmath, 2013](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). There is, of course, no Old East Slavic in WALS, but Russian, according to it, belongs to the group of languages with a complex syllable structure. Thus, the maximal syllable structure of Russian is represented as (C)(C)(C)V(C)(C)(C)(C), which matches traditional school. It is also important to note that *syllabification* does not always equal *hyphenation*. However, in the traditional school of syllabification, these concepts stand as close as possible (which is why there is no problem with finding a ready-made syllabizer). Creating a syllabizer based on ascending sonorities may be a subject for further research.

As a syllabizer for this skipit was chosen **russylab** - simple [Python package for breaking Russian words into syllables created by Ilja Koziev](https://github.com/Koziev/rusyllab) and distributed under a free, copyleft license. The original code was adapted for the old east slavic orthography. The soft sign ("ь"), which does not represent an individual sound but indicates palatalization of the preceding consonant, was moved to the vowels because in Old East slavic / Old Church Slavonic it represented a short (or "reduced") front vowel.

# Shannon Entropy and Information density

[Coupé et al. (2019)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) argue that information per syllable represents language-specific structural properties (for more details about The Uniform Information Density hypothesis see e.g [Jaeger (2010)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). They use the following measures to calculate the amount of information transmitted per syllable.

**Shannon Entropy (ShE)**

The first measure is the classical Shannon entropy of the first order, used by many linguists. The formula for the standard Shannon entropy (ShE) is:

<img src="https://imgur.com/rgRmEmM.png" width="35%" height="35%">

where p(x) is the maximum likelihood estimates of the syllable unigram probabilities observed in the corpus ([Coupé et al., 2019, p. 7](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). 

**Information Density (ID)**

However, ShE reflects only syllable frequencies regardless of context. For this reason ID (second-order entropy) was introduced. Coupé et al. characterized this context as "the identity of the previous syllable or a null marker for syllables occurring word initially (thus, no bigrams span across word boundaries)

<img src="https://imgur.com/lvG0cPs.png" width="35%" height="35%">

where p(x, y) is the maximum likelihood estimates of the syllable bigram probabilities observed in the corpus" ([ebd.](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)).

Both formulas were used in this script, which calculates ShE and ID both in each text separately and in general for the entire corpus.

***

# Running Requirements

- Python 3.9

***

# Files
## - Corpus (folder)
The corpus contains 83 Old East Slavic texts from the [Library of Literature of Ancient Rus'](http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070) [(Lihačev et al., 1997)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references). All texts are presented in their original form and are not edited. So they contain references to comments (e.g. "[1]", but the comments themselves are not included); quotation marks indicating the removal of certain fragments (e.g. "<...>") and other elements that do not relate to the raw text itself. Also all headings are in uppercase letters. Text processing that removes/corrects the mentioned problems occurs in the script itself.

## - LICENSE
Open Source License.

## - README.md
This file.

## - TABLE.pdf
The table of contents for the corpus with Old East Slavic texts. The table contains:
1. Text sequence number
2. Filename
3. Original text title (in Russian)
4. English text title

## - orvid.py
The main script, which processes the text(s), breaks tokens into syllables, counts them and the total ShE and the total ID. The script can easily be modified to get any other necessary data of the processed corpus. Results at the request of the user can be either displayed in the console or saved locally.

**Why "orvid"?** "orv" is the language code of Old East Slavic, "id" is abbreviation of "Information Density".

- **Usage**: `python orvid.py`

- **Input**: For the calculations you need:

(0). To select your text/corpus. The script uses this corpus (link) by default. But if you want to use the script for other text(s), don't forget to change the name of the textfile/folder (the variable `text`, line 664).

1. To select the form output: just to the console or to save as separate txt-file (result.txt). While starting the script, the user is asked for this task: `Do you want save the results? (y/n)`. If you enter "y" into the console, the output will be saved. If you enter "n" (or something else), the results will be displayed in the console.

- **Output**: The output has several columns:
   - Filename - the name of each analyzed file (text)
   - length (syl) - the length of this file in syllables
   - ShE - the Shannon Entropy of this file
   - ID	- the Information Density of this file
   - average ID - the Average ID (ID/length) of this file  

  In addition to the results for each text separately, the results for the entire corpus are calculated at the end:
   - Corpus ShE
   - Corpus ID
   - Corpus average ID

## - results.txt
Output saved in text format (created after user confirmation).

***

# Results & Diskussion
Clearly, the size of the text influences the entropy value. For example, Montemurro & Zanette ([2010, p.8](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)) point out that "the scales at which the informationis maximal, roughly between 1000 and 3000 words in length". That is why it is always worth considering the length of the text and paying special attention to those texts that fall out of the "standard" series. Let's look at a few examples.

Let's try to sort the texts by Shannon entropy (starting with the highest). As mentioned above, the biggest writings have the biggest scores. However, a couple of texts are relatively short in length, but high in ShE.

<img src="https://imgur.com/rOQMRUF.png" width="65%" height="65%">

The first highlighted text is **The Epistle of Kliment Smoliatich**. In the introduction to this text in the [Library of Literature of Ancient Rus'](http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070) is said that "Chronicles have preserved the description of Kliment Smolyatich as a scribe and philosopher, which has never been in the Russian land before" ([Lihačev et al., 1997, vol. 4, p. 600](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). Uspenskij ([2017, p. 172](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)) also calls Kliment "undoubtedly one of the most interesting and controversial figures of pre-Mongol Rus'". This text is a treatise in defense of the allegorical way of understanding the Scriptures and an example of literal-theological polemics ([Lihačev et al., 1997, vol. 4, p. 600](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). This epistle was addressed to the priest Foma, who, as can be seen from the context of the epistle, reproached Kliment Smoliatich for being conceited in his knowledge and in his philosophical boasting. And, apparently, this was not unreasonable, given such a high informativity of such a small text.

The second highlighted text is **The Teaching of Vladimir Monomakh**. Vladimir is called as "one of the most talented and educated Russian knyazes of the pre-Mongolian period"([Lihačev et al., 1997, vol. 1, p. 538](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). "The Teaching is one of the most outstanding works of ancient Russian literature" ([ebd, p. 539](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). The Teaching of Vladimir Monomakh is quite difficult to define to a certain genre. So, Alekseev draws genre parallels between The Teaching of Vladimir Monomakh and royal wills to the children-heirs, as well as with royal teachings ([Alekseev, 1935](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). As we can see, the *Teaching* really succeeded, as this text is very informative and it can really be considered as an unique work.

Among the texts with the lowest informativity **The Russkaya Pravda (Extensive edition)** stands out. The Russkaya Pravda was the legal code of Rus'. Thus, this work is one of the few *documents* represented in this corpus. As it should be in documents, the language in the Russian Pravda is not too artistic and the vocabulary is pretty limited (the laws usually list the offender, the crime, and the punishment). At the same time, researchers note that the Extensive edition is written "in beautiful Old East Slavic literary language without any dialecticisms" ([Lihačev et al., 1997, vol. 4, p. 675](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). This code was so well completed that it was used as a source of civil law until the end of the 15th century.

<img src="https://imgur.com/3qqelJx.png" width="65%" height="65%">

The *simplicity* of the language and the very high stability of the syllable combinations are also confirmed by the low total ID (at the level of shorter works):

<img src="https://imgur.com/LiVAYvw.png" width="65%" height="65%">

Analyzing the average ID per syllable (the shortest texts with less than a thousand syllables are, of course, at the top of the list) we see one untypically long text: **The Izbornik of Sviatoslav (1073)**. The Izbornik is a collection of articles (more than 380 articles by 25 authors). "The fields of study covered by the Izbornik of 1073 are impressively wide: along with dogmatic theology and questions of Christian morality, there are anthropology, philosophy, mathematics, philology, natural sciences, history, etc."([Lihačev et al., 1997, vol. 2, p. 520](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)). Precisely because of its variety of topics and authors, such a long text has an atypically high information density.

<img src="https://imgur.com/k2rRczd.png" width="65%" height="65%">

Obviously, the longest texts should be on the other side of the average information density rating. And this is actually the case. However, there is one exception: **Birch bark manuscripts**. These are usually private letters written on pieces of the inner layer of birch bark. They are about a variety of daily life activities: family, household, routine, commercial, money, judgment, etc. The authors and the addressees of birch bark letters are not only priests, monks and other scribes of the time; among them are many ordinary people: landlords, tradesmen, keysmen, artisans, warriors and even women. Although here we see short letters from completely different authors, the average ID is still very low, which can more or less objectively indicate that the language of the ordinary people was *"simpler"* compared to the language of literary works.

<img src="https://imgur.com/yeh5T28.png" width="65%" height="65%">

The total resuslts of the corpus represent the following values:

>  **Corpus ShE:** 6.521871617192656  
>  **Corpus ID:** 69638.71223146988   
>  **Corpus average ID:** 0.07023755764797653  

The data obtained represent one more metric for possible comparisons of texts, especially speaking of them in such categories as "complexity" or "uniqueness". The script also collects all possible types of syllables and counts their number to get total values (corpus ShE/ID/avg ID). Thus, if necessary, it is possible to modify the script to solve other problems related to the concept of "text uniqueness" (for example, comparing uni/bigrams of some text with the rest of the corpus, etc.). Furthermore, it would also be interesting to measure ShE and ID without using a null marker at the beginning of each word, which would allow us to consider the across-word context ([Coupé et al. (2019, p. 7)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) rejected the idea because some of their text corpora only provided word frequencies and not raw texts). Another interesting topic for future research is dealing with different text sizes. It would be entertaining to correlate ShE, ID, and text lenghts. In the context of this question it is possible to divide the texts into separate sections of equal length (such an approach was taken in [Montemurro & Zanette's (2011)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references) study).

It is important to note that to fully understand the informativity of the (literary) Old East Slavic language and to compare it with other languages (e.g., those presented in [Coupé et al. (2019)](https://github.com/GeorgStin/Information-Density-of-Old-East-Slavic#references)) it is necessary to move from the orthographic to the phonological level, which means splitting the *transcribed* texts into syllables. However, transcribing the language of the 10th-15th century is another big separate task that requires a lot of work.

***

# References
-	[Alekseev, M. P. (1935)](http://lib2.pushkinskijdom.ru/Media/Default/PDF/TODRL/02_tom/Alekseev/Alekseev.pdf). Anglo-saksonskaja parallel' k «Poucheniju» Vladimira Monomaha. In A. S. Orlov (Ed.), *Trudy otdela drevnerusskoj literatury* (T. 2., pp. 39–80). Moscow: Izdatel’stvo Akademii nauk SSSR. 
-	[Bane, M. (2008)](http://clml.uchicago.edu/pdfs/2008_bane.pdf). Quantifying and measuring morphological complexity. *Proc. of the 26th West Coast Conference on Formal Linguistics*, 69-76.
-	[Coupé, C., Oh, Y. M., Dediu, D., & Pellegrino, F. (2019)](https://www.science.org/doi/10.1126/sciadv.aaw2594). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. *Sci. Adv. 5:eaaw2594*.
-	[Dryer, M. S., & Haspelmath, M. (2013)](https://wals.info). *The World Atlas of Language Structures Online*. Leipzig: Max Planck Institute for Evolutionary Anthropology.
-	[Fenk-Oczlon, G., & Fenk, A. (2005)](http://wwwu.uni-klu.ac.at/gfenk/Fenk_Willi_05%20pdf.pdf). Crosslinguistic correlations between size of syllables, number of cases, and adposition order. In G. Fenk-Oczlon, & C. Winkler, (Eds.) *Sprache und Natürlichkeit, Gedenkband für Willi Mayerthaler*, Tübingen: Gunther Narr.
-	[Jaeger, T. F. (2010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2896231/pdf/nihms185965.pdf). Redundancy and reduction: Speakers manage syntactic information density. *Cogn Psychol. 2010 August; 61*(1). 23–62. doi: 10.1016/j.cogpsych.2010.02.002
-	[Lihačev, D. S, Dmitriev, L. A, Alekseev, A. A, & Ponyrko N. V. (1997)](http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070). *Biblioteka literatury Drevnej Rusi*. St. Petersburg: Nauka.
-	[Montemurro, M. A., & Zanette, D. (2010)](https://arxiv.org/pdf/0907.1558.pdf). Towards the quantification of the semantic information encoded in written language. *Advances in Complex Systems, 13*(02). 135–153.
-	[Montemurro, M. A., & Zanette, D. H. (2011)](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0019875&type=printable) Universal Entropy of Word Ordering Across Linguistic Families. *PLoS ONE 6*(5). e19875. doi:10.1371/journal.pone.0019875
-	[Oh, Y. M. (2015)](http://www.ddl.cnrs.fr/fulltext/Yoonmi/Oh_2015_1.pdf). *Linguistic Complexity and Information: Quantitative Approaches* [Doctoral dissertation, University of Lyon].
-	[Pellegrino, F., Coupé, C., & Marsico, E. (2011)](https://www.jstor.org/stable/23011654). A cross-language perspective on speech information rate. *Language, 87*(3), 539–558.
-	[Uspenskij, B. A. (2017)](http://slovene.ru/2017_1_Uspenskij.pdf). Metropolitan Kliment Smoliatich and His Epistles. *Slovene. International Journal of Slavic Studies. 6*(1). 171–218.
