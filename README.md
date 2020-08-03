<html>
<head>
<title>LaTeX4Web 1.4 OUTPUT</title>
<style type="text/css">
<!--
 body {color: black;  background:"#FFCC99";  }
 div.p { margin-top: 7pt;}
 td div.comp { margin-top: -0.6ex; margin-bottom: -1ex;}
 td div.comb { margin-top: -0.6ex; margin-bottom: -.6ex;}
 td div.norm {line-height:normal;}
 td div.hrcomp { line-height: 0.9; margin-top: -0.8ex; margin-bottom: -1ex;}
 td.sqrt {border-top:2 solid black;
          border-left:2 solid black;
          border-bottom:none;
          border-right:none;}
 table.sqrt {border-top:2 solid black;
             border-left:2 solid black;
             border-bottom:none;
             border-right:none;}
-->
</style>
</head>
<body>
\documentclass[12pt, onecolumn,compsoc]IEEEtran

\usepackagelipsum

\usepackageamsmath
\usepackagegraphicx
\usepackagefloat
\usepackagecite
\usepackage[hidelinks]hyperref


\title[something something] manipulator

\author\IEEEauthorblockNMahmoud Gamal
	\IEEEauthorblockA<br>
 <font size="-1"> Fayoum University</font><br>

		<font size="-1"> mg1488@fayoum.edu.eg</font>
	

\begindocument
	
\IEEEtitleabstractindextext	\beginabstract
	In this project we discuss the inverse kinematics of a 4 dof manipulator and various methods of controlling it then applying [idk yet] algorithm 
	\endabstract
	\beginIEEEkeywords
		Robotics, Manipulator, inverse kinematics.
\endIEEEkeywords
\maketitle
<p><hr>  
\tableofcontents
<p><hr>


<p><a name="toc.1"><h1>1&nbsp;Introduction</h1>  
the introduction is placed here


<p><a name="toc.2"><h1>2&nbsp;Kinematic diagram</h1>

\beginfigure[H]

	 <font face=symbol>Î</font> cludegraphics[width=\linewidth]diagram.jpg
	<font face=symbol>Ç</font>tionkinematics chain diagram.
	<a name="refdiagram">

	
\endfigure













<p><a name="toc.3"><h1>3&nbsp;Degrees of freedom</h1>   
The number of degrees of freedom of the manipulator can be calculated using Gr\"ubler’s formula which states: <br>

dof = m(N - 1 - J)+<font face=symbol>å</font><sub>i=1</sub><sup>j</sup>
</td>
<td nowrap align=center>
   f<sub>i</sub> <br>


where N=5 links, as ground is also regarded as a link, J = 4 joints,  m = 6 for spatial mechanisms, and the sum  of freedoms provided by each joint= 4<br>


Hence, the degrees of freedom(dof) = 4












<p><a name="toc.4"><h1>4&nbsp;Denavit–Hartenberg parameters</h1> 
Below table with the parameters<br>

Where <font face=symbol>q</font> is the rotation around Z, d the translation in Z, a the translation in X, 
and <font face=symbol>a</font> is rotation around X <br>
 
\begincenter
	\begintabular |c|c|c|c|c| 
		 \hline
		i & <font face=symbol>q</font><sub>i</sub> & d<sub>i</sub> & a<sub>i</sub> & <font face=symbol>a</font><sub>i</sub>  <br>
 
		\hline
		1 & q1 & a1 & 0 & 90 <br>
  
		2 & q2 & 0 & a2 & 0  <br>

		3 & q3 &  0 & a3 & ??  <br>

		4 & q4 &  0 & a4 & 0 <br>

		 \hline
		
	\endtabular
\endcenter
<font size="-1"> Angles are in degrees and displacements in mm</font>











<p><hr>
<p><a name="toc.5"><h1>5&nbsp;Workspace</h1>






<p><hr>
<p><a name="toc.6"><h1>6&nbsp;Control</h1>
<p><a name="toc.6.1"><h2>6.1&nbsp;Arduino based control</h2>
The simplest and first controlling method is by using potentiometers mounted on a small 3d printed manipulator model.






<p><hr>
<p><a name="toc.7"><h1>7&nbsp;References</h1>



[1] F. C. Park.,  K. M. Lynch INTRODUCTION TO ROBOTICS MECHANICS, PLANNING, AND CONTROL.<br>

[2] Sodemann, A. Robotics1. Retrieved from \urlhttp://www.robogrok.com./Robotics_1.php

    
\enddocument
<hr>
<p><h1>Table Of Contents</h1>
<p><a href="#toc.1"><h1>1&nbsp;Introduction</h1></a>
<p><a href="#toc.2"><h1>2&nbsp;Kinematic diagram</h1></a>
<p><a href="#toc.3"><h1>3&nbsp;Degrees of freedom</h1></a>
<p><a href="#toc.4"><h1>4&nbsp;Denavit–Hartenberg parameters</h1></a>
<p><a href="#toc.5"><h1>5&nbsp;Workspace</h1></a>
<p><a href="#toc.6"><h1>6&nbsp;Control</h1></a>
<p><a href="#toc.6.1"><h2>6.1&nbsp;Arduino based control</h2></a>
<p><a href="#toc.7"><h1>7&nbsp;References</h1></a>
</body>
</html>
