# Decoding interactomes: Supercomputing predicts bacterial protein links from shared evolutionary patterns

- Editoria: Biologia (`biologia`)
- Fonte: Phys.org — https://phys.org/news/2026-11-decoding-interactomes-supercomputing-bacterial-protein.html
- Autor: Barcelona Supercomputing Center
- Publicado: 2026-11-19T17:20:01+00:00
- Score: 5.943
- Imagem: imagens/biologia-decoding-interactomes-supercomputing-pre.jpg | crédito: Phys.org | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Decoding interactomes: Supercomputing predicts bacterial protein links from shared evolutionary patterns
Predicting how proteins interact inside a cell is essential to understanding how organisms function and why they differ from one another, yet experimental hurdles and the computational cost of analyzing millions of protein pairs make it impossible to explore complete interaction networks, particularly in understudied bacteria and organisms.
Now, researchers at the Barcelona Supercomputing Center—Centro Nacional de Supercomputación (BSC-CNS) have developed ContextMirror2.0, a tool capable of identifying relationships between proteins by using the information that millions of years of evolution left behind in their amino acid sequences.
The study, published in the journal PLOS Computational Biology, reveals how the algorithm compares the evolution of thousands of proteins across different species and searches for pairs exhibiting related evolutionary patterns. Thus, if two proteins evolved together (coevolved) and display correlated changes in their sequences, researchers can deduce that they interact and likely share related functions.
By applying this system across the entire protein set of three bacterial species (Escherichia coli, Salmonella enterica and Staphylococcus aureus), the researchers validated the method by recovering previously known associations while also identifying interaction patterns specific to each of the three species.
"ContextMirror2.0 reliably predicts hundreds of protein interactions in E. coli and identifies which ones are species-specific, a distinction that generic AI methods do not make and that could help uncover new targeted therapeutic targets," explained Alfonso Valencia, study lead and director of the Life Sciences Department at BSC.
One of the key differences between this tool and other methods for predicting protein interactions is that it does not require training on examples of known interactions. This avoids the biases that can arise with artificial intelligence, which tends to be trained on heavily studied organisms or proteins.
As a result, it serves as an especially valuable complementary tool for analyzing poorly characterized species where little prior experimental evidence exists.
"If you are going to study a bacterium about which nothing is known, you can use this algorithm to get a broad picture of its interaction network, as it narrows millions of combinations down to a small set of candidate proteins with a high probability of interacting, streamlining experimental work in the lab," explained Miguel Fernández, BSC researcher and first author of the study.
Eighteen years later, the project marks the culmination of ContextMirror, a study published by Valencia in 2008 that laid the groundwork for the current methodology but could only be applied to small sets of proteins due to the limitations of the era, including scarce data in bacterial genomic databases and limited computational analysis capacity.
A 'step zero' for biology and health care
To tackle the roughly 9 million protein pairs in E. coli, the team turned to the supercomputing power of MareNostrum 4 and later MareNostrum 5, selecting the 1,000 highest-scoring pairs identified by the algorithm. Of these 1,000 interactions, 400 had prior validation, while the remaining 600 represented plausible associations never before described.
"Predicting all protein interactions within a complete organism remains a highly complex challenge in modern biology. With this tool, we offer an ideal 'step zero' so the scientific community can place unknown proteins within their functional contexts and target their experimental trials much more precisely," noted Fernández.
To ensure the tool is useful to everyone, alongside the version optimized for supercomputing, the team also developed and released a lightweight, open-source library of ContextMirror2.0. This allows researchers to analyze smaller sets of proteins on a personal computer in an accessible way without requiring major computing infrastructure.
Looking ahead, the authors conclude, this tool and its comparative approach could facilitate the identification of therapeutic targets and the study of critical mechanisms such as bacterial antibiotic resistance in modern medicine.
Publication details
Miguel Fernandez-Martin et al., Sequence-based coevolutionary prediction of species-specific interactomes, PLOS Computational Biology (2026). DOI: 10.1371/journal.pcbi.1014839
