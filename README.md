# Simulation

This directory contains files used to simulate case-level data, and to assess when protected information might inadvertently leak out via (unprotected) variant-level data and how we can guard against such leakage.

Includes functions to run 4 different types of simulations that each take one arguement
which represents the number of pedigrees one wants to produce for each simulation.

run_simulation: 
    Runs pedigree simulation for a specified number of pedigrees
        
    Produces file "pedigree.txt" that contains number of specified
    pedigrees

    For each family in pedigrees goes through the following steps:
    1) Makes a healthy pedigree with designated proband, proband's
    parents, proband's grandparents, proband's aunts/uncles
    2) Randomly assigns pedigree founders (proband's grandparents)
    cancer using probabilties from Antoniou et al 2004 Table 1
    3) Randomly assigns pedigree founder mutations based on their cancer
    status using probabilities from Antonious et al 2004 Table 2
    4) Passes founder mutations from founder to each offspring with 50%
    chance of passing mutation
    5) Randomly assigns cancer to remaining individuals in pedigree
        
run_sim_fhx: 
    Runs pedigree simulation for a specified number of pedigrees as in 
    run_simulation
        
    Outputs "pedigree.txt" as before and also outputs "familyhistory.txt" 
    that contains summary family history information for each pedigree
        
run_ca_sims: 
    Runs pedigree simulation as in run_simulation but only returns pedigrees
    where at least one family member has a mutation
        
    Runs slowly when given large number of trials due to small probability of
    having a mutation if an indivdual has cancer
        
run_ca_sim_fhx: 
    Runs pedigree simulation as in run_ca_sims but also outputs summary family
    history in "familyhistory.txt" file
        
    Runs slowly when given large number of trials due to small probability of
    having a mutation if an indivdual has cancer
        
        
"pedigree.txt" uses the following abbreviations as headers:
     FamID: Unique family ID
     Name: same as IndID
     Target: 1 = proband, 0 = other members of pedigree
     IndID: Unique individual ID
     FathID: unique ID of father of individual
     MothID: unique ID of mother of individual
     Sex: gender of individual
     Twin: 1 = monozygotic twin, 0 = not monozygotic twin
     Dead: 1 = dead, 0 = alive
     Age: represents either current age or age at death
     Birth Year: birth year of individual
     BrCa_1: integer = age at 1st breast cancer diagnosis, 0 = unaffected
     BrCa_2: integer = age at 2nd breast cancer diagnosis, 0 = unaffected
     OvCa: integer = age at diagnosis of ovarian cancer, 0 = unaffected
     ProCa: integer = age at diagnosis of prostate cancer, 0 = unaffected
     PanCa: integer = age at diagnosis of pancreatic cancer, 0 = unaffected
     G Test: genetic test 0 = untested, S = mutation search, 
             T = direct gene test
     Mutn: mutation status 0 = untested, N = no mutation, 1 = BRCA 1+, 2 =
           BRCA2+, 3 = BRCA1+ and BRCA2+
     Ashkn: 0 = not Ashkanzi, 1 = Ashkenazi
     For the follwoing variables 0 = unaffected, N = neagtive, P = positive
     ER: Estrogen receptor status
     PR: = Progesteron receptor status
     HER2: = Human epidermal growth factor receptor status
     CK14: Cytokeratin 14 status 
     CK56: Cytokeratin 56 status
     
"familyhistory.txt" uses the following abbreviations as headers:
     fhx: family history known/present, 1 = known, 0 = unknown
     br_ca_ls: number of first degree relatives with female breast cancer
               diagnosis at age under 50
     br_ca_gr: number of first degree relatives with breast
               cancer diagnosis at age 50 or greater  
     ov_ca: number of first degree relatives with ovarian cancer
     m2_br_ca: number of maternal second degree relatives with female
               breast cancer
     p2_br_ca: number of paternal second degree relatives with female
               breast cancer
     m2_ov_ca: number of materal second degree relatives with ovarian
               cancer
     p2_ov_ca: number of paternal second degree relatives with
               ovarian cancer
     male_br_ca: number of first or second degree relatives with male
                 breast cancer, always 0 for this simulation
     pan_ca: number of first of second degree relatives with
             pancreatic cancer, always 0 for this simulation
