class Inst:
    def __init__(self):
        self.com = ""
        self.paramregexp = dict()
        self.prettyparam = dict()

    def make(self,name="kast"):

        self.com = "%s_calcs2n_wrapper,wave,s2n," %name
        if name == "kast" or name == "lris":

            self.paramregexp = dict(
                dichroic = r'(d|D)\d+',
                grating = r'\d+\/\d+',
                grism = r'\w\d+',
                mag = r'\d+\.?\d*',
                binning = r'\dx\d',
                slitwidth = r'\d\.?\d*',
                exptime = r'\d+\.?\d*',
                seeing = r'(\d\.?\d*|\.\d+)',
                airmass = r'\d\.?\d*',
                ffilter = r'\w+\.\w+',
                template = r'\w+\.\w+',
                mtype = r'\d',
                redshift = r'(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                dichroic = 'Dichroic',
                grating = 'Grating',
                grism = 'Grism',
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Slitwidth',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )

        elif name == "esi":

            self.paramregexp = dict(
                mag = r'\d+\.?\d*',
                binning = r'\dx\d',
                slitwidth = r'\d\.?\d*',
                exptime = r'\d+\.?\d*',
                seeing = r'(\d\.?\d*|\.\d+)',
                airmass = r'\d+\.?\d*',
                ffilter = r'\w+\.\w+',
                template = r'\w+\.\w+',
                mtype = r'\d',
                redshift = r'(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Slitwidth',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )
        elif  name == "apf":

            self.paramregexp = dict(
                mag = r'\d+\.?\d*',
                binning = r'\dx\d',
                slitwidth = r'\w',
                exptime = r'\d+\.?\d*',
                seeing = r'(\d\.?\d*|\.\d+)',
                airmass = r'\d+\.?\d*',
                ffilter = r'\w+\.\w+',
                template = r'\w+\.\w+',
                mtype = r'\d',
                redshift = r'(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Slitwidth',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )

        elif name == "hires":
            self.paramregexp = dict(
                mag = r'\d+\.?\d*',
                binning = r'\dx\d',
                slitwidth = r'\w\d',
                exptime = r'\d+\.?\d*',
                seeing = r'(\d\.?\d*|\.\d+)',
                airmass = r'\d+\.?\d*',
                ffilter = r'\w+\.\w+',
                template = r'\w+\.\w+',
                mtype = r'\d',
                redshift = r'(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Decker',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )

        elif name =="deimos":

            self.paramregexp = dict(
                grating = r'\d+\w',
                mag = r'\d+\.?\d*',
                cwave = r'\d+\.?\d*',
                binning = r'\dx\d',
                slitwidth = r'\d+\.?\d*',
                exptime = r'\d+\.?\d*',
                seeing = r'(\d\.?\d*|\.\d+)',
                airmass = r'\d+\.?\d*',
                ffilter = r'\w+\.\w+',
                template = r'\w+\.\w+',
                mtype = r'\d',
                redshift = r'(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                cwave = 'Central Wavelength',
                grating = 'Grating',
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Slitwidth',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )

        return self
