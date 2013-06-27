
def get_filters():
    filters = [
        "sdss_r.dat",
        "sdss_g.dat",
        "sdss_i.dat",
        "sdss_u.dat",
        "sdss_z.dat"]
    fabbr = ["r","g","i","u","z"]
    return(filters,fabbr)

def get_templates():
    
    tabbr = ["flat","S0","E","Orion","PNe","Sa","Sb","Sc",
             "starburst1","QSO","SNe Type 1a 10 days",
             "O5V","B5V","A0V","A5V","F5V","G5V","K0V","K5V","M5V"
             ]
    templates = ["",
        "s0_template.fits",
        "elliptical_template.fits",
        "orion_template.fits",
        "pn_template.fits",
        "sa_template.fits",
        "sb_template.fits",
        "sc_template.fits",	      
        "starb1_template.fits",
        "qso_template.fits",
        "sn1a10d_template.fits",
        "O5V_pickles_1.fits",
        "B5V_pickles_6.fits",
        "A0V_pickles_9.fits",
        "A5V_pickles_12.fits",
        "F5V_pickles_16.fits",
        "G5V_pickles_27.fits",
        "K0V_pickles_32.fits",
        "K5V_pickles_36.fits", 
        "M5V_pickles_44.fits"
        ]	      
    return(templates,tabbr)
