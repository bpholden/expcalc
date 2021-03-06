%rebase test_c3 title='Levy on the APF Exposure Time Calculator'
<div class="container">
<div class="navbar">
  <div class="navbar-inner">
    <a class="brand" href="#">UCO/Lick Obs ETCs</a>
    <ul class="nav">
      <li class="active"><a href="apf">Levy on the APF</a></li>
      <li ><a href="hires">Hires</a></li>
      <li><a href="esi">ESI</a></li>
      <li><a href="kast">Kast</a></li>
      <li ><a href="lris">LRIS</a></li>
      <li><a href="deimos">DEIMOS</a></li>
    </ul>
  </div>
</div>

<div class="row">
  <h1>Levy on the APF Exposure Time Calculator </h1>
</div>
<form id="gen_s2n" method="post" action="gen_inst_s2n" class="form-stacked">
<table border="1" class="table span12">
  <thead>
    <tr>
      <th><center>Slit</center></th>
      <th><center>CCD</center></th>
      <th><center>Exposure</center></th>
      <th><center>Object</center></th>
    </tr>
    </thead>
  <tbody>
    <tr class>

      <td><label>Slitwidth:</label>
	<select name="slitwidth" class="singleselect" id="slitwidth">
	<option value="W">1.0 by 3.0 arcsec Decker W</option>
	<option value="T">2.0  by 3.0 arcsec Decker T</option>
	<option value="B">2.0 by 8.0 arcsec Decker B</option>
	<option value="M">1.0  by 8.0 arcsec Decker M</option>
	<option value="S">0.75  by 8.0 arcsec Decker S</option>
	<option value="N">0.5  by 8.0 arcsec Decker N</option>
	<option value="O">8.0  by 8.0 arcsec Decker O</option>	  
      </select>
    </td>
    <!-- <td><label>Binning:</label> -->
    <!--   <select name="spatialbinning" class="singleselect span2" id="binning"> -->
    <!-- 	<option value="1">1 spatial pix</option> -->
    <!-- 	<option value="2">2 spatial pix</option> -->
    <!-- 	<option value="3">3 spatial pix</option> -->
    <!-- 	<option value="4">4 spatial pix</option> -->
    <!--   </select> -->
    <!--   <select name="spectralbinning" class="singleselect span2" id="binning"> -->
    <!-- 	<option value="1">1 spectral pix</option> -->
    <!-- 	<option value="2">2 spectral pix</option> -->
    <!-- 	<option value="3">3 spectral pix</option> -->
    <!-- 	<option value="4">4 spectral pix</option> -->
    <!--   </select> -->
	<td><label>Binning:</label> <select name="binning"
	  class="singleselect input-medium" id="binning">
	  <option value="1x1">1x1 pixels</option>
	  <option value="2x2">2x2 pixels</option> 
	  <option value="4x4">4x4 pixels</option>
	  </select>
	  <p> Spatial by spectral.</p>
	</td>

    </td>
    <td><label class="fieldlabel">Exp. Time (seconds):</label>
      <input type="text" name="exptime" class="required number" id="form_exptime" value="1200.0" size="6"/><br/>
    </td>	
    <td><label class="fieldlabel">Mag</label>
      <input type="text" name="mag" class="required number" id="form_mag" value="9.0" size="4"/><br/>
      <select name="ffilter" id="ffilter"  class="singleselect input-mini">
% for i,f in enumerate(filters):
	<option value="{{f}}">{{fabbr[i]}}</option>   
% end
      </select>
      <select name="mtype" id="mtype" class="singleselect input-mini">
	<option value="2">AB</option>
	<option value="1">Vega</option>
      </select>
    </td>	
  </tr>
  <tr class>
    <td><input type="hidden" name="inst" value={{inst}} />
    </td>
    <td>
    </td>
    <td><label class="fieldlabel">Seeing (arcsec):</label>
      <input type="text" name="seeing" class="required number" id="form_seeing" value="1.2" size="4"/><br/>
    </td>	
	<td><label class="fieldlabel">Template</label>
	  <select name="template" id="template" class="singleselect input-medium">
% for i,t in enumerate(templates):
	    <option value="{{t}}">{{tabbr[i]}}</option>
% end
	  </select>
	</td>
  </tr>
  <tr class>
    <td>
    </td>
    <td>
    </td>
    <td><label class="fieldlabel">Airmass:</label>
      <input type="text" name="airmass" class="required number" id="form_airmass" value="1.1" size="4"/><br/>
    </td>	
       <td><label class="fieldlabel">Redshift:</label>
	 <input type="text" name="redshift" class="required number" id="form_airmass" value="0.0" size="4"/><br/>
	 </td>
  </tr>
</tbody>
</table>
<input type="submit" class="btn btn-primary" value="Compute exposure"/>
</form>

<input id="tabdownloadbtn" type="submit" class="btn btn-primary"
name="submitbutton" value="Return csv table for exposure"/>
<br/><br/>

<div class="row">
  <div class="span1">
<a class="btn btn-info" data-backdrop="true" data-keyboard="true"
    data-controls-modal="dialog">Help</a>
    </div>
</div>
<p>
<div class="modal hide" id="dialog">
<div class="modal-header">
  <a href="#" class="close">&times;</a>
  <h3>Help</h3>
</div>
<div class="modal-body">
  <p>This tool calculates the expected counts and signal to noise for a point source
  using the APF spectrograph. The throughput measurements are from a 8 by 8 arcsecond 
  aperture. The data are from September of 2015.</p>

<p>The input spectrum is one of the templates normalized by the
 specified Vega or AB magnitude in the specified filter.  A flat
 template means that the flux is distributed as either flat in
 frequency or the spectrum of Vega. The total flux of the object
 specified by the user will be reduced to account for slit losses
 based on the specified slit width, height, and seeing.  The target is
 assumed to be a point source with a PSF FWHM as specified by the
 seeing parameter. For APF, the slit depends on which Decker is
 used.</p>
  
  <p>The output data are given in units of per pixel.</p>

</div>

</div>
