----- Jovian Trojan Matricies------

A set of matrices of the Jovian Trojans used in Holt et al. 2021.
-- File descriptions--

Generated: 2020-05-23
File type: csv 
Also available in nexus format

Matrix-Subset-Pop.csv: Matrix of the subset used in Holt et al. (2021). 
Matrix-Subset-L4.csv: Matrix of the subset of the L4 swarm used in Holt et al. (2021). 
Matrix-Subset-L5.csv: Matrix of the subset of the L4 swarm used in Holt et al. (2021). 

JTClanParamaterMatrix.csv: Ranges of each parameter for the superclans (Greater), clans and subclans (Sub) found in Holt et al. 2021. n: number of objects in each clan. Ranges are given based on the binned parameters. 

-Binned 
These matrices have been binned using the python program available on the associated Github
https://github.com/TimHoltastro/holt-etal-2021-Jovian-Trojan-astrocladistics.git

-individual matrices
These are selections of each superclan (Greater), clan and subclan (Sub) identified in Holt et al. 2021.

-- Characteristics --
full_name
Name of the object. From NASA-JPL HORIZONS Solar
System Dynamics Database https://ssd.jpl.nasa.gov/
Giorgini et al. (1996).
Format: number name (designation) 
e.g. 624 Hektor (1907 XM)

da_p
Proper delta semi-major axis of the object. From AsyDys database 
https://newton.spacedys.com/astdys/
Reference: Knežević & Milani (2017)
Units: au
L4 Bin Number: 13 
L4 R^2 value: 0.9901523311842176 
L4 Bin deliminators: [0.0004417 0.01277692 0.02495385 0.03713077
0.04930769 0.06148462 0.07366154 0.08583846 0.09801538
0.11019231 0.12236923 0.13454615 0.14672308 0.1589 ]
L5 Bin Number: 13
L5 R^2 value: 0.990187210122306
L5 Bin deliminators: [0.0041526 0.01563846 0.02697692
0.03831538 0.04965385 0.06099231 0.07233077 0.08366923
0.09500769 0.10634615 0.11768462 0.12902308 0.14036154
0.1517 ]

e_p
Proper eccentricity of the object. From AsyDys database 
https://newton.spacedys.com/astdys/
Units: n/a
Reference: Knežević & Milani (2017)
L4 Bin Number: 15 
L4 R^2 value: 0.9900176884771242 
L4 Bin deliminators: [0.0035364 0.01460667 0.02551333 0.03642
0.04732667 0.05823333 0.06914 0.08004667 0.09095333 0.10186
0.11276667 0.12367333 0.13458 0.14548667 0.15639333 0.1673 ]
L5 Bin Number: 15
L5 R^2 value: 0.9875593041451958
L5 Bin deliminators: [0.0041151 0.01662667 0.02895333 0.04128
0.05360667 0.06593333 0.07826 0.09058667 0.10291333 0.11524
0.12756667 0.13989333 0.15222 0.16454667 0.17687333 0.1892 ]

sini_p
Sine of the proper inclination of the object. From AsyDys database 
https://newton.spacedys.com/astdys/
Units: n/a
Reference: Knežević & Milani (2017)
L4 Bin Number: 15 
L4 R^2 value: 0.9869867323036892 
L4 Bin deliminators: [0.0101936 0.06476 0.11852 0.17228 0.22604 0.2798
0.33356 0.38732 0.44108 0.49484 0.5486 0.60236 0.65612 0.70988
0.76364 0.8174 ]
L5 Bin Number: 13 
L5 R^2 value: 0.9901097647298851 
L5 Bin deliminators: [0.012521 0.06543077 0.11766154 0.16989231
0.22212308 0.27435385 0.32658462 0.37881538 0.43104615
0.48327692 0.53550769 0.58773846 0.63996923 0.6922 ]

MeanLib
Mean libration value, relative to Jupiter. Calculated using REBOUND
(Rein & Liu 2012; Rein & Tamayo 2015) as outlined in section 2.1 of Holt et al. (2021)
of the text.
Units: degree
Reference: n/a
L4 Bin Number: 15
L4 R^2 value: 0.9837731931286373
L4 Bin deliminators: [56.4248396 57.77509172 59.10538938
60.43568704 61.7659847 63.09628236 64.42658001 65.75687767
67.08717533 68.41747299 69.74777065 71.07806831
72.40836597 73.73866362 75.06896128 76.39925894]
L5 Bin Number: 14
L5 R^2 value: 0.9907973521852185
L5 Bin deliminators: [ 285.72582824 286.91482596 288.0862523  289.25767863 290.42910496
 291.60053129 292.77195762 293.94338395 295.11481029 296.28623662
 297.45766295 298.62908928 299.80051561 300.97194195 302.14336828
 303.31479461]

LibRange
Range of the objects libration, relative to Jupiter. Calculated using
REBOUND (Rein & Liu 2012; Rein & Tamayo 2015) as outlined in
section 2.1 of of Holt et al. (2021).
Units: degree
Reference: n/a
L4 Bin Number: 14
L4 R^2 value: 0.9904121023736628
L4 Bin deliminators: [ 4.04450175 9.22096281 14.325954
19.43094519 24.53593638 29.64092757 34.74591876 39.85090995 
44.95590114 50.06089233 55.16588352
60.27087471 65.3758659 70.48085709 75.58584828]
L5 Bin Number: 14
L5 R^2 value: 0.9907973521852185
L5 Bin deliminators: [ 2.7354308 7.67859255 12.55350552
17.42841848 22.30333145 27.17824441 32.05315738 36.92807035 
41.80298331 46.67789628 51.55280924
56.42772221 61.30263518 66.17754814 71.05246111]

albedo
Geometric albedo of the object. From NASA-JPL HORIZONS Solar
System Dynamics Database https://ssd.jpl.nasa.gov/
Giorgini et al. (1996).
Units: n/a
Reference: Giorgini et al. (1996)
L4 Bin Number: 15
L4 R^2 value: 0.9830386940542256
L4 Bin deliminators: [0.024827 0.03653333 0.04806667 0.0596
0.07113333 0.08266667 0.0942 0.10573333 0.11726667 0.1288
0.14033333 0.15186667 0.1634 0.17493333 0.18646667 0.198 ]
L5 Bin Number: 15
L5 R^2 value: 0.9816963650614118
L5 Bin deliminators: [0.030831 0.04226667 0.05353333 0.0648
0.07606667 0.08733333 0.0986 0.10986667 0.12113333 0.1324
0.14366667 0.15493333 0.1662 0.17746667 0.18873333 0.2

W1Alb
Near Infrared values from the WISE survey using the W1 filter
(3.4μm).
Units: magnitude
Reference: Grav et al. (2011, 2012)
L4 Bin Number: 15
L4 R^2 value: 0.9823685939873733
L4 Bin deliminators: [0.055661 0.0786 0.1012 0.1238 0.1464
0.169 0.1916 0.2142 0.2368 0.2594 0.282 0.3046 0.3272 0.3498
0.3724 0.395 ]
L5 Bin Number: 15
L5 R^2 value: 0.9794794869794033
L5 Bin deliminators: [0.065666 0.08826667 0.11053333 0.1328
0.15506667 0.17733333 0.1996 0.22186667 0.24413333 0.2664
0.28866667 0.31093333 0.3332 0.35546667 0.37773333 0.4 ]

W2Alb
Near Infrared values from the WISE survey using the W2 filter
(4.6μm).
Units: magnitude
Reference: Grav et al. (2011, 2012)
L4 Bin Number: 15
L4 R^2 value: 0.9837919222258167
L4 Bin deliminators: [0.035641 0.05993333 0.08386667 0.1078
0.13173333 0.15566667 0.1796 0.20353333 0.22746667 0.2514
0.27533333 0.29926667 0.3232 0.34713333 0.37106667 0.395 ]
L5 Bin Number: 15
L5 R^2 value: 0.9773285129258688
L5 Bin deliminators: [0.027628 0.0528 0.0776 0.1024 0.1272
0.152 0.1768 0.2016 0.2264 0.2512 0.276 0.3008 0.3256 0.3504
0.3752 0.4 ]

g mag -mean
Mean G band magnitude from the GAIA survey. Filter passband
from 330nm to 1050nm Evans et al. (2018).
Units: magnitude
Reference: Spoto et al. (2018) 
L4 Bin Number: 15 
L4 R^2 value: 0.9894101650398079 
L4 Bin deliminators: [15.10926146
15.38560874 15.65787207 15.9301354 16.20239873 16.47466206
16.74692539 17.01918872 17.29145205 17.56371538
17.83597871 18.10824204 18.38050537 18.65276871
18.92503204 19.19729537] 
L5 Bin Number: 12 
L5 R^2 value: 0.9904193815513793 
L5 Bin deliminators: [15.85627031
16.11791172 16.37645066 16.6349896 16.89352854 17.15206747
17.41060641 17.66914535 17.92768429 18.18622323
18.44476217 18.7033011 18.96184004]

(b - v)
Index of Johnson B (442nm) and Johnson V (540nm) band
magnitudes, calculated from SDSS photometry (Fukugita et al.
1996).
Units: magnitude
Reference: Szabo et al. (2007)
L4 Bin Number: 15
L4 R^2 value: 0.9591346835087617
L4 Bin deliminators: [0.50896 0.57933333 0.64866667 0.718
0.78733333 0.85666667 0.926 0.99533333 1.06466667 1.134
1.20333333 1.27266667 1.342 1.41133333 1.48066667 1.55 ]
L5 Bin Number: 15
L5 R^2 value: 0.9877740996058247
L5 Bin deliminators: [0.60968 0.63133333 0.65266667 0.674
0.69533333 0.71666667 0.738 0.75933333 0.78066667 0.802
0.82333333 0.84466667 0.866 0.88733333 0.90866667 0.93 ]

(u - g)
Index of U (354.3nm) and G (477nm) band magnitudes taken from
the SDSS (Fukugita et al. 1996).
Units: magnitude
Reference: Szabo et al. (2007)
L4 Bin Number: 15
L4 R^2 value: 0.9656002330018459
L4 Bin deliminators: [0.873585 0.96933333 1.06366667 1.158
1.25233333 1.34666667 1.441 1.53533333 1.62966667 1.724
1.81833333 1.91266667 2.007 2.10133333 2.19566667 2.29 ]
L5 Bin Number: 15
L5 R^2 value: 0.97239842191769
L5 Bin deliminators: [0.62835 0.74 0.85 0.96 1.07 1.18 1.29 1.4
1.51 1.62 1.73 1.84 1.95 2.06 2.17 2.28 ]

(g - r)
Index of G (477nm) and R (623.1nm) band magnitudes taken from
the SDSS (Fukugita et al. 1996).
Units: magnitude
Reference: Szabo et al. (2007)
L4 Bin Number: 15
L4 R^2 value: 0.9560363222011405
L4 Bin deliminators: [0.299 0.36666667 0.43333333 0.5
0.56666667 0.63333333 0.7 0.76666667 0.83333333 0.9
0.96666667 1.03333333 1.1 1.16666667 1.23333333 1.3 ]
L5 Bin Number: 15
L5 R^2 value: 0.9850695579802035
L5 Bin deliminators: [0.4197 0.44 0.46 0.48 0.5 0.52 0.54 0.56
0.58 0.6 0.62 0.64 0.66 0.68 0.7 0.72 ]

(r - i)
Index of R (623.1nm) and I (762.5nm) band magnitudes taken
from the SDSS (Fukugita et al. 1996).
Units: magnitude
Reference: Szabo et al. (2007)
L4 Bin Number: 15
L4 R^2 value: 0.9889673218392642
L4 Bin deliminators: [0.09976 0.116 0.132 0.148 0.164 0.18 0.196
0.212 0.228 0.244 0.26 0.276 0.292 0.308 0.324 0.34 ]
L5 Bin Number: 15
L5 R^2 value: 0.9841490399412055
L5 Bin deliminators: [0.06824 0.09066667 0.1127619 0.13485714
0.15695238 0.17904762 0.20114286 0.2232381 0.24533333
0.26742857 0.28952381 0.31161905 0.33371429 0.35580952
0.37790476 0.4 ]


(i - z)
Index of I (762.5nm) and Z (913.4nm) band magnitudes taken from
the SDSS (Fukugita et al. 1996).
Units: magnitude
Reference: Szabo et al. (2007)
L4 Bin Number: 15
L4 R^2 value: 0.9613960873233834
L4 Bin deliminators: [-0.55087 -0.492 -0.434 -0.376 -0.318 -0.26
-0.202 -0.144 -0.086 -0.028 0.03 0.088 0.146 0.204 0.262 0.32 ]
L5 Bin Number: 15
L5 R^2 value: 0.9656110906722879
L5 Bin deliminators: [-0.37082 -0.31533333 -0.26066667 -0.206
-0.15133333 -0.09666667 -0.042 0.01266667 0.06733333 0.122
0.17666667 0.23133333 0.286 0.34066667 0.39533333 0.45 ]

(Y - J)
Index of Y (1.02μm) and J (1.25μm) band magnitudes from the
VISTA survey (Sutherland et al. 2015), in the MOVIS database
(Popescu et al. 2016).
Units: magnitude
Reference: Popescu et al. (2018)
L4 Bin Number: 15 
L4 R^2 value: 0.98747935083033 
L4 Bin deliminators: [0.02060934 0.0655506 0.1098277 0.1541048
0.1983819 0.242659 0.2869361 0.3312132 0.3754903 0.4197674
0.4640445 0.5083216 0.5525987 0.5968758 0.6411529 0.68543
] 
L5 Bin Number: 15 
L5 R^2 value: 0.9886225775779977 
L5 Bin deliminators: [0.05425359 0.09975333 0.14458067 0.189408
0.23423533 0.27906267 0.32389 0.36871733 0.41354467
0.458372 0.50319933 0.54802667 0.592854 0.63768133
0.68250867 0.727336 ]

(J - Ks)
Index of J (1.25μm) and K (2.15μm) band magnitudes from the
VISTA survey (Sutherland et al. 2015), in the MOVIS database
(Popescu et al. 2016).
Units: magnitude
Reference: Popescu et al. (2018)
L4 Bin Number: 15
L4 R^2 value: 0.984597756033517
L4 Bin deliminators: [0.14045928 0.25723273 0.37228047
0.4873282 0.60237593 0.71742367 0.8324714 0.94751913
1.06256687 1.1776146 1.29266233 1.40771007 1.5227578
1.63780553 1.75285327 1.867901 ]
L5 Bin Number: 15
L5 R^2 value: 0.9889442542998902
L5 Bin deliminators: [0.06778045 0.16160333 0.25403967
0.346476 0.43891233 0.53134867 0.623785 0.71622133
0.80865767 0.901094 0.99353033 1.08596667 1.178403
1.27083933 1.36327567 1.455712 ]

(H - Ks)
Index of H (1.65μm) and K (2.15μm) band magnitudes from the
VISTA survey (Sutherland et al. 2015), in the MOVIS database
(Popescu et al. 2016).
Units: magnitude
Reference: Popescu et al. (2018)
L4 Bin Number: 8 
L4 R^2 value: 0.9990695024162797 
L4 Bin deliminators: [-0.33295512 -0.2505985 -0.1688955 -0.0871925 -
0.0054895 0.0762135 0.1579165 0.2396195 0.3213225 ] 
L5 Bin Number: 14 
L5 R^2 value: 0.990567513882253 
L5 Bin deliminators:
[-0.1558507 -0.05802146 0.03845707 0.13493561 0.23141414
0.32789268 0.42437121 0.52084975 0.61732829 0.71380682
0.81028536 0.90676389 1.00324243 1.09972096 1.1961995 ]

L	
Libration lagrange point of the object around Jupiter. Either L4 (4) or L5 (5), 60 degrees ahead or behind in the orbit of Jupiter. 

GreaterClan, Clan and SubClan
Taxonomic framework presented in Holt et al 2021. 

tax_c
Canonical taxonomic designation, based on the Bus-Demeo taxonomy (DeMeo et al. 2009). Note: any ’P-type’ have been modernised into the X-types. Reference dataset  used is in tax_ref.

tax_ref
Source of canonical taxonomic classification (tax_c) Tholen1989:Tholen (1989); Bendjoya2004: Bendjoya et al. (2004); Fornasier2004 (Fornasier et al. 2004); Lazzaro2004: Lazzaro et al.(2004); Fornasier2007: Fornasier et al. (2007); Hasselmann2012: Hasselmann et al. (2012).

-- Refs. --
Bendjoya, P., Cellino, A., Di Martino, M., & Saba, L. (2004). Spectroscopic observations of Jupiter Trojans. Icarus, 168(2), 374–384. https://doi.org/10.1016/j.icarus.2003.12.004

DeMeo, F. E., Binzel, R. P., Slivan, S. M., & Bus, S. J. (2009). An extension of the Bus asteroid taxonomy into the near-infrared. Icarus, 202(1), 160–180. https://doi.org/10.1016/j.icarus.2009.02.005

Fornasier, S., Dotto, E., Marzari, F., Barucci, M. ~A., Boehnhardt, H., Hainaut, O., & Debergh, C. (2004). Visible spectroscopic and photometric survey of L5 Trojans: investigation of dynamical families. Icarus, 172(1), 221–232. https://doi.org/10.1016/j.icarus.2004.06.015

Fornasier, S., Dotto, E., Hainaut, O., Marzari, F., Boehnhardt, H., Deluise, F., & Barucci, M. ~A. (2007). Visible spectroscopic and photometric survey of Jupiter Trojans: Final results on dynamical families. Icarus, 190(2), 622–642. https://doi.org/10.1016/j.icarus.2007.03.033

Fukugita, M., Ichikawa, T., Gunn, J. E., Doi, M., Shimasaku, K., & Schneider, D. P. (1996). The Sloan Digital Sky Survey Photometric System. The Astronomical Journal, 111, 1748. https://doi.org/10.1086/117915

Fukugita, M., Ichikawa, T., Gunn, J. E., Doi, M., Shimasaku, K., & Schneider, D. P. (1996). The Sloan Digital Sky Survey Photometric System. The Astronomical Journal, 111, 1748. https://doi.org/10.1086/117915

Grav, T., Mainzer, A. K., Bauer, J. M., Masiero, J. R., Spahr, T. B., McMillan, R. S., … Wilkins, A. (2011). WISE /NEOWISE OBSERVATIONS OF THE JOVIAN TROJANS: PRELIMINARY RESULTS. The Astrophysical Journal, 742(1), 40. https://doi.org/10.1088/0004-637X/742/1/40

Grav, T., Mainzer, A. K., Bauer, J. M., Masiero, J. R., & Nugent, C. R. (2012). WISE/NEOWISE observations of the Jovian Trojan Population: Taxonomy. The Astrophysical Journal, 759(1), 49. https://doi.org/10.1088/0004-637X/759/1/49

Hasselmann, P. H., Carvano, J. M., & Lazzaro, D. (2012). SDSS-based Asteroid Taxonomy V1.1. EAR-A-I0035-5-SDSSTAX-V1.1. NASA Planetary Data System. Retrieved from https://sbn.psi.edu/pds/resource/sdsstax.html

Holt, T.R., Horner, J., Nesvorný, D., King, R., Popescu, M., Carter, B.D. & Tylor, C.C.E. (2021) Astrocladistics of the Jovian Trojan Swarms. Submitted to Monthly Notices of the Royal Astronomical Society. 

Knežević, Z., & Milani, A. (2017). AstDys: Synthetic proper elements 5553 numbered and multiopposition Trojans. Retrieved from https://newton.spacedys.com/~astdys2/propsynth/tro.syn

Lazzaro, D., Angeli, C. A., Carvano, J. M., Mothé-Diniz, T., Duffard, R., & Florczak, M. (2004). S3OS2: The visible spectroscopic survey of 820 asteroids. Icarus, 172(1 SPEC.ISS.), 179–220. https://doi.org/10.1016/j.icarus.2004.06.006

Popescu, M., Licandro, J., Morate, D., de León, J., Nedelcu, D. A., Rebolo, R., … Irwin, M. (2016). Near-infrared colors of minor planets recovered from VISTA-VHS survey (MOVIS). Astronomy & Astrophysics, 591, A115. https://doi.org/10.1051/0004-6361/201628163

Popescu, M., Licandro, J., Carvano, J. M., Stoicescu, R., De León, J., Morate, D., … Cristescu, C. P. (2018). Taxonomic classification of asteroids based on MOVIS near-infrared colors. Astronomy and Astrophysics, 617. https://doi.org/10.1051/0004-6361/201833023

Rein, H., & Liu, S.-F. (2012). REBOUND: an open-source multi-purpose N -body code for collisional dynamics. Astronomy & Astrophysics, 537, A128. https://doi.org/10.1051/0004-6361/201118085

Rein, H., & Tamayo, D. (2015). whfast: a fast and unbiased implementation of a symplectic Wisdom–Holman integrator for long-term gravitational simulations. Monthly Notices of the Royal Astronomical Society, 452(1), 376–388. https://doi.org/10.1093/mnras/stv1257

Spoto, F., Tanga, P., Mignard, F., Berthier, J., Carry, B., Cellino, A., … Zwitter, T. (2018). Gaia Data Release 2. Astronomy & Astrophysics, 616, A13. https://doi.org/10.1051/0004-6361/201832900

Sutherland, W., Emerson, J., Dalton, G., Atad-Ettedgui, E., Beard, S., Bennett, R., … Woodhouse, G. (2015). The Visible and Infrared Survey Telescope for Astronomy (VISTA): Design, technical overview, and performance. Astronomy & Astrophysics, 575, A25. https://doi.org/10.1051/0004-6361/201424973

Szabo, G. M., Ivezić, Ž., Jurić, M., & Lupton, R. H. (2007). The properties of Jovian Trojan asteroids listed in SDSS Moving Object Catalogue 3. Monthly Notices of the Royal Astronomical Society, 377(4), 1393–1406. https://doi.org/10.1111/j.1365-2966.2007.11687.x

Tholen, D. J. (1989). Asteroid taxonomic classifications. In Asteroids II (p. 1139). University of Arizona Press.








