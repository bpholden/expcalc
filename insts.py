class inst:
    def __init__(self):
        self.com = ""
        self.paramregexp = dict()
        self.prettyparam = dict()

    def make(self,name="kast"):

        self.com = "%s_calcs2n_wrapper,wave,s2n," %name
        if name == "kast" or name == "lris":

            self.paramregexp = dict(
                dichroic = '(d|D)\d+',
                grating = '\d+\/\d+',
                grism = '\w\d+',
                mag = '\d+\.?\d*',
                binning = '\dx\d',
                slitwidth = '\d\.?\d*',
                exptime = '\d+\.?\d*',
                seeing = '(\d\.?\d*|\.\d+)',
                airmass = '\d\.?\d*',
                ffilter = '\w+\.\w+',
                template = '\w+\.\w+',
                mtype = '\d',
                redshift = '(\d\.?\d*|\.\d+)',
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
                mag = '\d+\.?\d*',
                binning = '\dx\d',
                slitwidth = '\d\.?\d*',
                exptime = '\d+\.?\d*',
                seeing = '(\d\.?\d*|\.\d+)',
                airmass = '\d+\.?\d*',
                ffilter = '\w+\.\w+',
                template = '\w+\.\w+',
                mtype = '\d',
                redshift = '(\d\.?\d*|\.\d+)',
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
                mag = '\d+\.?\d*',
                binning = '\dx\d',
                #                spatialbinning = '\d',
                #                spectralbinning = '\d',
                #                slitwidth = '\d\.?\d*',
                slitwidth = '\w',
                exptime = '\d+\.?\d*',
                seeing = '(\d\.?\d*|\.\d+)',
                airmass = '\d+\.?\d*',
                ffilter = '\w+\.\w+',
                template = '\w+\.\w+',
                mtype = '\d',
                redshift = '(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                mag = 'Mag',
                binning = 'CCD Binning',
                #                spatialbinning = 'Binning in Spatial Pixels',
                #                spectralbinning = 'Binning in Spectral Pixels',
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
                mag = '\d+\.?\d*',
                binning = '\dx\d',
                slitwidth = '\w\d',
                exptime = '\d+\.?\d*',
                seeing = '(\d\.?\d*|\.\d+)',
                airmass = '\d+\.?\d*',
                ffilter = '\w+\.\w+',
                template = '\w+\.\w+',
                mtype = '\d',
                redshift = '(\d\.?\d*|\.\d+)',
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
                grating = '\d+',
                mag = '\d+\.?\d*',
                cwave = '\d+\.?\d*',
                binning = '\dx\d',
                slitwidth = '\d+\.?\d*',
                # slitlength = '\d+\.?\d*',
                exptime = '\d+\.?\d*',
                seeing = '(\d\.?\d*|\.\d+)',
                airmass = '\d+\.?\d*',
                ffilter = '\w+\.\w+',
                template = '\w+\.\w+',
                mtype = '\d',
                redshift = '(\d\.?\d*|\.\d+)',
                )

            self.prettyparam = dict(
                cwave = 'Central Wavelength',
                grating = 'Grating',
                mag = 'Mag',
                binning = 'CCD Binning',
                slitwidth = 'Slitwidth',
                #                        slitlength = 'Slitlength',
                exptime = 'Exp. time',
                seeing = 'Seeing',
                airmass = 'Airmass',
                ffilter = 'Filter',
                template = 'Template',
                mtype = 'Mag. Type',
                redshift = 'Redshift',
                )

        return self




