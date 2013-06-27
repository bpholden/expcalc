%rebase layout title='KAST Exposure Time Calculator'
<div class="container">
<div class="navbar">
  <div class="navbar-inner">
    <a class="brand" href="#">UCO/Lick Obs ETCs</a>
    <ul class="nav">
      <li class="active"><a href="#">Kast</a></li>
      <li ><a href="lris">LRIS</a></li>
      <li><a href="esi">ESI</a></li>
      <li><a href="hires">Hires</a></li>
      <li><a href="deimos">DEIMOS</a></li>
      <li><a href="apf">APF</a></li>
    </ul>
  </div>
</div>

<div class="row"><h1 class="span6">KAST Exposure Time Calculator</h1></div>
<form id="gen_s2n" method="post" action="gen_inst_s2n"
class="form-stacked">
<table border="1" class="table span12">
<thead>
  <tr>
  <th id="disp"><center>Grating/Grism</center>
  </th>
  <th id="slit"><center>Slit</center>
  </th>
  <th id="ccd"><center>CCD</center>
  </th>
  <th id="exp"><center>Exposure</center> </th>
  <th id="obj"><center>Object</center></th>

</tr></thead>
<tbody>
<tr class>
  <td><span><label class="">Dichroic:</label> <select name="dichroic" class="singleselect" id="dichroic">
      <option value="d55">d55</option>
      <option value="d46">d46</option></select></span>
  </td>
  <td><label>Slitwidth:</label> <select name="slitwidth" class="singleselect" id="slitwidth">
      <option value="2.0">2.0 arcsec</option>
      <option value="1.0">1.0 arcsec</option>
      <option value="1.5">1.5 arcsec</option>
      </select>
  </td>
  <td id="binning"><label>Binning:</label> <select name="binning" class="singleselect" id="binning">
      <option value="1x1">1x1 pixels</option>
      <option value="2x1">2x1 pixels</option>
      <option value="2x2">2x2 pixels</option>
      <option value="3x1">3x1 pixels</option></select>
      <p>      Spatial by spectral.</p>
  </td>
  
<!--  <td><label>Binning:</label> <select name="binning" class="singleselect" id="binning">
      <option value="1x1">1x1</option>
      </select>
  </td>
//-->

<td><label class="fieldlabel">Exp. Time (seconds):</label>
<input type="textarea" name="exptime" class="required number" id="form_exptime" value="900.0" size="6"/><br/>
 </td>	

 <td><label class="fieldlabel" >Mag</label>
    <input type="textarea" name="mag" class="required number"
    id="form_mag" value="19.0" size="4"/>
   <select name="ffilter" id="ffilter"  class="singleselect input-mini">
% for i,f in enumerate(filters):
     <option value="{{f}}">{{fabbr[i]}}</option>   
% end
    </select>
    <select name="mtype" id="mtype" class="singleselect input-mini">
      <option value="2">AB</option>
      <option value="1">Vega</option>
    </select>

</tr>
<tr class>
  <td><label>Grism:</label> <select name="grism" class="singleselect" id="grism">
      <option value="G2">600/4310</option>
      <option value="G3">830/3460</option></select>
  </td>
  <td><input type="hidden" name="inst" value={{inst}} />
  </td>
  <td>
  </td>
<td><label class="fieldlabel">Seeing (arcsec):</label>
<input type="textarea" name="seeing" class="required number" id="form_seeing" value="1.5" size="4"/><br/>
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
  <td><label>Grating: </label><select name="grating" class="singleselect" id="grating">
      <option value="600/7500">600/7500</option></select>
  </td>
  <td>
  </td>
  <td>
  </td>
<td><label class="fieldlabel">Airmass:</label>
<input type="textarea" name="airmass" class="required number" id="form_airmass" value="1.1" size="4"/><br/>
 </td>	
       <td><label class="fieldlabel">Redshift:</label>
	 <input type="textarea" name="redshift" class="required number" id="form_airmass" value="0.0" size="4"/><br/>
	 </td>

</tr>
</tbody>
</table>
<input type="submit" class="button btn-primary" value="Compute exposure"/>
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
  <p>This tool calculates the expected signal to noise for a point source
  using the KAST spectrograph.  Currently, the user can only select two
  grisms, two dichroics and one grating.  As more data on the throughput
  of the instrument become available, more options will be added.</p>

<p>The input spectrum is one of the templates normalized by the
 specified AB magnitude in the specified filter.  The total flux of
 the object specified by the user will be reduced to account for slit
 losses based on the specified slit width, height, and seeing.  The
 target is assumed to be a point source with a PSF FWHM as specified
 by the seeing parameter. For KAST the slit is 120 arcseconds in
 length.</p>
  
  <p>The output data are given in units of per resolution element.</p>
  
</div>

</div>

