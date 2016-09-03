%rebase layout title='DEIMOS Exposure Time Calculator'
<div class="container">
<div class="navbar">
  <div class="navbar-inner">
    <a class="brand" href="#">UCO/Lick Obs ETCs</a>
    <ul class="nav">
      <li class="active"><a href="#">DEIMOS</a></li>
      <li><a href="hires">Hires</a></li>
      <li><a href="kast">Kast</a></li>
      <li ><a href="lris">LRIS</a></li>
      <li><a href="esi">ESI</a></li>
      <li><a href="apf">Levy on the APF</a></li>
    </ul>
  </div>
</div>

  <div class="row">
    <h1>DEIMOS Exposure Time Calculator</h1>
  </div>
  <form id="gen_s2n" method="post" action="gen_inst_s2n" class="form-stacked">
    <table border="1" class="table  span12">
      <thead><tr>
	<th><center>Grating</center></th>
	<th><center>Slit</center></th>
	<th><center>CCD</center></th>
	<th><center>Exposure</center></th>
	<th><center>Object</center></th>
      </tr></thead>
    <tbody>
      <tr class>
	<td><label>Grating: </label><select name="grating"
	  class="singleselect input-medium" id="grating">
	  <option value="600">600</option>
	  <option value="900">900</option>
	  <option value="1200">1200</option></select>
	</td>
	<td><label>Slitwidth:</label> <select name="slitwidth"
	  class="singleselect input-medium" id="slitwidth">
	  <option value="0.75">0.75 arcsec</option>
	  <option value="1.0">1.0 arcsec</option>
	  <option value="1.5">1.5 arcsec</option>
	 </select>
        </td>
	<td><label>Binning:</label> <select name="binning"
	  class="singleselect input-medium" id="binning">
	  <option value="1x1">1x1 pixels</option>
	  </select>
	  <p> Spatial by spectral.</p>
	</td>
	<td><label class="fieldlabel">Exp. Time (seconds):</label>
	  <input type="text" name="exptime" class="required number" id="form_exptime" value="1200.0" size="6"/><br/>
	</td>	

	<td><label class="fieldlabel" >Mag</label>
	  <input type="textbox" name="mag" class="required number"
	  id="form_mag" value="22.0" size="4"/>
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
	<td><label>Central Wavelength: </label><select name="cwave"
	    class="singleselect input-large" id="cwave">
	  <option value="7000">7000 Angstroms</option><option value="5000">5000 Angstroms</option>
	  <option value="6000">6000 Angstroms</option><option value="8000">8000 Angstroms</option>
	  </select>
	</td>
	<td><input type="hidden" name="inst" value={{inst}} />
	</td>
	<td></td>
       <td><label class="fieldlabel">Seeing (arcsec):</label>
	 <input type="text" name="seeing" class="required number" id="form_seeing" value="0.75" size="4"/><br/>
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
   <input type="submit" class="btn btn-primary" name="submitbutton"
   value="Compute exposure"/>
   </form>   
   <input id="tabdownloadbtn" type="submit" class="btn btn-primary"
   name="submitbutton" value="Return csv table for exposure"/>
<br/>
   <br/>
   
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

  <p>This tool calculates the expected counts and signal to noise for
  a point source using the DEIMOS spectrograph.  Currently, the user
  can only select three gratings at a fixed number of tilts.  As more
  data on the throughput of the instrument become available, more
  options will be added. The throughput measurements come from the
  data on the DEIMOS web pages at Keck Observatory</p>

  <p>The input spectrum is one of the templates normalized by the
 specified AB or Vega magnitude in the specified filter. A flat
 template means that the flux is distributed as either flat in
 frequency or the spectrum of Vega. The total flux of the
 object specified by the user will be reduced to account for slit
 losses based on the specified slit width, height, and seeing.  The
 target is assumed to be a point source with a PSF FWHM as specified
 by the seeing parameter.  For DEIMOS the slit is assumed to be 10
 arcseconds in length.</p>
  
  <p>The output data are given in units of per pixel.</p>

 </div>

 
</div>
