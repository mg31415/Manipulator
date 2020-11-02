<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <meta name="author" content="" />
 
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<header id="title-block-header">
<h1 class="title">Manipulator</h1>
<p class="author"></p>
</header>
<img src="imgs/manp.gif" id="manp" alt="" />

<h1 id="kinematic-diagram">Kinematic diagram</h1>
<figure>
<img src="imgs/diagram.jpg" id="diagram" alt="" /><figcaption>kinematics chain diagram.</figcaption>
</figure>

<h1 id="denavithartenberg-parameters">Denavit–Hartenberg parameters/caution this is for 4dof arm, haven't updated this yet</h1>
<p>Below table with the parameters, Where <span class="math inline"><em>θ</em></span> is the rotation around Z, d is the translation in Z, a is the translation in X, and <span class="math inline"><em>α</em></span> is rotation around X<br />
</p>
<table>
<thead>
<tr class="header">
<th style="text-align: center;">i</th>
<th style="text-align: center;"><span class="math inline"><em>θ</em><sub><em>i</em></sub></span></th>
<th style="text-align: center;"><span class="math inline"><em>d</em><sub><em>i</em></sub></span></th>
<th style="text-align: center;"><span class="math inline"><em>a</em><sub><em>i</em></sub></span></th>
<th style="text-align: center;"><span class="math inline"><em>α</em><sub><em>i</em></sub></span></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">1</td>
<td style="text-align: center;">q1</td>
<td style="text-align: center;">a1</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">90</td>
</tr>
<tr class="even">
<td style="text-align: center;">2</td>
<td style="text-align: center;">q2</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">a2</td>
<td style="text-align: center;">0</td>
</tr>
<tr class="odd">
<td style="text-align: center;">3</td>
<td style="text-align: center;">q3</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">90</td>
</tr>
<tr class="even">
<td style="text-align: center;">4</td>
<td style="text-align: center;">q4</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">a3+a4</td>
<td style="text-align: center;">0</td>
</tr>
</tbody>
</table>
<p><span>Angles are in degrees and displacements in mm</span></p>
<img src="imgs/TM.png" id="TM" alt="" />



<img src="imgs/viz.png" id="viz" alt="" />
<h1 id="Dependencies">Dependencies</h1>

  <p> run these command in your terminal or command line, if you don't have   <a href="https://pip.pypa.io/en/stable/installing/">pip</a>, install it first.
  <p> pip install numpy <br />
  <p> pip install pandas <br/>
  <p> pip install plotly<br/>
  <p> pip install pyfirmata <br/>
    
  <p> Make sure to change "from tkinter import *" to "from Tkinter import * " if you are using windows. <br/>

    
    
<h1 id="control">Control</h1>
<h2 id="manual-control">Manual control</h2>
<p>1- using pyFirmata's Python interface for the Firmata protocol i managed to control the arduino with tkinter GUI and control each joint to get the desired position and orientation, or choose  specific point in space or even make incremental changes in the coordinates.(IK not working yet) <br />
  
  <img src="imgs/gui.png" id="gui" alt="" />
  
<h1 id="electroni○s">electronics</h1>
<p> to spare myself the agony of connecting all these wires i made an arduino sheild for the servos </p>
 <img src="imgs/shield.jpg" id="shield" alt="" />

<h1 id="Resources">Resources</h1>
<p><span>[1]</span> F. C. Park., K. M. Lynch INTRODUCTION TO ROBOTICS MECHANICS, PLANNING, AND CONTROL.<br />
<span>[2]</span> Sodemann, A. Robotics1. Retrieved from <a href="http://www.robogrok.com./Robotics_1.php">http://www.robogrok.com./Robotics_1.php</a></p>
</body>
</html>
