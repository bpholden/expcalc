function decide(exp) {
    $("#expmeterdiv").hide();
    if (exp !== null) {
	$("#expmeterdiv").show();
    }
}

function plotoptions(chart,resp) {
    var markings = [];
    if(resp.dich == "d46") {
	chart.xAxis[0].addPlotBand({
	    from: 4500,
	    to: 4700,
	    color: '#CCCCFF',
	    id: 'dichroic'
        });
    } else if (resp.dich == "d55") {
	chart.xAxis[0].addPlotBand({
	    from: 5400,
	    to: 5500,
	    color: '#FFCCCC',
	    id: 'dichroic'
        });
	
    }else if (resp.dich == "D560") {
	chart.xAxis[0].addPlotBand({
	    from: 5550,
	    to: 5650,
	    color:  '#CCCCFF',
	    id: 'dichroic'
        });
	
    }
}

function find_max(array) {

    var maxval = array[0][1];
    for (var i = 0; i < array.length; i++) {
	//	console.log(array[i][1]);
	if (array[i][1] > maxval) {
	    maxval = array[i][1];
	}
    }
    return (maxval);
}

function strip_resp(resp) {

    var wave = [];
    var s2n = [];
    for (var i = 0; i < resp.s2n.length; i++) {
	wave.push(resp.s2n[i][0]);
	s2n.push(resp.s2n[i][1]);
    }
    return s2n;
}


function showify(inarr) {
    $.map(inarr,function(n) {
	$(n).show();
    });

}
function hidify(inarr) {
    $.map(inarr,function(n) {
	$(n).hide();
    });

}


function showRequest(formData, jqForm, options) { 
    //       $(".btn").button({disabled: true})
    var queryString = $.param(formData); 
    //      alert("started here!");
    console.log('About to submit: \n\n' + queryString); 
    hidify(["#cts","#s2n","#s2nbtn","#ctsbtn","#ctstabbtn","#ctstabdiv","#ctsoverview","#expmeterdiv"]);
    $("#bysy_indicator").show();
    
    return true; 
}



// a whole lot of work happens in this function
function showResponse(resp, statusText, xhr, $form)  { 
	
    var bigdw = 2000;
    var smalldw = 1000;
    $("#bysy_indicator").hide();
    if (resp.errormsg) {
        alert(resp.errormsg);
    } else {
        if (resp.msg) {
	    alert(resp.msg);
        }
	if (resp.exp !== null) {
	    var t = parseFloat(resp.exp);
	    if ( t <= 0) {
		resp.exp = null;
	    } else {
		resp.exp = [resp.exp];
	    }
	}
	console.log(resp);

	var max_obj = null;
	resp.wave.unshift('Wavelength');
	resp.js2n.unshift('Signal to Noise');
// console.log(resp.wave);
// console.log(resp.js2n);
	// the s2n chart is built first
	var chart = c3.generate({
	    bindto: '#s2n',
	    data: {
		x : 'Wavelength',
		columns: [
		     resp.wave ,
		     resp.js2n
		],
		type : 'spline'
	    },
	    axis: {
                x: { 
                    label : {
			text : 'Wavelength (Angstrom)',
			position : 'outer-middle'
                    },
		    tick : {
			count : 11,
			culling : true,
			format : function (x) { return parseInt(x); }
		    }
		},
		y : {
                    label: {
			text: 'S/N per Pixel',
			position : 'outer-middle'
                    }
		}
	    }

	});
	resp.jobj.unshift('Obj Cts');
	resp.jsky.unshift('Sky Cts');
	resp.jnoise.unshift('Readnoise Cts');		
	
	// now we build the cts chart
	var ctschart = c3.generate({
	    bindto: '#cts',
	    data: {
		x : 'Wavelength',
		columns: [
		    resp.wave,
		    resp.jobj,
		    resp.jsky,
		    resp.jnoise
		],
		type : 'spline'
	    },
	    axis: {
                x: { 
                    label : {
			text : 'Wavelength (Angstrom)',
			position : 'outer-middle'
                    },
		    tick : {
			count : 11,
			culling : true,
			format : function (x) { return parseInt(x); }
		    }
		},
		y : {
                    label: {
			text: 'Electrons per pixel',
			position : 'outer-middle'
                    }
		}
	    }

	});
	    
	    
	// finally, we write up the table containing the counts
	// first we build a table with a $.html() call
	
    	$("#ctstabdiv").html('<table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="ctstab"></table>');
	// now we pass that table to dataTable along with the column definitions and a javascript array 
	// this array is all of the counts (as opposed to the plotted array in the pcts object,
	// which breaks the counts up by source, e.g., obj, sky, or detector noise)
	//
	// this single array gets dumped into the table.

	$("#ctstab").dataTable({
	    "aoColumns" : [
		{ "sTitle": "Wavelength (Angstroms)" },
		{ "sTitle": "Obj (Cts)" },
		{ "sTitle": "Sky (Cts)" },
		{ "sTitle": "RN (Cts)" },
		{ "sTitle": "S/N" }
	    ],
	    "aaData" : resp.cts,
	    "bPaginate" : false,
	    "bFilter" : false
	});
	    
        $("#ctstabdiv").hide(); // Once more, but with feeling
	$("#expmeterdiv").html('<table cellpadding="0" cellspacing="0" border="0" class="table table-striped table-bordered" id="expmeter"></table>');
	decide(resp.exp);
	$("#expmeter").dataTable({
	    "aoColumns" : [
		{ "sTitle": "Exposure Meter" }
	    ],
	    "aaData" : resp.exp,
	    "bPaginate" : false,
	    "bFilter" : false,
	    "bInfo" : false,
	    "bSort" : false,
	    "bLengthChange" : false,
	    "bAutoWidth" : false
	    
	});
	showify(["#ctsbtn","#s2n","#ctstabbtn"]);
    }
}

$(document).ready(function(){

    $("#bysy_indicator").hide();

    var options = {
        target: "#divtabdownload",
        dataType:     'JSON',
        beforeSubmit: showRequest,
        success:       showResponse 
    } ;
    $("#gen_s2n").ajaxForm(options);
    // $("#gen_s2n").validate();

    hidify(["#ctsbtn","#ctstabbtn","#s2nbtn","#cvsbtn","#expmeterdiv"]);

    $("#ctsbtn").click(function () {
	hidify(["#ctstabdiv","#ctsbtn","#s2n","#s2noverview","#cvsbtn"]);
	showify(["#cts","#ctsoverview","#s2nbtn","#ctstabbtn"]);
    });
    
    $("#s2nbtn").click(function () {
	hidify(["#cts","#s2nbtn","#ctsoverview","#ctstabdiv","#cvsbtn"]);
	showify(["#ctstabbtn","#ctsbtn","#s2n","#s2noverview"]);
    });

    $("#ctstabbtn").click(function () {
	hidify(["#cts","#s2n","#ctsoverview","#ctstabbtn","#s2noverview"]);
	showify(["#ctstabdiv","#ctsbtn","#s2nbtn","#cvsbtn"]);
    });

    $("#tabdownloadbtn").click( function () {
	var queryString = $('#gen_s2n').formSerialize();
	$("#divtabdownload").html('<iframe id="tabdownload" src="" style="display:none; visibility:hidden;"></iframe>')	;
	var turl = "tab_s2n";
	turl += "?" + queryString;
	console.log(turl);
	$("#tabdownload").attr("src",turl);
    });

    $("#gen_s2n").change( function () {
	hidify(["#ctsbtn","#ctstabbtn","#s2nbtn","#cvsbtn"]);	
	hidify(["#ctstabdiv","#cts","#s2n","#expmeterdiv"]);
    });
    
    $("#disp").tooltip({
	placement : "top",
	title : "Dispersive elements"
    });
    $("#obj").tooltip({
	placement : "top",
	title : "Object parameters"
    });
    $("#exp").tooltip({
	placement : "top",
	title : "Details of the exposure"
    });
    $("#ccd").tooltip({
	placement : "top",
	title : "Details on the CCD read out"
    });
    $("#binning").tooltip({
	placement : "top",
	title : "Spatial pixels by spectral pixels"
    });

});

