# Applied-Bioinformatics
Labs and project archive for DD2404 Applied Bioinformatics.
## Lab contents:

## Project: Predicting signal peptides
This project deals with a machine learning approach to predicting signal peptides. As signal peptidesare at the N-terminal end of a sequence, 
we tested the effects of shortening the sequence to different lengths. 
Additionally, we compared the two approaches of using the unmodified sequence and of simplifying it to contain only types of amino acids instead of the actual
amino acids. By using a support vector machine (SVM) with one-hot encoded types of amino acids and a sequence length of 25, 
we were able to achieve an accuracy of 0.729 with an F1 score of 0.358.

## References
[Gavin E Crooks et al. WebLogo: a sequence logo generato](https://pubmed.ncbi.nlm.nih.gov/15173120/)

[Guy D.  Duffaud  et  al.  “Structure  and  Function  of  the  Signal  Peptide”](https://www.researchwithrutgers.com/en/publications/structure-and-function-of-the-signal-peptide)

[Vikramaditya Jakkula. “Tutorial on support vector machine (svm)”](https://course.ccs.neu.edu/cs5100f11/resources/jakkula.pdf)

[Rhoda J. Kinsella et al. “Ensembl BioMarts: a hub for data retrieval across taxonomic space”](https://pubmed.ncbi.nlm.nih.gov/21785142/)

[William  Stafford  Noble.  “A  Quick  Guide  to  Organizing  Computational  Biology  Projects”](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)

[Rabie Saidi, Mondher Maddouri, and Engelbert Mephu Nguifo. “Protein sequences classificationby means of feature extraction with substitution matrices"](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-175)
