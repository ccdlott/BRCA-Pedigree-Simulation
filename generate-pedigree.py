#!/usr/bin/env python
import random
from datetime import datetime
now = datetime.now()
year = now.year

class Pedigree(object):
    '''
    The following definitions/abbreviations are used throughout this class
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
    '''

    family_id = 0
    ind_id = 0

    def __init__(self):
        '''Initializes a unique family ID for each instance of a pedigree'''
        Pedigree.family_id += 1

    def get_family_id(self):
        '''Returns unique family ID when called'''
        return self.family_id

    def get_ind_id(self):
        '''Returns unique individual ID when called'''
        Pedigree.ind_id += 1
        return self.ind_id

    def get_gender(self):
        '''Randomly returns either M for male or F for female when called'''
        gender = random.randint(1,2)
        if gender == 1:
            return "M"
        else:
            return "F"
        
    def init_proband(self):
        '''
        Initializes the proband for the pedigree and returns a list in
        the format:
        [FamID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, 
        Mutn, Ashkn, ER, PR, HER2, CK14, CK56]
        '''
        fam_id = self.get_family_id()
        person_id = self.get_ind_id()
        name = person_id
        target = 1
        moth_id = 0
        fath_id = 0
        gender = self.get_gender()
        twin = 0
        dead = 0
        age = random.randint(20,65)
        birth_year = int(year)-int(age)
        br_ca_dx1 = 0
        br_ca_dx2 = 0
        ov_ca_dx = 0
        pro_ca_dx = 0
        pan_ca_dx = 0
        g_test = 0
        mutn = 0
        ashkn = 0
        ER = 0
        PR = 0
        HER2 = 0
        CK14 = 0
        CK56 = 0
        proband = []
        variables = [fam_id, name, target, person_id, fath_id, moth_id,
                    gender, twin, dead, age, birth_year, br_ca_dx1,
                    br_ca_dx2, ov_ca_dx, pro_ca_dx, pan_ca_dx, g_test,
                    mutn, ashkn, ER, PR, HER2, CK14, CK56]
        for variable in variables:
            proband.append(variable)
        return proband

##to debug init_proband
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    new_proband = new_ped.init_proband()
#    print "Proband", x
#    print new_proband
#    x += 1

    def add_parents(self, person):
        '''
        Adds parent information for an individual
        Returns a list of lists with information for child's  mother and
        father in the following format:
        [Fam ID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, Mutn,
        Ashkn, ER, PR, HER2, CK14, CK56]
        '''
        person_moth_id = person[5]
        person_fath_id = person[4]
        if person_moth_id == 0 and person_fath_id == 0:
            fam_id = person [0]
            person_moth_id = self.get_ind_id()
            person_fath_id = self.get_ind_id()
            person_moth_name = person_moth_id
            person_fath_name = person_fath_id
            moth_id = 0
            fath_id = 0
            target = 0
            moth_gender = "F"
            fath_gender = "M"
            twin = 0
            child_age = int(person[9])
            moth_age = random.randint(child_age + 20, child_age + 40)
            fath_age = random.randint(child_age + 20, child_age + 40)
            moth_birth_year = int(year) - int(moth_age)
            fath_birth_year = int(year) - int(fath_age)
            if moth_age > 90:
                moth_dead = 1
                moth_age = 91
            else:
                moth_dead = 0
            if fath_age > 90:
                fath_dead = 1
                fath_age = 91
            else:
                fath_dead = 0
            br_ca_dx1 = 0
            br_ca_dx2 = 0
            ov_ca_dx = 0
            pro_ca_dx = 0
            pan_ca_dx = 0
            g_test = 0
            mutn = 0
            ashkn = 0
            ER = 0
            PR = 0
            HER2 = 0
            CK14 = 0
            CK56 = 0
            moth_variables = [fam_id, person_moth_name, target, person_moth_id, fath_id,
                              moth_id, moth_gender, twin, moth_dead, moth_age,
                              moth_birth_year, br_ca_dx1, br_ca_dx2,
                              ov_ca_dx, pro_ca_dx, pan_ca_dx, g_test,
                              mutn, ashkn, ER, PR, HER2, CK14, CK56]
            fath_variables = [fam_id, person_fath_name, target, person_fath_id, fath_id,
                              moth_id, fath_gender, twin, fath_dead, fath_age,
                              fath_birth_year, br_ca_dx1, br_ca_dx2,
                              ov_ca_dx, pro_ca_dx, pan_ca_dx, g_test,
                              mutn, ashkn, ER, PR, HER2, CK14, CK56]
            mother = []
            for variable in moth_variables:
                mother.append(variable)
            father = []
            for variable in fath_variables:
                father.append(variable)
            person[5] = person_moth_id
            person[4] = person_fath_id
            parents = []
            parents.append(father)
            parents.append(mother)
            return parents
        else:
            raise TypeError("This person already has parents")
        
##to debug add_parents
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    print "Pedigree", x
#    new_proband = new_ped.init_proband()
#    new_parents = new_ped.add_parents(new_proband)
#    print "Proband", new_proband
#    print "Mother", new_parents[1]
#    print "Father", new_parents[0]
#    x += 1

##to debug expection to add_parents
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    new_proband = new_ped.init_proband()
#    new_parents = new_ped.add_parents(new_proband)
#    other_parents = new_ped.add_parents(new_proband)

    def add_partner(self, person):
        '''
        Creates a partner given a specific person and randomly generates
        offspring for pair
        Returns a list of information for the new partner in
        the following format:
        [Fam ID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, Mutn,
        Ashkn, ER, PR, HER2, CK14, CK56]
        '''
        fam_id = person[0]
        partner_id = self.get_ind_id()
        partner_name = partner_id
        partner_target = 0
        partner_moth_id = 0
        partner_fath_id = 0
        person_gender = person[6]
        if person_gender == "M":
            partner_gender = "F"
        else:
            partner_gender = "M"
        partner_twin = 0
        partner_dead = 0
        person_age = int(person[9])
        partner_age = random.randint(person_age - 15, person_age + 15)
        if partner_age > 90:
            partner_age = 91
            partner_dead = 1
        partner_birth_year = int(year)-int(partner_age)
        br_ca_dx1 = 0
        br_ca_dx2 = 0
        ov_ca_dx = 0
        pro_ca_dx = 0
        pan_ca_dx = 0
        g_test = 0
        mutn = 0
        ashkn = 0
        ER = 0
        PR = 0
        HER2 = 0
        CK14 = 0
        CK56 = 0
        partner = [fam_id, partner_name, partner_target, partner_id,
                   partner_fath_id, partner_moth_id,
                   partner_gender, partner_twin,
                   partner_dead, partner_age, partner_birth_year,
                   br_ca_dx1, br_ca_dx2, ov_ca_dx,
                   pro_ca_dx, pan_ca_dx, g_test, mutn, ashkn, ER,
                   PR, HER2, CK14, CK56]
        return partner

##to debug add_partner
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    new_pro = new_ped.init_proband()
#    family  = new_ped.add_parents(new_pro)
#    partner = new_ped.add_partner(new_pro)
#    family.append(partner)
#    print "Family", x
#    print "Mother", family[0]
#    print "Father", family[1]
#    print "Proband", new_pro
#    print "Proband Partner", family[2]
#    x += 1


    def add_offspring(self, person1, person2):
        '''
        Generates offrsping given 2 parents

        Returns a list of lists with each list representing one child in
        the following format:
        [Fam ID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, Mutn,
        Ashkn, ER, PR, HER2, CK14, CK56]
        '''
        fam_id = person1[0]
        if person1[6] == "F":
            moth_id = person1[3]
            fath_id = person2[3]
            moth_age = int(person1[9])
        else:
            moth_id = person2[3]
            fath_id = person1[3]
            moth_age = int(person2[9])
        num_children = random.randint(0,4)
        children = []
        for child in range(num_children):
            child_id = self.get_ind_id()
            child_name = child_id
            child_target = 0
            child_gender = self.get_gender()
            child_twin = 0
            child_dead = 0
            child_age = random.randint(moth_age - 40, moth_age -
                        20)
            if child_age <= 0:
                child_age = 1
            child_birth_year = int(year) - int(child_age)
            br_ca_dx1 = 0
            br_ca_dx2 = 0
            ov_ca_dx = 0
            pro_ca_dx = 0
            pan_ca_dx = 0
            g_test = 0
            mutn = 0
            ashkn = 0
            ER = 0
            PR = 0
            HER2 = 0
            CK14 = 0
            CK56 = 0
            child_variables = [fam_id, child_name, child_target, child_id, fath_id,
                               moth_id, child_gender, child_twin, child_dead,
                               child_age, child_birth_year, br_ca_dx1,
                               br_ca_dx2, ov_ca_dx, pro_ca_dx,
                               pan_ca_dx, g_test, mutn, ashkn, ER,
                               PR, HER2, CK14, CK56]
            children.append(child_variables)
        return children

#to debug add_offspring
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    new_pro = new_ped.init_proband()
#    new_part = new_ped.add_partner(new_pro)
#    new_children= new_ped.add_offspring(new_pro, new_part)
#    print "Pedigree", x
#    print "Parent 1", new_pro
#    print "Parent 2", new_part
#    for child in range(len(new_children)):
#        print "Child", child+1, new_children[child]
#    x += 1

    def add_siblings(self, person):
        '''
        Given a particular person, generates siblings. Parents must be
        initialized before creating any siblings

        Returns of list of lists containing the information for each
        siblings in the following format:
        [Fam ID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, Mutn,
        Ashkn, ER, PR, HER2, CK14, CK56]
        '''
        fam_id = person[0]
        moth_id = person[5]
        fath_id = person[4]
        person_age = int(person[9])
        if moth_id == 0 and fath_id == 0:
            raise ValueError("Must add parents before adding siblings")
        else:
            num_sibs = random.randint(0,4)
            siblings = []
            for sib in range(num_sibs):
                sib_id = self.get_ind_id()
                sib_name = sib_id
                sib_target = 0
                sib_gender = self.get_gender()
                sib_twin = 0
                sib_dead = 0
                sib_age = random.randint(person_age - 15, person_age +
                                         15)
                sib_birth_year = int(year) - int(sib_age)
                if sib_age > 90:
                    sib_dead = 1
                    sib_age = 91
                br_ca_dx1 = 0
                br_ca_dx2 = 0
                ov_ca_dx = 0
                pro_ca_dx = 0
                pan_ca_dx = 0
                g_test = 0
                mutn = 0
                ashkn = 0
                ER = 0
                PR = 0
                HER2 = 0
                CK14 = 0
                CK56 = 0
                sib_variables = [fam_id, sib_name, sib_target, sib_id, fath_id,
                                 moth_id, sib_gender, sib_twin, sib_dead,
                                 sib_age, sib_birth_year, br_ca_dx1,
                                 br_ca_dx2, ov_ca_dx, pro_ca_dx,
                                 pan_ca_dx, g_test, mutn, ashkn, ER,
                                 PR, HER2, CK14, CK56]
                siblings.append(sib_variables)
            return siblings
        
#to debug add_siblings
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    new_pro = new_ped.init_proband()
#    new_parents = new_ped.add_parents(new_pro)
#    new_sibs = new_ped.add_siblings(new_pro)
#    print "Pedigree", x
#    print "Mother", new_parents[1]
#    print "Father", new_parents[0]
#    print "Proband", new_pro
#    for sib in range(len(new_sibs)):
#        print "Sibling", sib+1, new_sibs[sib]
#    x += 1

    def make_healthy_pedigree(self):
        '''
        Randomly generates a pedigree of 3 generations with proband in
        final generation

        Returns a list of lists with information for each pedigree
        member in the following format:
        [Fam ID, Name, Target, IndID, FathID, MothID, Sex, Twin, Dead,
        Age, Birth Year, BrCa_1, BrCa_2, OvCa, ProCa, PanCa, G Test, Mutn,
        Ashkn, ER, PR, HER2, CK14, CK56]

        Order of family members is paternal grandfather, paternal
        grandmother, materal grandfather, maternal grandmother, father,
        mother, father's siblings, mother's siblings, proband's
        siblings, proband
        '''
        pedigree = []
        proband = self.init_proband()
        pro_parents = self.add_parents(proband)
        pro_fath = pro_parents[0]
        pro_moth = pro_parents[1]
        pro_siblings = self.add_siblings(proband)
        pro_fath_parents = self.add_parents(pro_fath)
        pro_moth_parents = self.add_parents(pro_moth)
        pro_fath_siblings = self.add_siblings(pro_fath)
        pro_moth_siblings = self.add_siblings(pro_moth)
        for person in pro_fath_parents:
            pedigree.append(person)
        for person in pro_moth_parents:
            pedigree.append(person)
        pedigree.append(pro_fath)
        pedigree.append(pro_moth)
        for person in pro_fath_siblings:
            pedigree.append(person)
        for person in pro_moth_siblings:
            pedigree.append(person)
        for person in pro_siblings:
            pedigree.append(person)
        pedigree.append(proband)
        return pedigree

##to debug make_healthy_pedigree
#x = 1
#while x <= 5:
#    new_ped = Pedigree()
#    pedigree = new_ped.make_healthy_pedigree()
#    for person in pedigree:
#        print person
#    x += 1

    def write_pedigree(self, pedigrees):
        '''
        Writes a list of pedigrees in output specific for BOADICEA 
        import to file pedigree.txt
        '''
        new_f = "pedigree.txt"
        my_pedigree = open(new_f, "w")
        my_pedigree.write("BOADICEA import pedigree file format 2.0 \n")
        headers = ["FamID", "Name", "Target", "IndivID", "FathID", "MothID",
                   "Sex", "Twin", "Dead", "Age", "Yob", "1BrCa",
                   "2BrCa", "OvCa", "ProCa", "PanCa", "Gtest", "Mutn",
                   "Ashkn", "ER", "PR", "HER2", "CK14", "CK56"]
        for item in headers:
             my_pedigree.write("%s\t" % item)
        my_pedigree.write("\n")
        for pedigree in pedigrees:
            for person in pedigree:
                for info in person:
                    my_pedigree.write("%s\t" % info)
                my_pedigree.write("\n")
        my_pedigree.close()
    
##to debug write_pedigree
#x = 1
#pedigrees = []
#while x <= 5:
#    new_ped = Pedigree()
#    pedigree = new_ped.make_healthy_pedigree()
#    pedigrees.append(pedigree)
#    x += 1
#w_ped = new_ped.write_pedigree(pedigrees)

class CancerPedigree(Pedigree):

    def sample_ca_inc(self, inc, age):
        '''
        inc: dictionary of cancer incidences key = age, value =
        incidence
        age: age to sample incidence

        Returns the probability of cancer incidence for a specific age
        '''
        if age < 40:
            prob = inc[30]/100
        elif age >=40 and age < 50:
            prob = inc[40]/100
        elif age >= 50 and age < 60:
            prob = inc[50]/100
        elif age >= 60 and age < 70:
            prob = inc[60]/100
        elif age >= 70:
            prob = inc[70]/100
        return prob

##to debug sample_ca_inc
#nc_br_ca_inc = {30:0.009, 40:0.040, 50:0.068, 60:0.092, 70:0.114}
#new_fam = CancerPedigree()
#x = 1
#while x <= 5:
#    age = random.randint(30, 90)
#    new_prob = new_fam.sample_ca_inc(nc_br_ca_inc, age)
#    print age, new_prob
#    x += 1

    def sample_mutn_inc(self, inc, age):
        '''
        inc: dictionary of mutation probabilites key = age, value =
        probability
        age: age to sample probability

        Returns the probability of a mutations for a specific age
        '''
        if age < 40:
            prob = inc[30]
        elif age >= 40 and age < 50:
            prob = inc[40]
        elif age >= 50 and age < 60:
            prob = inc[50]
        elif age >= 60 and age < 70:
            prob = inc[60]
        elif age >= 70:
            prob = inc[70]
        return prob

##to debug sample_mutn_inc
#brca1_br_inc = {30:0.051, 40: 0.016, 50:0.004, 60:0.002,
#                70:0.001}
#new_fam = CancerPedigree()
#x = 1
#while x <= 10:
#    age = random.randint(0,90)
#    new_prob = new_fam.sample_mutn_inc(brca1_br_inc, age)
#    print age, new_prob
#    x += 1

    def get_br_cancer(self, person):
        '''
        Randomly determines whether a person gets breast cancer using
        probabilites from Table 1 in Antoniou et al 2004

        Returns person information with age of 1st breast cancer
        diagnosis and age of 2nd breast cancer diagnosis if person does
        randomly gets breast cancer 
        '''
        nc_br_ca_inc = {30:0.009, 40:0.040, 50:0.068, 60:0.092,
                        70:0.114}
        brca1_br_ca_inc = {30:0.538, 40:1.021, 50:0.677, 60:0.450,
                           70:0.481}
        brca2_br_ca_inc = {30:0.375, 40:0.799, 50:1.484, 60:2.612,
                           70:3.591}
        sex = person[6]
        st_age = person[9]
        ca_age = 30
        br_ca1_status = person[11]
        br_ca2_status = person[12]
        mutn_status = person[17]
        if mutn_status == 0:
            while ca_age <= st_age:
                br_ca_prob = self.sample_ca_inc(nc_br_ca_inc, ca_age)
                chance = random.random()
                if chance < br_ca_prob:
                    if br_ca1_status == 0:
                        person[11] = ca_age
                    else:
                        if br_ca2_status == 0:
                            if br_ca1_status > ca_age:
                                person[12] = br_ca1_status
                                person[11] = ca_age
                            else:
                                person[12] = ca_age
                ca_age += 1
        elif mutn_status == 1:
            while ca_age <= st_age:
                br_ca_prob = self.sample_ca_inc(brca1_br_ca_inc, ca_age)
                chance = random.random()
                if chance < br_ca_prob:
                    if br_ca1_status == 0:
                        person[11] = ca_age
                    else:
                        if br_ca2_status == 0:
                            if br_ca1_status > ca_age:    
                                person[12] = br_ca1_status
                                person[11]= ca_age
                            else:
                                person[12] = ca_age
                ca_age += 1
        elif mutn_status == 2:
            while ca_age <= st_age:
                br_ca_prob = self.sample_ca_inc(brca2_br_ca_inc, ca_age)
                chance = random.random()
                if chance < br_ca_prob:
                    if br_ca1_status == 0:
                        person[11] = ca_age
                    else:
                        if br_ca2_status == 0:
                            if br_ca1_status > ca_age:
                                person[12] = br_ca1_status
                                person[11] = ca_age
                            else:
                                person[12] = ca_age
                ca_age += 1
        elif mutn_status == 3:
            while ca_age <= st_age:
                br_ca_prob = self.sample_ca_inc(brca1_br_ca_inc, ca_age)
                chance = random.random()
                if chance < br_ca_prob:
                    if br_ca1_status == 0:
                        person[11] = ca_age
                    else:
                        if br_ca2_status == 0:
                            if br_ca1_status > ca_age:
                                person[12] = br_ca1_status
                                person[11] = ca_age
                            else:
                                person[12] = ca_age
                ca_age += 1
        if sex == "M":
            person[11] = 0
            person[12] = 0
        return person

#to debug get_br_cancer
#new_fam = CancerPedigree()
#x = False
#y = False
#while x == False:
#    while y == False:
#        new_person = new_fam.init_proband()
#        get_cancer = new_fam.get_br_cancer(new_person)
#        has_ca1 = new_person[11]
#        if has_ca1 > 0:
#           y = True
#           print get_cancer
#    get_ca2 = new_fam.get_br_cancer(new_person)
#    has_ca2 = new_person[12]
#    if has_ca2 > 0:
#        x = True
#        print get_ca2

    def get_ov_cancer(self, person):
        '''
        Randomly determines whether a person gets ovarian cancer using
        probabilities from Antoniou et al 2004

        Returns person information with age of ovarian cancer included
        if person gets ovarian cancer
        '''
        nc_ov_ca_inc = {30:0.004, 40:0.012, 50:0.031, 60:0.044,
                        70:0.048}
        brca1_ov_ca_inc = {30:0.021, 40:1.173, 50:0.813, 60:0.976,
                           70:0.100}
        brca2_ov_ca_inc = {30:0.022, 40:0.044, 50:0.462, 60:0.416,
                           70:0.100}
        sex = person[6]
        st_age = person[9]
        ca_age = 30
        ov_ca_status = person[13]
        mutn_status = person[17]
        if mutn_status == 0:
            while ca_age <= st_age:
                ov_ca_prob = self.sample_ca_inc(nc_ov_ca_inc,ca_age)
                chance = random.random()
                if chance < ov_ca_prob:
                    if ov_ca_status == 0:
                        person[13] = ca_age
                ca_age += 1
        elif mutn_status == 1:
            while ca_age <= st_age:
                ov_ca_prob = self.sample_ca_inc(brca1_ov_ca_inc, ca_age)
                chance = random.random()
                if chance < ov_ca_prob:
                    if ov_ca_status == 0:
                        person[13] = ca_age
                ca_age += 1
        elif mutn_status == 2:
            while ca_age <= st_age:
                ov_ca_prob = self.sample_ca_inc(brca2_ov_ca_inc, ca_age)
                chance = random.random()
                if chance < ov_ca_prob:
                    if ov_ca_status == 0:
                        person[13] = ca_age
                ca_age += 1
        elif mutn_status == 3:
            while ca_age <= st_age:
                ov_ca_prob = self.sample_ca_inc(brca1_ov_ca_inc, ca_age)
                chance = random.random()
                if chance < ov_ca_prob:
                    if ov_ca_status == 0:
                        person[13] = ca_age
                ca_age += 1
        if sex == "M":
            person[13] = 0
        return person

##to debug get_ov_cancer
#new_fam = CancerPedigree()
#x = False
#while x == False:
#    new_person = new_fam.init_proband()
#    ov_ca = new_fam.get_ov_cancer(new_person)
#    has_ov_ca = ov_ca[13]
#    if has_ov_ca > 0:
#        x = True
#        print ov_ca

    def get_founder_ca(self, pedigree):
        '''
        Given a pedigree selects pedigree founders and randomly gives
        breast and ovarian cancer given probabilites used in functions
        get_br_cancer and get_ov_cancer

        Returns a list of lists for all individuals in the original
        pedigree with updated information for the four founder individuals
        '''
        founders = pedigree[:4]
        founders_ca = []
        for founder in founders:
            br_ca = self.get_br_cancer(founder)
            ov_ca = self.get_ov_cancer(br_ca)
            founders_ca.append(ov_ca)
        for index in range(4):
            pedigree[index] = founders_ca[index]
        return pedigree
    
##to debug get_founder_ca
# x = CancerPedigree()
# y = False
# while y == False:
#     h_ped = x.make_healthy_pedigree()
#     founders = x.get_founder_ca(h_ped)
#     for person in founders:
#         if person[11] > 0 or person[13] > 0:
#             y = True
#             w_ped = x.write_pedigree([founders])

        
    def get_mutn_br(self, person):
        '''
        Determines whether an individual with breast cancer has a BRCA1
        or BRCA2 mutation using probailities from Antoniou et al 2004
        Table 2

        Returns a list of information for a given person including their
        updated mutation status
        '''
        br_brca1_prob = {30:0.051, 40:0.016, 50:0.004, 60:0.002,
                         70:0.001}
        br_brca2_prob = {30:0.050, 40:0.020, 50:0.015, 60:0.012,
                         70:0.008}
        ca_age = person[11]
        br_ca_status = person[11]
        mutn_status = person[17]
        brca1 = False
        brca2 = False
        if br_ca_status > 0:
            if mutn_status == 0:
                brca1_prob = self.sample_mutn_inc(br_brca1_prob, ca_age)
                chance1 = random.random()
                if chance1 < brca1_prob:
                    brca1 = True
                brca2_prob = self.sample_mutn_inc(br_brca2_prob, ca_age)
                chance2 = random.random()
                if chance2 < brca2_prob:
                    brca2 = True
                if brca1 == True and brca2 == True:
                    person[17] = 3
                    person[16] = "T"
                elif brca1 == True and brca2 == False:
                    person[17] = 1
                    person[16] = "T"
                elif brca1 == False and brca2 == True:
                    person[17] = 2
                    person[16] = "T"
                else:
                    person[17] = 0
            elif mutn_status == 1:
                brca2_prob = self.sample_mutn_inc(br_brca2_prob, ca_age)
                chance = random.random()
                if chance < brca2_prob:
                    person[17] = 3
                    person[16] = "T"
            elif mutn_status == 2:
                brca1_prob = self.sample_mutn_inc(br_brca1_prob, ca_age)
                chance = random.random()
                if chance < brca1_prob:
                    person[17] = 3
                    person[16] = "T"
            else:
                person[17] = 3
                person[16] = "T"
        return person

##to debug get_mutn_br
#new_ped = CancerPedigree()
#x = False
#while x == False:
#    new_person = new_ped.init_proband()
#    new_ca = new_ped.get_br_cancer(new_person)
#    new_mutn = new_ped.get_mutn_br(new_ca)
#    mutn_status = new_mutn[17]
#    if mutn_status > 0:
#        x = True
#        print new_mutn
                    
    def get_mutn_ov(self, person):
        '''
        Determines whether an individual with ovarian cancer has a BRCA1
        or BRCA2 mutation using the probabilites in Table 2 from
        Antoniou et al 2004

        Returns a list of information for the person including the
        updated mutations status
        '''
        ov_brca1_prob = {30:0.006, 40:0.082, 50:0.018, 60:0.013,
                         70:0.001}
        ov_brca2_prob = {30:0.008, 40:0.004, 50:0.016, 60:0.008,
                         70:0.001}
        ca_age = person[13]
        ov_ca_status = person[13]
        mutn_status = person[17]
        brca1 = False
        brca2 = False
        if ov_ca_status > 0:
            if mutn_status == 0:
                brca1_prob = self.sample_mutn_inc(ov_brca1_prob, ca_age)
                chance1 = random.random()
                if chance1 < brca1_prob:
                    brca1 = True
                brca2_prob = self.sample_mutn_inc(ov_brca2_prob, ca_age)
                chance2 = random.random()
                if chance2 < brca2_prob:
                    brca2 = True
                if brca1 == True and brca2 == True:
                    person[17] = 3
                    person[16] ="T"
                elif brca1 == True and brca2 == False:
                    person[17] = 1
                    person[16] = "T"
                elif brca1 == False and brca2 == True:
                    person[17] = 2
                    person[16] = "T"
                else:
                    person[17] = 0
            elif mutn_status == 1:
                brca2_prob = self.sample_mutn_inc(ov_brca2_prob, ca_age)
                chance = random.random()
                if chance < brca2_prob:
                    person[17] = 3
                    person[16] = "T"
            elif mutn_status == 2:
                brca1_prob = self.sample_mutn_inc(ov_brca1_prob, ca_age)
                chance = random.random()
                if chance < brca1_prob:
                    person[17] = 3
                    person[16] = "T"
            else:
                person[17] = 3
                person[16] = "T"
        return person

##to debug get_mutn_ov
#new_ped = CancerPedigree()
#x = False
#while x == False:
#    new_person = new_ped.init_proband()
#    new_ca = new_ped.get_ov_cancer(new_person)
#    new_mutn = new_ped.get_mutn_ov(new_ca)
#    mutn_status = new_mutn[17]
#    if mutn_status > 0:
#        x = True
#        print new_mutn

    def get_founder_mutns(self, ca_pedigree):
        '''
        Given a pedigree where the founders have cancer, randomly
        assigns mutations with the probabilites from the functions
        get_munt_br and get_mutn_ov for only the female founders in a
        pedigree

        Returns a list of lists of the information for each individual
        in the pedigree with updated mutation information for the two
        female founder individuals
        '''
        founders = ca_pedigree[:4]
        founder_mutns = []
        for founder in founders:
            sex = founder[6]
            if sex == "F":
                br_mutn = self.get_mutn_br(founder)
                ov_mutn = self.get_mutn_ov(br_mutn)
                founder_mutns.append(ov_mutn)
            else:
                founder_mutns.append(founder)
        for index in range(4):
            ca_pedigree[index] = founder_mutns[index]
        return ca_pedigree

##to debug get_founder_mutns
#x = CancerPedigree()
#y = False
#while y == False:
#    h_ped = x.make_healthy_pedigree()
#    ca_founders = x.get_founder_ca(h_ped)
#    mutn_founders = x.get_founder_mutns(ca_founders)
#    for person in mutn_founders:
#        if person [17] > 0:
#            y = True
#            w_ped = x.write_pedigree([mutn_founders])

    def pass_founder_mutn(self, founder, mutn_pedigree):
        '''
        Given arguements of a specific founder with a mutation and a
        pedigree with a mutation returns a list of individuals with the
        founder mutation having a 50% chance of passing to the next
        generation
        '''
        founder_id = founder[3]
        founder_mutn = founder[17]
        for person in mutn_pedigree:
            moth_id = person[5]
            fath_id = person[4]
            if founder_id == moth_id or founder_id == fath_id:
                prob_pass = 0.5
                chance = random.random()
                if chance < prob_pass:
                    person[17] = founder_mutn
                    person[16] = "T"
        return mutn_pedigree

##to debug pass_founder_mutn
#new_ped = CancerPedigree()
#x = False
#while x == False:
#    h_pedigree = new_ped.make_healthy_pedigree()
#    ca_pedigree = new_ped.get_founder_ca(h_pedigree)
#    mutn_pedigree = new_ped.get_founder_mutns(ca_pedigree)
#    for person in mutn_pedigree:
#        if person[17] > 0:
#            founder = person
#            pass_mutn = new_ped.pass_founder_mutn(founder,
#                                                  mutn_pedigree)
#            length = len(pass_mutn)
#            if pass_mutn[1][17] > 0:
#                if pass_mutn[length-1][17] > 0:
#                    x = True
#                    w_mutn_ped = new_ped.write_pedigree([pass_mutn])

    def make_ca_pedigree(self, mutn_pedigree):
        '''
        Returns a pedigree where family members randomly have
        cancer given a pedigree where founders have been randomly
        assigned cancer and mutations
        
        Returns a list of lists with each list containing information
        for an individual in the format used in the
        make_healthy_pedigree function
        '''
        cancer_pedigree = []
        founders = mutn_pedigree[:4]
        for founder in founders:
            cancer_pedigree.append(founder)
        wo_founders = mutn_pedigree[4:]
        for person in wo_founders:
            sex = person[6]
            if sex == "F":
                br_ca = self.get_br_cancer(person)
                ov_ca = self.get_ov_cancer(br_ca)
                cancer_pedigree.append(ov_ca)
            else:
                cancer_pedigree.append(person)
        return cancer_pedigree

##to debug make_ca_pedigree
#x = False
#while x == False:
#    new_ped = CancerPedigree()
#    h_ped = new_ped.make_healthy_pedigree()
#    founder_ca = new_ped.get_founder_ca(h_ped)
#    founder_mutns = new_ped.get_founder_mutns(founder_ca)
#    founders = []
#    for person in founder_mutns:
#        if person[17] > 0:
#            founders.append(person)
#    if len(founders) > 0:
#        for person in founders:
#            pass_mutn = new_ped.pass_founder_mutn(person,founder_mutns)
#        ca_ped = new_ped.make_ca_pedigree(pass_mutn)
#        wo_founders = ca_ped[4:]
#        for person in wo_founders:
#            if person[11] > 0 or person[13] > 0:
#                x = True
#                w_ca_ped = new_ped.write_pedigree([ca_ped])
 
    def get_family_history(self, ca_pedigree):
        '''
        Computes summary family history for the proband in a pedigree
        and returns a list in the following order (variable descriptions
        also specified  after colon:
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
        '''
        family_hx = []
        ped_length = len(ca_pedigree)
        proband = ca_pedigree.pop(ped_length-1)
        fam_id = proband[0]
        ind_id = proband[3]
        first_deg_rels = []
        m_second_deg_rels = []
        p_second_deg_rels = []
        pro_fath_parents = ca_pedigree[:2]
        for person in pro_fath_parents:
            p_second_deg_rels.append(person)
        pro_moth_parents = ca_pedigree[2:4]
        for person in pro_moth_parents:
            m_second_deg_rels.append(person)
        pro_parents = ca_pedigree[4:6]
        for person in pro_parents:
            first_deg_rels.append(person)
        pro_fath_id = proband[4]
        pro_sibs = []
        for person in ca_pedigree:
            fath_id = person[4]
            if fath_id == pro_fath_id:
                pro_sibs.append(person)
        for person in pro_sibs:
            first_deg_rels.append(person)
        pro_fath_sibs = []
        pro_fath_fath_id = pro_fath_parents[0][3]
        for person in ca_pedigree:
            fath_id = person[4]
            person_id = person[3]
            if fath_id == pro_fath_fath_id and person_id != pro_parents[0][3]:
                pro_fath_sibs.append(person)
        for person in pro_fath_sibs:
            p_second_deg_rels.append(person)
        pro_moth_sibs = []
        pro_moth_fath_id = pro_moth_parents[0][3]
        for person in ca_pedigree:
            fath_id = person[4]
            person_id = person[3]
            if fath_id == pro_moth_fath_id and person_id != pro_parents[1][3]:
                pro_moth_sibs.append(person)
        for person in pro_moth_sibs:
            m_second_deg_rels.append(person)
        fhx = 1
        br_ca_ls = 0
        br_ca_gr = 0
        ov_ca = 0
        for person in first_deg_rels:
            br_ca_status = person[11]
            ov_ca_status = person[13]
            if br_ca_status > 0 and br_ca_status < 50:
                br_ca_ls += 1
            if br_ca_status >= 50:
                br_ca_gr += 1
            if ov_ca_status > 0:
                ov_ca += 1
        m2_br_ca = 0
        m2_ov_ca = 0
        for person in m_second_deg_rels:
            br_ca_status = person[11]
            ov_ca_status = person[13]
            if br_ca_status > 0:
                m2_br_ca += 1
            if ov_ca_status > 0:
                m2_ov_ca += 1
        p2_br_ca = 0
        p2_ov_ca = 0
        for person in p_second_deg_rels:
           br_ca_status = person[11]
           ov_ca_status = person[13]
           if br_ca_status > 0:
               p2_br_ca += 1
           if ov_ca_status > 0:
               p2_ov_ca += 1
        male_br_ca = 0
        pan_ca = 0
        var_list = [fam_id, ind_id, fhx, br_ca_ls, br_ca_gr, ov_ca, m2_br_ca,
                    p2_br_ca, m2_ov_ca, p2_ov_ca, male_br_ca, pan_ca]
        for var in var_list:
            family_hx.append(var)
        ca_pedigree.append(proband)
        return family_hx

##to debug get_family_hx
#x = False
#while x == False:
#    new_ped = CancerPedigree()
#    h_ped = new_ped.make_healthy_pedigree()
#    founder_ca = new_ped.get_founder_ca(h_ped)
#    founder_mutns = new_ped.get_founder_mutns(founder_ca)
#    founders = []
#    for person in founder_mutns:
#        if person[17] > 0:
#            founders.append(person)
#    if len(founders) > 0:
#        for person in founders:
#            pass_mutn = new_ped.pass_founder_mutn(person,
#                                                  founder_mutns)
#        ca_ped = new_ped.make_ca_pedigree(pass_mutn)
#        wo_founders = ca_ped[4:]
#        for person in wo_founders:
#            if person[11] > 0 or person[13] > 0:
#                x = True
#                fam_hx = new_ped.get_family_history(ca_ped)
#                w_ped = new_ped.write_pedigree([ca_ped])
#                print fam_hx

    def write_family_history(self, fam_hxs):
        '''
        Write family history information for multiple families given
        list of family histories and output information to file 
        familyhistory.txt 
        '''
        new_f = "familyhistory.txt"
        my_hx = open(new_f, "w")
        my_hx.write("Summary family history information \n")
        headers = ["FamID", "ProID", "FamHx", "ls1BrCa", "gr1BrCa", "1OvCa", "m2BrCa",
                   "p2BrCa", "m2OvCa", "p2OvCa", "maleBr", "PanCa"]
        for item in headers:
            my_hx.write("%s\t" % item)
        my_hx.write("\n")
        for fam in fam_hxs:
            for value in fam:
                my_hx.write("%s\t" % value)
            my_hx.write("\n")
        my_hx.close()

##to debug write_family_history
#x = False
#while x == False:
#    new_ped = CancerPedigree()
#    h_ped = new_ped.make_healthy_pedigree()
#    founder_ca = new_ped.get_founder_ca(h_ped)
#    founder_mutns = new_ped.get_founder_mutns(founder_ca)
#    founders = []
#    for person in founder_mutns:
#        if person[17] > 0:
#            founders.append(person)
#    if len(founders) > 0:
#        for person in founders:
#            pass_mutn = new_ped.pass_founder_mutn(person,
#                                                  founder_mutns)
#        ca_ped = new_ped.make_ca_pedigree(pass_mutn)
#        wo_founders = ca_ped[4:]
#        for person in wo_founders:
#            if person[11] > 0 or person[13] > 0:
#                x = True
#                fam_hx = new_ped.get_family_history(ca_ped)
#                w_ped = new_ped.write_pedigree([ca_ped])
#                w_hx = new_ped.write_family_history([fam_hx])


#simulation
def run_simulation(num_trials):
    '''
    Runs pedigree simulation for number of trials specified

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
    '''
    pedigrees = []
    x = 1
    while x <= num_trials:
        new_ped = CancerPedigree()
        h_ped = new_ped.make_healthy_pedigree()
        founder_ca = new_ped.get_founder_ca(h_ped)
        founder_mutns = new_ped.get_founder_mutns(founder_ca)
        founders = []
        for person in founder_mutns:
            if person[17] > 0:
                founders.append(person)
        if len(founders) > 0:
            for person in founders:
                pass_mutn = new_ped.pass_founder_mutn(person, founder_mutns)
            ca_ped = new_ped.make_ca_pedigree(pass_mutn)
            pedigrees.append(ca_ped)
        else:
            ca_ped = new_ped.make_ca_pedigree(founder_mutns)
            pedigrees.append(ca_ped)
        x += 1
    new_sim = Pedigree()
    w_ped = new_sim.write_pedigree(pedigrees)
    return pedigrees

#run_simulation(500)            

def run_ca_sims(num_trials):
    '''
    Does the same thing as the function run simulation but only
    returns pedigrees where at least one family member has a mutation
    
    Runs very slowly due to small probability of developing mutation
    if an individual develops cancer
    '''
    pedigrees = []
    x = 1
    while x <= num_trials:
        new_ped = CancerPedigree()
        h_ped = new_ped.make_healthy_pedigree()
        founder_ca = new_ped.get_founder_ca(h_ped)
        founder_mutns = new_ped.get_founder_mutns(founder_ca)
        founders = []
        for person in founder_mutns:
            if person[17] > 0:
                founders.append(person)
        if len(founders) > 0:
            for person in founders:
                pass_mutn = new_ped.pass_founder_mutn(person,
                                                founder_mutns)
            ca_ped = new_ped.make_ca_pedigree(pass_mutn)
            pedigrees.append(ca_ped)
            x += 1
    new_sim = Pedigree()
    w_ped = new_sim.write_pedigree(pedigrees)
    return pedigrees

#run_ca_sims(5)

