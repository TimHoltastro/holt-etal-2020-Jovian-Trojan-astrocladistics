----- Jovian Trojan Clan Dispersal Velocities-----

A set of dispersal velocities based on the superclans (Greater), clans and subclans (Sub) identified in Holt et al. 2021. Program available the associated Github repository: https://github.com/TimHoltastro/holt-etal-2021-Jovian-Trojan-astrocladistics.git

-- File descriptions--

Generated: 2020-05-29
File type: csv

Name: JTCluster-Lx-name-#.csv. Lx indicates the swarm, L4 or L5. Name indicates the superclan (Greater), clan or subclan(Sub) identified. # is the number of objects in the cluster. 
e.g. JTCluster-L4-Eurybates-16.csv shows the dispersal velocities for the Eurybates clan, in the L4 swarm, which has 16 members. 

D:
Diameter of the object. From NASA-JPL HORIZONS Solar
System Dynamics Database https://ssd.jpl.nasa.gov/
Giorgini et al. (1996). Where not available, generated from H magnitude and
mean geometric albedo (0.075).
Units:km

dV_ref:
Dispersal velocity to the reference object (largest object in the cluster). Claculated using reverse Gause equations (Zappala et al., 1996) also see Holt et al. (2018, 2020)
Units: ms^-1

dV_cent:
Dispersal velocity to the mean of the cluster parameter space. Calculated using reverse Gauss equations (Zappala et al., 1996) also see Holt et al. (2018)
Units: ms^-1

F_esc:
Fraction of clones that escape the Jovian Trojan swarms. From Holt et al. (2020). 



-- Refs. --

Holt, T. R., Brown, A. J., Nesvorný, D., Horner, J., & Carter, B. D. (2018). Cladistical Analysis of the Jovian and Saturnian Satellite Systems. The Astrophysical Journal, 859(2), 97. https://doi.org/10.3847/1538-4357/aabe2c

Holt, T. R., Nesvorný, D., Horner, J., King, R., Marschall, R., Kamrowski, M., … Tylor, C. (2020). Stability of Jovian Trojans and their collisional families. Monthly Notices of the Royal Astronomical Society, 495(4), 4085–4097. https://doi.org/10.1093/mnras/staa1348

Holt, T.R., Horner, J., Nesvorný, D., King, R., Popescu, M., Carter, B.D. & Tylor, C.C.E. (2021) Astrocladistics of the Jovian Trojan Swarms. Submitted to Monthly Notices of the Royal Astronomical Society. 

Zappala, V., Cellino, A., Dell’Oro, A., Migliorini, F., & Paolicchi, P. (1996). Reconstructing the Original Ejection Velocity Fields of Asteroid Families. Icarus, 124(1), 156–180. https://doi.org/10.1006/icar.1996.0196
