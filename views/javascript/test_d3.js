function postdata(data1) {

    var maxval = 0,
    sampsize = 0;
    var label_array = new Array(),
    table_array = new Array(),
    val_array1 = new Array();
    
    console.log(data1);
    sampsize = data1.wave.length;
    console.log("sample size" + sampsize);

    for (var i=0; i < sampsize; i++) {
	label_array[i] = parseInt(data1.wave[i]);
	val_array1[i] = { x: label_array[i], y: parseFloat(data1.s2n[i][1]) };
	table_array[i] =[ label_array[i], parseFloat(data1.s2n[i][1]), parseFloat(data1.obj[i][1]) ]
	maxval = Math.max(maxval, parseFloat(data1.s2n[i][1]) );
    }
    maxval = (1 + Math.floor(maxval / 10)) * 10;   
//    console.log(label_array);
//    console.log(val_array1);
    var  w = 750,
    h = 400,
    p = 30,
    x = d3.scale.linear().domain([ label_array[0], label_array[sampsize-1] ]).range([0, w]),
    y = d3.scale.linear().domain([0, maxval]).range([h, 0]);
    
    var vis = d3.select("#s2n")
	.data([val_array1])
	.append("svg:svg")
	.attr("width", w + p * 2)
	.attr("height", h + p * 2)
	.append("svg:g")
	.attr("transform", "translate(" + p + "," + p + ")");
    
   var rules = vis.selectAll("g.rule")
	.data(x.ticks(15))
	.enter().append("svg:g")
	.attr("class", "rule");
    
    // Place axis tick labels
    rules.append("svg:text")
	.attr("x", x)
	.attr("y", h + 15)
	.attr("dy", ".71em")
	.attr("text-anchor", "middle")
	.text(x.tickFormat(10))
	.text(String);
    
    rules.append("svg:text")
	.data(y.ticks(12))
	.attr("y", y)
	.attr("x", -10)
	.attr("dy", ".35em")
	.attr("text-anchor", "end")
	.text(y.tickFormat(5));
    

    // Series I
    vis.append("svg:path")
	.attr("class", "line")
	.attr("fill", "none")
	.attr("stroke", "maroon")
	.attr("stroke-width", 4)
	.attr("d", d3.svg.line()
              .x(function(d) { return x(d.x); })
              .y(function(d) { return y(d.y); }));
    
    
    // -----------------------------
    // Add Title then Legend
    // -----------------------------
    vis.append("svg:text")
	.attr("x", w/4)
	.attr("y", 20)
	.text("S/N as a function of Wavelength");

    var tr = d3.select("#ctstab").append("table").selectAll("tr")
	.data(table_array)
	.enter().append("tr");
    
    $("#ctstab").children().attr("class","table table-condensed table-bordered");

    var td = tr.selectAll("td")
	.data(function(d) { return d; })
	.enter().append("td")
	.text(function(d) { return d; });

} 

$(document).ready(function(){

//    var furl = 'http://etc.ucolick.org/web_s2n/gen_inst_s2n';
    var furl = 'gen_inst_s2n';

// airmass	1.1
// exptime	1200.0
// ffilter	sdss_r.dat
// inst	apf
// mag	13.0
// mtype	2
// redshift	0.0
// seeing	1.2
// slitwidth	2.0
// spatialbinning	1
// spectralbinning	1

    var indata = {seeing : 1.2,
		  slitwidth : 2.0,
		  airmass : 1.1,
		  redshift : 0.0,
		  mtype : 2,
		  slitwidth : 2.0,
		  inst : 'apf',
		  mag : 13,
		  redshift : 0.0,
		  spatialbinning : 1,
		  exptime : 1200.,
		  spectralbinning : 1,
		  ffilter : 'sdss_r.dat',
		  template : 'A0V_pickles_9.fits'};

    $.ajax({url: furl,
	    data : indata,
	    type : "POST",
	     beforeSend: function () {
		 console.log("posting");
		 console.log(indata);
	    },
	    success: postdata,
	    error : function (data,text,error) {
		alert(data);
		console.log(data);
		alert(text);
		alert(error);
	    }

	   });


});