----- Data for Astrocladistical analysis of Jovian Trojans------

This data set is associate with Holt et al. (2021) 'Astrocladistics of the Jovian Trojan Swarms'. 

-Abstract-
The Jovian Trojans are two swarms of small objects that share Jupiter's orbit, clustered around the leading and trailing Lagrange points, L_4 and L_5. In this work, we investigate the Jovian Trojan population using the technique of astrocladistics, an adaptation of the ``tree of life'' approach used in biology. We combine colour data from WISE, SDSS, Gaia DR2 and MOVIS surveys with knowledge of the physical and orbital characteristics of the Trojans, to generate a classification tree composed of clans with distinctive characteristics. We identify 48 clans, indicating groups of objects that likely share a common origin. Amongst these are several that reflect the known collisional families, though our work identifies subtleties in that classification that bear future investigation. Our clans are often broken into subclans, and most can be grouped into 10 superclans, reflecting the hierarchical nature of the population.  Outcomes from this project include the identification of several high priority objects for additional observations and as well as providing context for the objects to be visited by the forthcoming \textit{Lucy} mission. Our results demonstrate the ability of astrocladistics to classify multiple large and heterogeneous composite survey datasets into groupings useful for studies of the origins and evolution of our Solar system

---------- Program descriptions---------- 



---------- Dataset descriptions---------- 

-------Dispersal Velocity-------
A set of dispersal velocities based on the superclans (Greater), clans and subclans (Sub) identified in Holt et al. 2021. Program availalbe the asosciated Github repository: https://github.com/TimHoltastro/holt-etal-2021-Jovian-Trojan-astrocladistics.git .  Claculated using reverse Gause equations (Zappala et al., 1996)
-- File descriptions--
Generated: 2020-05-29
File type: csv
Name: JTCluster-Lx-name-#.csv. Lx indicates the swarm, L4 or L5. Name indicates the superclan (Greater), clan or subclan(Sub) identified. # is the nubmer of objects in the cluster. 
e.g. JTCluster-L4-Eurybates-16.csv shows the dispersal velocities for the Eurybates clan, in the L4 swarm, which has 16 members.

-------Matricies-------
A set of matricies of the Jovian Trojans used in Holt et al. 2021.
-- File descriptions--
Generated:2020-05-23
File type: csv
Matrix-Subset-Pop.csv: Matrix of the subset used in Holt et al. (2021). 
Matrix-Subset-L4.csv: Matrix of the subset of the L4 swarm used in Holt et al. (2021). 
Matrix-Subset-L5.csv: Matrix of the subset of the L4 swarm used in Holt et al. (2021). 
JTClanParamaterMatrix.csv: Ranges of each paramater fo the superclans (Greater), clans and subclans (Sub) found in Holt et al. 2021. n: number of objects in each clan. Ranges are given based on the binned paramaters. 
-Binned 
These matricies have been binned using the python program availalbe on the associated Github
https://github.com/TimHoltastro/holt-etal-2021-Jovian-Trojan-astrocladistics.git
-individual matricies
These are selections of each superclan (Greater), clan and subclan (Sub) indentified in Holt et al. 2021.

-------Trees-------
A set of astrocladistical consnesus trees of the Jovian Trojans used in Holt et al. (2021). Created using Tree analysis using New Technology (TNT) 1.5 (Goloboff, et al. 2008, 2015). 
-- File descriptions--
Generated:2020-08-07
File type: pdf
SubMatrixWiseSDSSGaiaMovis-L4-Conserv.pdf: Consensus tree of the L4 subset.
SubMatrixWiseSDSSGaiaMovis-L5-Conserv.pdf: Consensus tree of the L5 subset.
-Individual clusters
Lx-name-tax.pdf: Details of individual clans and superclans. Lx shows L4 or L5 swarm. Name indicates the superclan (Greater) or clan identified. 
e.g. L4-GreaterAjax-tax.pdf is the consensus tree for the Greater Ajax superclan, in the L4 swarm. 



-- Refs. --
Goloboff, P. A., Farris, J. S., & Nixon, K. C. (2008). TNT, a free program for phylogenetic analysis. Cladistics, 24(5), 774–786. https://doi.org/10.1111/j.1096-0031.2008.00217.x

Goloboff, P. A., & Catalano, S. A. (2016). TNT version 1.5, including a full implementation of phylogenetic morphometrics. Cladistics, 32(3), 221–238. https://doi.org/10.1111/cla.12160

Holt, T.R., Horner, J., Nesvorný, D., King, R., Popescu, M., Carter, B.D. & Tylor, C.C.E. (2021) Astrocladistics of the Jovian Trojan Swarms. Submitted to Monthly Notices of the Royal Astronomical Society. 

Zappala, V., Cellino, A., Dell’Oro, A., Migliorini, F., & Paolicchi, P. (1996). Reconstructing the Original Ejection Velocity Fields of Asteroid Families. Icarus, 124(1), 156–180. https://doi.org/10.1006/icar.1996.0196
