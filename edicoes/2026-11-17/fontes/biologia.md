# New tool tracks unintended CRISPR edits and their effects in individual cells

- Editoria: Biologia (`biologia`)
- Fonte: Phys.org — https://phys.org/news/2026-11-tool-tracks-unintended-crispr-effects.html
- Autor: Salk Institute
- Publicado: 2026-11-16T10:00:01+00:00
- Score: 5.697
- Imagem: imagens/biologia-new-tool-tracks-unintended-crispr-edits.jpg | crédito: Phys.org | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

New tool tracks unintended CRISPR edits and their effects in individual cells
A new era of genome research began in 2012 with the discovery that CRISPR/Cas9 could function as molecular scissors to cut specific DNA sequences. Over time, scientists harnessed CRISPR as a genome-editing tool, which held the promise of precise gene removal and addition for research purposes, targeted therapies for genetic diseases like cystic fibrosis or Huntington's, and a future where personalized treatments are the norm. But a major shortcoming has snagged that progress: CRISPR can make off-target edits to parts of the genome never meant to be touched.
Salk scientists have designed Superb-seq as a solution. Superb-seq is a method that reads out all the edits—both on- and off-target—and changes to gene activity made by CRISPR, at single-cell resolution. This new tool allows researchers to identify unwanted edits and how those edits change the cell's molecular landscape, making it easier to study gene regulation in the lab and evaluate the safety of gene-editing therapies.
The study was published in Nature Methods on Nov. 16, 2026.
Wait… CRISPR has room for improvement?
Genetics as a field has come a long way over a century of discovery—from discovering that the blueprint for life is written in a four-letter code, to revealing the double-helical structure of that code, to understanding the genetic basis for human diseases and editing the genome with CRISPR.
The field also has deep roots at Salk; Francis Crick, Ph.D., co-discoverer of DNA's double-helical structure, for which he earned a Nobel Prize, served as a research professor and president of the institute. Today, Graham McVicker, Ph.D., is working on a new question: How can we make genome editing more precise for scientists and safer for patients?
"What really inspired Superb-seq was a frustration with the existing state of affairs," says McVicker, senior author of the study and an associate professor at Salk. "We knew there were problems with CRISPR making unwanted edits, but also there was no good way to see what those edits were and how they affected the cell—what we wanted to see was invisible using current technologies."
How does CRISPR genome editing work?
The clustered regularly interspaced short palindromic repeats (CRISPR) method for genome editing emerged from an observation in bacteria: They could defend themselves against infection by cutting up the viral genetic material that causes the infection. Cas9 is the protein that performs this cut, and it targets the viral genome using a strand of RNA, known as a guide RNA, which is encoded by the CRISPR elements.
Scientists soon realized that they could create their own guide RNAs to direct cutting to any desired stretch of genetic code. This would allow scientists to remove a gene to study its function in the lab or replace a mutated gene to restore health in a therapeutic setting.
CRISPR has already been an incredible scientific tool, and in 2023 the first FDA-approved CRISPR-based therapy was developed to treat sickle cell disease and beta thalassemia. But despite its successes, the problem with off-target edits looms over the technology.
What is Superb-seq?
Current methods can show where unwanted edits are located, but don't reveal which individual cells carry those edits, nor how those edits impact cell behavior. Superb-seq does both.
"In some cases, off-target edits could disrupt key genes that protect against cancer or other unhealthy cellular states," says co-first author Brad Balderson, Ph.D., a postdoctoral researcher in McVicker's lab. "That is why it's essential to not only know what off-target edits are being made, but to know in what cells they occurred and whether they have any impact on activity that could result in disorder or disease. That ability to distinguish between likely benign versus important off-target edits is a key layer of information Superb-seq gives us."
Superb-seq integrates Cas9 editing, a short edit-reporting DNA sequence and single-cell RNA sequencing to capture single-cell edits and their impact on gene expression. After developing Superb-seq, the Salk team tested it on 34,000 cells from three different cell lines. In one group of 10,000 human leukemia cells grown in the lab, Superb-seq detected 43 edit sites—36 of which were off-target—and 5,761 edited cells.
"There are some people that have worked on this off-target issue before that have an awareness of how bad it is, but for many people that pick up CRISPR to use it in the lab, the extent of this problem will really come as a surprise," says McVicker. "I knew off-targets were an issue, but they were far more frequent than I was expecting."
Superb-seq detected gene expression changes caused by genome edits that are invisible to existing edit detection methods. It also improved interpretation of the effect of edits compared to a predecessor, Perturb-seq, which reads out gene expression and guide RNAs but not the resulting edits.
By connecting single-cell edits with changes in gene expression, Superb-seq reveals the effects of CRISPR genome editing with greater detail than ever before.
How could Superb-seq change what we see in the lab and clinic?
The Salk researchers foresee four primary applications for Superb-seq: basic research, drug development, personalized medicine and training machine learning models.
"There are tens of thousands of papers that use CRISPR to study different aspects of biology," says co-first author Michael Lorenzini, Ph.D., a staff scientist in McVicker's lab. "Superb-seq could reveal the extent to which off-target edits color all those findings. And beyond basic discovery settings, our tool could be immensely helpful in establishing the safety of genome therapy candidates early on in development. Superb-seq could be used to profile candidates and learn what their off-target edits are, as well as their effects."
McVicker notes that, since genomes differ from person to person, the most effective genome-editing therapies may vary as well. Genetic differences can create new off-target edits, and Superb-seq could reveal both the edits and their effects on an individual basis to determine the safest treatment option.
The team also envisions Superb-seq as a valuable data generator for training new machine learning models that predict how cells respond to perturbations. Recently, there has been an emphasis on generating more data to train these models. The Salk researchers emphasize that generating better data is just as important, and that the absence of single-cell edit outcomes in current training data limits what artificial intelligence models can learn. Superb-seq could help overcome this problem and improve the accuracy of artificial intelligence models of cellular function.
McVicker, Balderson and Lorenzini have filed a patent for Superb-seq, and look forward to exploring how the tool can be used across the discovery pipeline—from bench to bedside.
