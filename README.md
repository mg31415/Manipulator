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
<h1 id="kinematic-diagram">Kinematic diagram</h1>
<figure>
<img src="diagram.jpg" id="diagram" alt="" /><figcaption>kinematics chain diagram.</figcaption>
</figure>
<h1 id="degrees-of-freedom">Degrees of freedom</h1>
<p>The number of degrees of freedom of the manipulator can be calculated using Grübler’s formula which states:<br />
dof = m(N - 1 - J)+<span class="math inline">$\sum_{i=1}^{j} f_i$</span><br />
where N=5 links, as ground is also regarded as a link, J = 4 joints, m = 6 for spatial mechanisms, and the sum of freedoms provided by each joint= 4<br />
Hence, the degrees of freedom(dof) = 4</p>
<h1 id="denavithartenberg-parameters">Denavit–Hartenberg parameters</h1>
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
<img src="TM.png" id="TM" alt="" />
<h1 id="visualization">visualization </h1>
<p> Now that we have the DH paramters  we can easily derive the transformation matrices with some numpy arrays and then we can visualize the frames as a 3d scatter plot using plotly. </p>
<img src="viz.png" id="viz" alt="" />


<h1 id="control">Control</h1>
<h2 id="manual-control">Manual control</h2>
<p>1- On rasppery-pi 3 using Tkinter GUI we can control each joint to get the desired position and orientation , or choose  specific point in space or even make incremental changes in the coordinates <br />
  
2- On arduino using potentiometers mounted on a small 3d printed manipulator model.</p>
<h1 id="references">References</h1>
<p><span>[1]</span> F. C. Park., K. M. Lynch INTRODUCTION TO ROBOTICS MECHANICS, PLANNING, AND CONTROL.<br />
<span>[2]</span> Sodemann, A. Robotics1. Retrieved from <a href="http://www.robogrok.com./Robotics_1.php">http://www.robogrok.com./Robotics_1.php</a></p>
</body>
</html>
