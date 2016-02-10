<!DOCTYPE HTML>
<html>
<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
    <title>{{title}}</title>
    <script type="text/javascript" src="javascript/jquery-1.8.2.min.js"></script>
    <script type="text/javascript" src="javascript/jquery.form.js"></script>
    <script type="text/javascript" src="javascript/jquery.validate.min.js"></script>
    <script type="text/javascript" src="javascript/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="javascript/bootstrap.min.js"></script>
    <script type="text/javascript" src="javascript/bootstrap-modal.js"></script>
    <script type="text/javascript" src="javascript/highcharts.js"></script>
    <script type="text/javascript" src="javascript/doublespec_plot.js"></script>

<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="css/bootstrap-responsive.min.css">
<link rel="stylesheet" href="css/busy.css">

<style type="text/css">
#gen_s2n { width: 1000px; }
#gen_s2n label { width: 150px; }
#gen_s2n th { background: #d9edf7 }
#gen_s2n label.error, #gen_s2n input.submit { margin-left: 5px; }
</style>


</head>
<body>
%include

<div class="row">
  <div class="span2"  id="bysy_indicator">Computing ...</div>
</div>
<div class="row">
  <div class="span2">
  <input id="s2nbtn" type="submit" class="button btn-primary"
    value="Show signal to noise"/>
    </div>
  <div class="span2">
  <input id="ctsbtn" type="submit" class="button btn-primary"
    value="Show counts"/>
  </div>
  <div class="span2 offset1">
  <input id="ctstabbtn" type="submit" class="button btn-primary"
     value="Show table of counts"/>
  </div>
</div>
<div class="row ">
  <div id="expmeterdiv" class="span2"></div>
</div>
<div class="row ">
  <div   id="s2n" class="span11" style="width: 1000px"></div>
</div>
<div class="row ">
  <div  class="span11" id="cts" style="width: 1000px"></div>
</div>
<div class="row ">
  <div id="ctstabdiv" class="span11"></div>
</div>
 <div id="divtabdownload">

 </div>

 <hr>
 <p>Email comments, questions to <email>holden@ucolick.org</email></p>
</body>
</html>
