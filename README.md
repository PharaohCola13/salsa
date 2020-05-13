<a id="top"></a>
<div id="intro">
	<div class="collapsible">
		<div class="collapsible-header">
			<h2>Some Analysis for Looking at the Sun's Atmosphere</h2>
		</div>
		<div class="panel">
			<h3>Introduction</h3>
			This goal of this project is to observe the sun's upper atmosphere.
			To reach this objective, a refracting telescope is being converted into a
			solar coronagraph and then deployed to take images of the Sun.
			For more information about this instrument, visit the
			<a href='https://pharaohcola13.github.io/salsa/blind_eye'><i>Blind Eye</i>
			Documentation Page</a>.
		</div>
	</div>
</div>        
<div id="intro_sun">
	<div class="collapsible">
		<div class="collapsible-header">
				<h2>A review of solar coronagraphy</h2>
		</div>
		<div class="panel">
			<h3>Introduction</h3>
				<p>
					&emsp;The Sun is the primary energy source for the solar system and its dynamics are governed by gravitational forces and electromagnetic interactions. The Sun undergoes an eleven year oscillation of activity. During the maximum peak of this activity, sunspots form further away the equator in large amounts and magnetic field activity sparks an increase in flares accompanied by more X-ray and radio emissions (Weissman, 2006). As the minimum peak approaches, the sunspots drift towards the equator and the surface of the Sun is quieter.
					<br>
					&emsp;When the Sun transitions to a more active state, solar flares become more common. Flares are classified into three categories based on energy: C, M, and X (Jaggard, 2019). The low-energy C-class flares do not have a significant impact on the Earth and are usually only detected by coronagraphs in orbit or sensors tuned to observe X-ray emissions. The medium M-class flares can cause disruptions in electronics in orbit and minor solar storms. The high-energy class, X, can have a significant impact on global scales electronic, and high-intensity solar storms (Jaggard, 2019).
					<br>
					&emsp;Another solar event that is of interest are Coronal Mass Ejections *(CME)*, similar to flares, CMEs increase in frequency during solar maximum. These energetic events formed at active region magnetic fields and are composed of high-energy plasma (Murray, 2018; Waldmeier,1974). The commonly depicted loop structure of CMEs is explained in terms of flux ropes, volumetric plasma structure with the magnetic field lines wrapped around a central axis (Filippov, 2015; Gou, 2019). Large scale CMEs accelerate high-energy particles that can drive geomagnetic storms, and by interacting ith the Earth's magnetic field, can modulate galactic cosmic rays (Richardson, 2010).
				</p>
			<br>
			<h4>The solar atmosphere</h4>
				<p>
					&emsp;The surface of the Sun is a complex, high-energy environment that continuously emits solar radiation and ionized particles throughout the heliosphere. The atmosphere is an extension of the surface and is similarly comprised of high-energy, charged particles. The Sun's atmosphere is comprised of three primary layers: the chromosphere, the corona, and the solar winds.
					<br>
					&emsp;The atmosphere has a significant impact on photospheric phenomena. During solar maximum, images from an early spectroheliograph show that the structure of a sunspot resembles high-velocity vortexes of ionized particles produced from the solar atmosphere (Hale, 1925). We can also note the relationship between the surface and the solar winds. While stronger magnetic fields tend to be isolated near the surface by means of resisting the hydrodynamic expansion, the weaker fields can interact with the Earth and can reach into the distant regions of the heliosphere by means of the solar wind. (Parker, 1969) details how this phenomena can be analytically represented by defining the radial and the angular magnetic fields as
					<div lang="latex", style="text-align: center">
					B(r, \theta, \phi) = B \Big( \theta, \phi + \frac{r\Omega}{v} \Big) \Big( \frac{r\_0}{r} \Big)^2
					</div>
					<br>
					where <span lang="latex">\Omega</span> represents the angular velocity of the Sun, <span lang="latex">v</span> is the velocity of the radial winds, while <span lang="latex">\theta</span> and <span lang="latex">\phi</span> represent traditional polar and azimuthal angles.
				</p>
			<h5>The chromosphere</h5>
				<p>
					&emsp;The chromosphere is the lowest region of the solar atmosphere and contains a mixture of cool gas and hot plasma that is released from the surface. This region of the Sun's atmosphere has structure that is particularly difficult to observe directly with spectroscopic methods as a consequence of weak magnetic fields, the insensitive spectral lines broaden (Kontar, 2008). However, utilizing the magnetic field's interactions with X-rays it is possible to quantitatively define the loop structure (Kontar, 2008; Watko, 2000). For the purposes of this paper, we will not continue this discussion regarding the chromosphere, as this region is usually not the focus of observation for coronagraphs.
				</p>
			<h5>The corona</h5>
			    <p>
			        &emsp;The corona is the furthest part of the solar atmosphere and is the focus of observation for coronagraphs, as we will discuss in more detail later. The corona has also been observed elongated between 0.07 AU and 0.45 AU (Howard, 2019). There are three primary components associated with the corona, denoted by the letters: F, K, and L.
							<br>
							&emsp;The F-component is the outer portion of the corona and is a consequence of diffraction via interplanetary dust (Waldmeier, 1963). The dark absorption lines of the solar spectrum, Fraunhofer lines, are observed in this region unlike the K-corona. (Calbert, 1972) characterizes the light intensity of this region as a function of the elongation angle of corona <span lang="latex">\epsilon</span> as ,
							<div lang="latex", style="text-align:center">
								i(\epsilon) = E(\lambda)\iint\frac{\pi a^2}{r^2} n(r,a) I(\theta) dl da.
							</div><br>
							where <span lang="latex">E(\lambda)</span> is the total light radiated per steradian, <span lang="latex">a</span> is the radius of the interplanetary dust, <span lang="latex">r</span> is the distance between the dust particle and the center of the Sun, <span lang="latex">n(r,a)</span> defines the number of particles of the given radius between differential positions.
							<br>
							&emsp;The inner-most portion of the corona, the K-component, of the corona is caused by Thomson scattered solar radiation by free electrons (Waldmeier, 1963). As a consequence of the thermal motion of the electrons in the this region which generates a Doppler shift, the Fraunhofer lines are not present (Calbert, 1972).
							<br>
							&emsp;The L-component of the corona is comprised of line emissions originating from highly ionized atoms (Cooper, 1964). This particular aspect of the solar atmosphere can be observed at several arcminutes from the limb (Cooper, 1964), but only represents approximately one percent of coronal light (Waldmeier, 1963). For the purposes of this paper we will not completely explore this regions.
							<br>
							&emsp;Some other physical substructures associated with the corona include coronal holes and loops. Coronal holes are defined as regions of the solar corona that have reduced emissivity associated with the regional temperature line (Wiegelmann, 2004). Coronal loops, similar to CMEs, are structured by means of the flux ropes. However, the arching plasma is magnetically isolated from the surroundings (Reale, 2014).
			    </p>
			<h5>Solar winds</h5>
				<p>
					 &emsp;The solar wind has an far reaching influence in dynamical processes throughout the solar system. Focusing on the impact the winds have on the sun, we have seen that the weak magnetic fields can be extended by the winds which allows for interplanetary interaction. In addition, based upon the conservation of angular momentum the solar winds are responsible for removing angular momentum from the Sun.
				</p>
			<br>
			<h3>Operation and Design</h3>
				<p>
					&emsp;Coronagraphs are optical instruments that artificially create a total solar eclipse effect to observe the fainter, further out regions of the solar atmosphere. This eclipse effect is manufactured by either an internal or external occulting mechanism, such as a disk. As we will see, most coronagraphs, such as the High Altitude Observatory, use an external occulting disk.
					<br>
					&emsp;Internally occulting coronagraphs use internal optical suppression techniques to remove stray light that enters the aperture, while the externally occulting coronagraphs use a disk that resides near the aperture that will block out any of the direct light from the Sun.
				</p>
				<h4>Solar Coronagraphs</h4>
					<p>
						&emsp;Solar coronagraphs are utilized at looking at our Sun, rather than at distant star systems. The original design for a coronagraph included an external occulting disk with a planoconvex lens, ground from borosilicate crown glass, with diameter of twenty centimeters and a focal length of four meters (Lyot, 1939). The main tube was made from duralumin with a length of six meter which can be seen in <a href="#Lyot_corona">Figure 2</a>. In the original design it can be noted that there was a spectrograph integrated into the instrument. The imaging device that was used in this design was a simple camera, noted by R in <a href="#Lyot_corona">Figure 2</a>. From his design, by applying a orange filter and a "weak" eyepiece, Lyot stated that the innermost regions of the solar corona can be observed. One of the many products of the invention of the coronagraph was a mechanism called the Lyot Stop. This simple mechanism reduces the intensity of flare cause by the diffraction of other field stops in a optical system (Noll, 1973).
						<br>
						&emsp;The modern coronagraphs that we will look at include the High Altitude Observatory *(HAO)*, the Solar and Heliospheric Observatory *(SoHO)*, a probe with three coronagraphs on-board including one hybrid coronagraph, and the Solar Terrestrial Relations Observatory *(STeReO)*.
						<br>
						&emsp;The HAO has a focus on research pertaining to various disciplines of space science and solar physics. The telescope itself is, as mentioned before, a ground-based photometer with a Lyot design (Evans, 1948). The telescope is equipped with two externally occulting disks with a linear diameter analytically defined as
						<div lang="latex", style="text-align:center">
							O\_1 = 2\varphi d + a\_1,
						</div>
						<br>
						<div lang="latex", style="text-align:center">
							O\_2 = 2f\_1 ( \varphi + \frac{a\_1}{d} ).
						</div><br>
						where <span lang="latex">\varphi</span> is the angular radius of the sun *(usually about 0.0047 radians)*, <span lang="latex">d</span> is the distance between the first occulting disk and the aperture of diameter <span lang="latex">a\_1</span>, the focal length of the optical system is defined by <span lang="latex">f\_1</span> (Evans, 1948). The first occulting disk is used primarily to block out the direct sunlight, the second disk was applied early on to negate the effects of vignetting that became apparent during the initial tests of the coronagraph (Evans, 1948).
						<br>
						&emsp;The SoHO payload includes the Large Angle Spectroscopic Coronagraph *(LASCO)*; a collection of three coronagraphs labeled: C1, C2, and C3. Some of the basic properties of the three telescopes are included in Table 1. Each of the coronagraphs is equipped with a three-phase, front-side illuminated 1024 <span lang="latex">\times</span> 1024 pixel CCD imaging system (Brueckner, 1995).
					</p>
					<table>
						<tbody>
							<tr>
								<td>  </td>
								<td> Field of View <span lang="latex">(R\_{\odot})</span></td>
								<td>Pixel Size</td>
								<td>Brightness Range <span lang="latex">(B\_{\odot})</span></td>
							</tr>
							<tr>
								<td> C1 </td>
								<td lang="latex"> 1.1 - 3.0 </td>
								<td><span lang="latex">5.6</span>'' </td>
								<td lang="latex"> 2\times10^{-5} - 2\times10^{-8}</td>
							</tr>
							<tr>
								<td> C2 </td>
								<td lang="latex"> 1.5 - 6.0 </td>
								<td><span lang="latex"> 11.4 </span>'' </td>
								<td lang="latex"> 2\times10^{-8} - 5\times10^{-10}</td>
							</tr>
							<tr>
								<td> C3 </td>
								<td lang="latex"> 3.7 - 30 </td>
								<td><span lang="latex">56.0</span>'' </td>
								<td lang="latex">  3\times10^{-9} - 1\times10^{-11} </td>
							</tr>
						</tbody>
					</table>
					<p>*Table 1: Basic optical properties of the three coronagraphs on-board SoHO (Brueckner, 1995).*
					<p>
						 &emsp;The first of the three utilizes a series of mirrors and a piezoelectrically scanned Fabry-Perot interferometer (Brueckner, 1995). The Fabry-Perot interferometer, characterized by the following relationship (Pedrotti, 2019):
						 <div lang="latex", style="text-align:center">
						 		2nL = m\lambda\, ,
						 </div>
						 acts as a adjustable filter capable of capturing monochromatic images over the entire field-of-view. The series of mirrors produces a one-to-one real image of the initial aperture A0 onto the Lyot stop, denoted as A1 in <a href="#ray-c1">Figure 1</a>. The design of this instrument allows the full light of the Sun and corona to interact with the off-axis parabolic objective mirror noted as M1 in <a href="#ray-c1">Figure 1</a> (Brueckner, 1995).
						 <br>
						 &emsp;We can note from the comparison of the C2 and C3 coronagraphs in <a href="#lasco_c2">Figure 3</a>, that the design of the instruments are fundamentally similar. Both systems utilize field and Lyot stops to block diffracted light and both apply a internal occulting disk. The primary differences between the two coronagraphs are based on heat exposure and payload limitations. In the case of C2, the disk is actually a tapered cylinder with a polished screw thread, while C3 uses three circular disks on a common spindle, each of the disks are sized and spaced to allow more sunlight to be blocked on the edge of the previous (Brueckner, 1995).
						 <br>
						 &emsp;The final instrument that we will look at is STeReO. This orbital telescope contains two coronagraphs, the first has an internally occulting refractive Lyot design with a field of view of 1.3 to 4 <span lang="latex">R\_{\odot}</span> (Thompson, 2003). The second uses a three-disk external occulting mechanism and includes an objective lens group along, three apertures with a fourth acting as a Lyot stop, a spectra filter and a polarizer (Howard, 2008). The field of view for this instrument corresponds to a height of 15 <span lang="latex">R_{\odot}</span>.
					 </p>
					 <h4>Data collected from coronagraphs</h4>
					 &emsp;Coronagraphs produce image data from the equipped CCD systems. Before we can analyze the data collected from the coronagraphs, we can break down the sample data in <a href="#annotate">Figure 4</a>. Some of the standard characteristics of the coronagraph data is that the occulting disk is usually larger than the size of the Sun. It should be noted that there is a difference in the design specifications between the STeReO and the HAO, as we will see, and this difference can have a significant impact on the agreement between the telescopes.
					 <br>
					 &emsp;In this discussion we will examine some solar energetic events and see how they appear through the coronagraph. In <a href="#data_777">Figure 5</a> we can see a comparison between STeReO and the HAO coronagraphs on July <span lang="latex">7^{\text{th}}</span>, 2007, due to some maintenance on the LASCO historical database the three coronagraphs are not included in this comparison. In the data we can easily observe an energetic event in STeReO, and in fact this event was classified as a C-class solar flare. As we discussed, these types of solar flares are low-energy and is difficult to observe from the surface. This would explain why the HAO coronagraph was unable to record the flare while STeReO registered a significant event.
					 <br>
					 &emsp;The next data comparison will be between the STeReO and the LASCO C2 coronagraph. The event in <a href="#data_91017">Figure 6</a> is an X-class solar flare that occurred on September <span lang="latex">10^{\text{th}}</span>, 2017. Unlike the previous comparison between the HAO and STeReO, we can easily identify the flare in both images. Due to the intensity of the flare, if HAO data was available for this flare, we would likely see some substantial spike in intensity on the image. Something that is also interesting is the loop structure of the flare. This structure occurs when a large amount of solar material arcs with the magnetic field.
			 <h3>Applications</h3>
			 		&emsp; One of the primary goals of observing the Sun is to further understand and predict extreme solar events, such as Coronal Mass Ejections and solar flares. However, as a consequence of directing cameras and sensors at the Sun, we can observe comets and transits of planets to further understand properties of the outer regions of the solar system in addition to the inner-most planets.
					<h4>Space Weather Monitoring</h4>
						&emsp;One of the science goals for NASA's Heliophysics Division is to develop the capability to "predict extreme conditions in space to protect life and society and to safeguard human and robotic explores beyond Earth" (NASA, 2019). Although the well-being of crucial satellites in orbit is import, further understanding of severe solar events can help develop more robust safety procedures and redundancies here on the ground. As noted by (Weiss, 2019), the power grid in the United States is vulnerable to geomagnetic storms typically generated by solar activity. In more detail, the intense magnetic fields that are propagated along the path of the solar flare or CME interacts with the magnetosphere and ionosphere which can generate electromagnetic fields on the surface (Weiss, 2019).
						<br>
						&emsp;With the capability to develop an early warning system for extreme solar events would be able to take the necessary precautions to ensure that satellites in orbit and continental power grids are not significantly effected by the intense solar activity.
						<br>
						&emsp; After an extensive review by Richardson (2010), they state that CMEs can be predicted by unusually low solar wind proton temperatures in addition low solar wind charge states. They also admit that more data needs to be collected, since there have been few recorded CMEs.
					<h4>Planetary Science</h4>
						&emsp;Another interesting application of coronagraphs is comet tracking. Since the deployment of SoHO, there have been at least 3138 comets recorded (Battams, 2017). With the advantage of residing in the L1 Lagrange point, providing an unobstructed view of the Sun and its surroundings, the LASCO coronagraphs can observe comets and classify them based on their closest approach (Jones, 2017). The primary classification of comets that are observed by space-based coronagraph is the Kreutz group. This particular group are the only comets that are considered to be sungrazers.
				<h3>Conclusion</h3>
				&emsp;In conclusion, the coronagraphs provide a unique look into the Sun's dynamical process and provides insight into how the Sun interacts with the Earth and the outer solar system. We have seen some of the original design of the coronagraph as well as some of the more modern systems, each of them utilizing the similar mechanisms. The data that is collected from coronagraphs, observations severe solar events such as CMEs and solar flares as well as comets, can be used to explore the solar-terrestrial environment and better prepare countries around the world for impacts on electrical and telecommunication systems.
				<h3>Figures</h3>
				<div class="collapsible" style="width:100%" id="ray-c1">
					<div class="panel">
						<img src="https://i.ibb.co/0KYBCRP/ray-c1.png" style="display: block;margin-left:auto;margin-right: auto;width:100%" alt="ray-c1" border="0" width=500>
						<br>
						*Figure 1: Ray diagram of the LASCO C1, a mirror Lyot coronagraph. The mirrors are noted by M, the apertures A, the Fabry-Perot interferometer by F-P, and the polarizer and blocking filter are denoted as P and F, respectively (Brueckner, 1995).*
					</div>
				</div>
				<div class="collapsible"  style="width:100%" id="Lyot_corona">
					<div class="panel">
						<img src="https://i.ibb.co/9ZRspFJ/Lyot-corona.png" style="display: block;margin-left:auto;margin-right: auto;width:100%" alt="Lyot-corona" border="0">
						<br>
						*Figure 2: Final design of the coronagraph developed by Lyot in 1938 (Lyot, 1939).*
						</div>
				</div>
				<div class="collapsible" style="width:100%" id="lasco_c2">
					<div class="panel">
						<div style="display: block; margin-left: 5%; margin-right: 5%;">
							<img src="https://i.ibb.co/4pLSZDz/lasco-c2.png" style="margin-left:auto;margin-right: auto;width:49%" alt="lasco-c2" border="0">
							<img src="https://i.ibb.co/pzwPSPX/lasco-c3.png" style="margin-left:auto;margin-right: auto;width:50%" alt="lasco-c3" border="0">
						</div>
						<br>
						*Figure 3: Schematic diagrams of the LASCO C2 (left) and C3 (right) systems. Although they appear very different in their design and structure, the two devices utilize a primary external occulting disk as well as a secondary internal disk as well as various types of Stops in a similar fashion (Brueckner, 1995).*
					</div>
				</div>
				<div class="collapsible" style="width:100%" id="annotate">
					<div class="panel">
						<img src="https://i.ibb.co/S5Hv0B1/annotate.png" style="display: block;margin-left:auto;margin-right: auto;width:45%" alt="annotate" border="0" width=250>
						<br>
						*Figure 4: An annotated images of the visual output from SoHO. We can easily identify the occulting disk as well as the Coronal Mass Ejection, all noted in white.*
					</div>
				</div>
				<div class="collapsible" style="width:100%" id="data_777">
					<div class="panel">
						<div style="display: block; margin-left: 15%; margin-right: 10%;">
							<img src="https://i.ibb.co/dGfsRzG/hao-777.jpg" style="width:45%" alt="hao-777" border="0">
							<img src="https://i.ibb.co/Prg4T66/stereo-777.jpg" style="width:45%" alt="stereo-777" border="0">
						</div>
						<br>
						*Figure 5: A C-class solar flare, recorded in July 2007, as seen from STeReO (left) and HAO (right), we can make note that the distinct designs and the atmospheric effects produce two unique views on the solar flare.*
					</div>
				</div>
				<div class="collapsible" style="width:100%" id="data_91017">
					<div class="panel">
							<div style="display: block; margin-left: 15%; margin-right: 10%;">
								<img src="https://i.ibb.co/Sc3wQXN/soho-91017.png" style="margin-left:auto;margin-right: auto;width:45%" alt="soho-91017" border="0">
								<img src="https://i.ibb.co/mzTBNwG/stereo-91017.jpg" style="margin-left:auto;margin-right: auto;width:45%" alt="stereo-91017" border="0">
							</div>
						<br>
						*Figure 6: An X-class solar flare imaged by STeReO (left) and SoHO (right) on September 2017. The loop structure can be clearly observed in both images. It can also be noted that the different perspectives is the cause of the flipped images.*
					</div>
				</div>
		</div>
	</div>
</div>
<div id="references">
	<div class="collapsible">
		<div class="collapsible-header">
			<h2>References</h2>
		</div>
		<div class="panel">
		<p><a name="Calbert_1972"></a>
		Roosevelt Calbert and David&nbsp;B. Beard.
		 The F and K Components of the Solar Corona.
		 <em></em>, 176:497, September 1972.
		[<a href="http://dx.doi.org/10.1086/151652">DOI</a>&nbsp;]
		</p>
		<p><a name="Hale_1925"></a>
		George&nbsp;E. Hale and Seth&nbsp;B. Nicholson.
		 The Law of Sun-Spot Polarity.
		 <em></em>, 62:270, November 1925.
		[<a href="http://dx.doi.org/10.1086/142933">DOI</a>&nbsp;]
		</p>
		<p><a name="Waldmeier_1963"></a>
		M.&nbsp;Waldmeier.
		 Slow Variations of the Solar Corona.
		 In John&nbsp;Wainwright Evans, editor, <em>The Solar Corona</em>, volume&nbsp;16
		  of <em>IAU Symposium</em>, page 129, January 1963.
		</p>
		<p><a name="Lyot_1939"></a>
		Bernard Lyot.
		 The study of the solar corona and prominences without eclipses
		  (George Darwin Lecture, 1939).
		 <em></em>, 99:580, June 1939.
		[<a href="http://dx.doi.org/10.1093/mnras/99.8.580">DOI</a>&nbsp;]
		</p>
		<p><a name="Evans_1948"></a>
		John&nbsp;W. Evans.
		 A photometer for measurement of sky brightness near the sun.
		 <em>J. Opt. Soc. Am.</em>, 38(12):1083--1085, Dec 1948.
		[<a href="http://dx.doi.org/10.1364/JOSA.38.001083">DOI</a>&nbsp;|
		<a href="http://www.osapublishing.org/abstract.cfm?URI=josa-38-12-1083">http</a>&nbsp;]
		</p>
		<p><a name="Richardson_2010"></a>
		I.&nbsp;G. Richardson and H.&nbsp;V. Cane.
		 Near-Earth Interplanetary Coronal Mass Ejections During Solar Cycle
		  23 (1996 - 2009): Catalog and Summary of Properties.
		 <em></em>, 264(1):189--237, June 2010.
		[<a href="http://dx.doi.org/10.1007/s11207-010-9568-6">DOI</a>&nbsp;]
		</p>
		<p><a name="Howard_2019"></a>
		RA&nbsp;Howard, A&nbsp;Vourlidas, V&nbsp;Bothmer, RC&nbsp;Colaninno, CE&nbsp;DeForest, B&nbsp;Gallagher,
		  JR&nbsp;Hall, P&nbsp;Hess, AK&nbsp;Higginson, CM&nbsp;Korendyke, A&nbsp;Kouloumvakos, PL&nbsp;Lamy,
		  PC&nbsp;Liewer, J&nbsp;Linker, M&nbsp;Linton, P&nbsp;Penteado, SP&nbsp;Plunkett, N&nbsp;Poirier,
		  NE&nbsp;Raouafi, N&nbsp;Rich, P&nbsp;Rochus, AP&nbsp;Rouillard, DG&nbsp;Socker, G&nbsp;Stenborg,
		  AF&nbsp;Thernisien, and NM&nbsp;Viall.
		 Near-sun observations of an f-corona decrease and k-corona fine
		  structure.
		 <em>Nature</em>, 576(7786):232—236, December 2019.
		[<a href="http://dx.doi.org/10.1038/s41586-019-1807-x">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1038/s41586-019-1807-x">http</a>&nbsp;]
		</p>
		<p><a name="McComas_2019"></a>
		DJ&nbsp;McComas, ER&nbsp;Christian, CMS Cohen, AC&nbsp;Cummings, AJ&nbsp;Davis, MI&nbsp;Desai,
		  J&nbsp;Giacalone, ME&nbsp;Hill, CJ&nbsp;Joyce, SM&nbsp;Krimigis, AW&nbsp;Labrador, RA&nbsp;Leske,
		  O&nbsp;Malandraki, WH&nbsp;Matthaeus, RL&nbsp;McNutt, RA&nbsp;Mewaldt, DG&nbsp;Mitchell, A&nbsp;Posner,
		  JS&nbsp;Rankin, EC&nbsp;Roelof, NA&nbsp;Schwadron, EC&nbsp;Stone, JR&nbsp;Szalay, ME&nbsp;Wiedenbeck,
		  SD&nbsp;Bale, JC&nbsp;Kasper, AW&nbsp;Case, KE&nbsp;Korreck, RJ&nbsp;MacDowall, M&nbsp;Pulupa, ML&nbsp;Stevens,
		  and AP&nbsp;Rouillard.
		 Probing the energetic particle environment near the sun.
		 <em>Nature</em>, 576(7786):223—227, December 2019.
		[<a href="http://dx.doi.org/10.1038/s41586-019-1811-1">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1038/s41586-019-1811-1">http</a>&nbsp;]
		</p>
		<p><a name="Kasper_2019"></a>
		J&nbsp;C Kasper, S&nbsp;D Bale, J&nbsp;W Belcher, M&nbsp;Berthomier, A&nbsp;W Case, B&nbsp;D&nbsp;G Chandran, D&nbsp;W
		  Curtis, D&nbsp;Gallagher, S&nbsp;P Gary, L&nbsp;Golub, J&nbsp;S Halekas, G&nbsp;C Ho, T&nbsp;S Horbury,
		  Q&nbsp;Hu, J&nbsp;Huang, K&nbsp;G Klein, K&nbsp;E Korreck, D&nbsp;E Larson, R&nbsp;Livi, B&nbsp;Maruca,
		  B&nbsp;Lavraud, P&nbsp;Louarn, M&nbsp;Maksimovic, M&nbsp;Martinovic, D&nbsp;McGinnis, N&nbsp;V Pogorelov,
		  J&nbsp;D Richardson, R&nbsp;M Skoug, J&nbsp;T Steinberg, M&nbsp;L Stevens, A&nbsp;Szabo, M&nbsp;Velli, P&nbsp;L
		  Whittlesey, K&nbsp;H Wright, G&nbsp;P Zank, R&nbsp;J MacDowall, D&nbsp;J McComas, R&nbsp;L McNutt,
		  M&nbsp;Pulupa, N&nbsp;E Raouafi, and N&nbsp;A Schwadron.
		 Alfvénic velocity spikes and rotational flows in the near-sun solar
		  wind.
		 <em>NATURE</em>, 2019.
		[<a href="http://dx.doi.org/10.1038/s41586-019-1813-z">DOI</a>&nbsp;|
		<a href="http://hdl.handle.net/10150/636694">http</a>&nbsp;]
		</p>
		<p><a name="Bale_2019"></a>
		S. D. Bale, S. T. Badman, J. W. Bonnell, T. A. Bowen, D.&nbsp;Burgess, A.
		  W. Case, C. A. Cattell, B. D.G. Chandran, C. C. Chaston, C. H.K.
		  Chen, J. F. Drake, T. Dudok de Wit, J. P. Eastwood, R. E. Ergun,
		  W. M. Farrell, C.&nbsp;Fong, K.&nbsp;Goetz, M.&nbsp;Goldstein, K. A. Goodrich, P. R.
		  Harvey, T. S. Horbury, G. G. Howes, J. C. Kasper, P. J. Kellogg, J.
		  A. Klimchuk, K. E. Korreck, V. V. Krasnoselskikh, S.&nbsp;Krucker, R.&nbsp;Laker,
		  D. E. Larson, R. J. MacDowall, M.&nbsp;Maksimovic, D. M. Malaspina,
		  J.&nbsp;Martinez-Oliveros, D. J. McComas, N.&nbsp;Meyer-Vernet, M.&nbsp;Moncuquet, F. S.
		  Mozer, T. D. Phan, M.&nbsp;Pulupa, N. E. Raouafi, C.&nbsp;Salem, D.&nbsp;Stansby,
		  M.&nbsp;Stevens, A.&nbsp;Szabo, M.&nbsp;Velli, T.&nbsp;Woolley, and J. R. Wygant.
		 Highly structured slow solar wind emerging from an equatorial coronal
		  hole.
		 <em>Nature</em>, 576(7786):237--242, dec 2019.
		[<a href="http://dx.doi.org/10.1038/s41586-019-1818-7">DOI</a>&nbsp;]
		</p>
		<p><a name="Waldmeier_1974"></a>
		M.&nbsp;Waldmeier.
		 The Coronal Hole at the 7 March 1970 Solar Eclipse.
		 <em></em>, 40(2):351--358, February 1975.
		[<a href="http://dx.doi.org/10.1007/BF00162382">DOI</a>&nbsp;]
		</p>
		<p><a name="Tousey_1965"></a>
		R.&nbsp;Tousey.
		 Observations of the white light corona by rocket.
		 <em>Annales d'Astrophysique</em>, 28:600, February 1965.
		</p>
		<p><a name="Cooper_1964"></a>
		Detwiler C. R. Koomen M. J. Packer D. M. Purcell J.D. Seal R. T. Jr Tousey R.
		  et&nbsp;al. Cooper, H.&nbsp;W.
		 Observations of the white light corona from a rocket.
		 <em>NASA Technical Report</em>, February 1964.
		</p>
		<p><a name="Brueckner_1995"></a>
		G.&nbsp;E. Brueckner, R.&nbsp;A. Howard, M.&nbsp;J. Koomen, C.&nbsp;M. Korendyke, D.&nbsp;J.
		  Michels, J.&nbsp;D. Moses, D.&nbsp;G. Socker, K.&nbsp;P. Dere, P.&nbsp;L. Lamy,
		  A.&nbsp;Llebaria, M.&nbsp;V. Bout, R.&nbsp;Schwenn, G.&nbsp;M. Simnett, D.&nbsp;K. Bedford,
		  and C.&nbsp;J. Eyles.
		 The Large Angle Spectroscopic Coronagraph (LASCO).
		 <em></em>, 162(1-2):357--402, December 1995.
		[<a href="http://dx.doi.org/10.1007/BF00733434">DOI</a>&nbsp;]
		</p>
		<p><a name="nasa_2017"></a>
		Stereo, Nov 2017.
		[<a href="https://stereo.gsfc.nasa.gov/classroom/coronagraphs.shtml">http</a>&nbsp;]
		</p>
		<p><a name="Parker_1969"></a>
		E.&nbsp;N. Parker.
		 Theoretical Studies of the Solar Wind Phenomenon.
		 <em></em>, 9(3):325--360, May 1969.
		[<a href="http://dx.doi.org/10.1007/BF00175236">DOI</a>&nbsp;]
		</p>
		<p><a name="Jaggard_2019"></a>
		Victoria Jaggard.
		 Solar flares, explained, Apr 2019.
		[<a href="https://www.nationalgeographic.com/science/space/reference/solar-fares/\#close">http</a>&nbsp;]
		</p>
		<p><a name="Kontar_2008"></a>
		Kontar, E. P., Hannah, I. G., and MacKinnon, A. L.
		 Chromospheric magnetic field and density structure measurements using
		  hard x-rays in a flaring coronal loop.
		 <em>A&amp;A</em>, 489(3):L57--L60, 2008.
		[<a href="http://dx.doi.org/10.1051/0004-6361:200810719">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1051/0004-6361:200810719">http</a>&nbsp;]
		</p>
		<p><a name="Watko_2000"></a>
		J.&nbsp;A. Watko and J.&nbsp;A. Klimchuk.
		 Width Variations along Coronal Loops Observed by TRACE.
		 <em></em>, 193:77--92, April 2000.
		[<a href="http://dx.doi.org/10.1023/A:1005209528612">DOI</a>&nbsp;]
		</p>
		<p><a name="Howard_2008"></a>
		R.&nbsp;A. Howard, J.&nbsp;D. Moses, A.&nbsp;Vourlidas, J.&nbsp;S. Newmark, D.&nbsp;G. Socker, S.&nbsp;P.
		  Plunkett, C.&nbsp;M. Korendyke, J.&nbsp;W. Cook, A.&nbsp;Hurley, J.&nbsp;M. Davila, W.&nbsp;T.
		  Thompson, O.&nbsp;C. St&nbsp;Cyr, E.&nbsp;Mentzell, K.&nbsp;Mehalick, J.&nbsp;R. Lemen, J.&nbsp;P. Wuelser,
		  D.&nbsp;W. Duncan, T.&nbsp;D. Tarbell, C.&nbsp;J. Wolfson, A.&nbsp;Moore, R.&nbsp;A. Harrison, N.&nbsp;R.
		  Waltham, J.&nbsp;Lang, C.&nbsp;J. Davis, C.&nbsp;J. Eyles, H.&nbsp;Mapson-Menard, G.&nbsp;M. Simnett,
		  J.&nbsp;P. Halain, J.&nbsp;M. Defise, E.&nbsp;Mazy, P.&nbsp;Rochus, R.&nbsp;Mercier, M.&nbsp;F. Ravet,
		  F.&nbsp;Delmotte, F.&nbsp;Auchere, J.&nbsp;P. Delaboudiniere, V.&nbsp;Bothmer, W.&nbsp;Deutsch,
		  D.&nbsp;Wang, N.&nbsp;Rich, S.&nbsp;Cooper, V.&nbsp;Stephens, G.&nbsp;Maahs, R.&nbsp;Baugh, D.&nbsp;McMullin,
		  and T.&nbsp;Carter.
		 Sun earth connection coronal and heliospheric investigation (secchi).
		 <em>Space Science Reviews</em>, 136(1):67, May 2008.
		[<a href="http://dx.doi.org/10.1007/s11214-008-9341-4">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1007/s11214-008-9341-4">http</a>&nbsp;]
		</p>
		<p><a name="Thompson_2003"></a>
		William&nbsp;T. Thompson, Joseph&nbsp;M. Davila, Richard&nbsp;R. Fisher, Larry&nbsp;E. Orwig,
		  John&nbsp;Eric Mentzell, Samuel&nbsp;E. Hetherington, Rebecca&nbsp;J. Derro, Robert&nbsp;E.
		  Federline, David&nbsp;C. Clark, Philip T.&nbsp;C. Chen, June&nbsp;L. Tveekrem, Anthony&nbsp;J.
		  Martino, Joseph Novello, Richard&nbsp;P. Wesenberg, Orville&nbsp;C. StCyr, Nelson&nbsp;L.
		  Reginald, Russell&nbsp;A. Howard, Kimberly&nbsp;I. Mehalick, Michael&nbsp;J. Hersh, Miles&nbsp;D.
		  Newman, Debbie&nbsp;L. Thomas, Gregory&nbsp;L. Card, and David&nbsp;F. Elmore.
		 The COR1 inner coronagraph for STEREO-SECCHI.
		 In Stephen&nbsp;L. Keil and Sergey&nbsp;V. Avakyan, editors, <em>Innovative
		  Telescopes and Instrumentation for Solar Astrophysics</em>, volume 4853, pages 1
		  -- 11. International Society for Optics and Photonics, SPIE, 2003.
		[<a href="http://dx.doi.org/10.1117/12.460267">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1117/12.460267">http</a>&nbsp;]
		</p>
		<p><a name="Weiss_2019"></a>
		Matthew Weiss and Martin Weiss.
		 An assessment of threats to the american power grid.
		 <em>Energy, Sustainability and Society</em>, 9(1):18, May 2019.
		[<a href="http://dx.doi.org/10.1186/s13705-019-0199-y">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1186/s13705-019-0199-y">http</a>&nbsp;]
		</p>
		<p><a name="Battams_2017"></a>
		Karl Battams and Matthew&nbsp;M. Knight.
		 Soho comets: 20 years and 3000 objects later.
		 <em>Philosophical Transactions of the Royal Society A: Mathematical,
		  Physical and Engineering Sciences</em>, 375(2097):20160257, 2017.
		[<a href="http://dx.doi.org/10.1098/rsta.2016.0257">DOI</a>&nbsp;|
		<a href="http://arxiv.org/abs/https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2016.0257">arXiv</a>&nbsp;|
		<a href="https://royalsocietypublishing.org/doi/abs/10.1098/rsta.2016.0257">http</a>&nbsp;]
		</p>
		<p><a name="Posner_2007"></a>
		Arik Posner.
		 Up to 1-hour forecasting of radiation hazards from solar energetic
		  ion events with relativistic electrons.
		 <em>Space Weather</em>, 5(5), 2007.
		[<a href="http://dx.doi.org/10.1029/2006SW000268">DOI</a>&nbsp;|
		<a href="http://arxiv.org/abs/https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2006SW000268">arXiv</a>&nbsp;|
		<a href="https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2006SW000268">http</a>&nbsp;]
		</p>
		<p><a name="Murray_2018"></a>
		Sophie&nbsp;A. Murray, Jordan&nbsp;A. Guerra, Pietro Zucca, Sung-Hong Park, Eoin&nbsp;P.
		  Carley, Peter&nbsp;T. Gallagher, Nicole Vilmer, and Volker Bothmer.
		 Connecting coronal mass ejections to their solar active region
		  sources: Combining results from the helcats and flarecast projects.
		 <em>Solar Physics</em>, 293(4), Apr 2018.
		[<a href="http://dx.doi.org/10.1007/s11207-018-1287-4">DOI</a>&nbsp;|
		<a href="http://dx.doi.org/10.1007/s11207-018-1287-4">http</a>&nbsp;]
		</p>
		<p><a name="Reale_2014"></a>
		Fabio Reale.
		 Coronal loops: Observations and modeling of confined plasma.
		 <em>Living Reviews in Solar Physics</em>, 11(1):4, Jul 2014.
		[<a href="http://dx.doi.org/10.12942/lrsp-2014-4">DOI</a>&nbsp;|
		<a href="https://doi.org/10.12942/lrsp-2014-4">http</a>&nbsp;]
		</p>
		<p><a name="Pedrotti_2019"></a>
		Frank&nbsp;L. Pedrotti, Leno&nbsp;Matthew Pedrotti, and Leno&nbsp;S. Pedrotti.
		 <em>Introduction to optics</em>.
		 Cambridge University Press, 2019.
		</p>
		<p><a name="Noll_1973"></a>
		Robert&nbsp;J. Noll.
		 Reduction of diffraction of use of a lyot stop.
		 <em>J. Opt. Soc. Am.</em>, 63(11):1399--1402, Nov 1973.
		[<a href="http://dx.doi.org/10.1364/JOSA.63.001399">DOI</a>&nbsp;|
		<a href="http://www.osapublishing.org/abstract.cfm?URI=josa-63-11-1399">http</a>&nbsp;]
		</p>
		<p><a name="Jones_2017"></a>
		Geraint&nbsp;H. Jones, Matthew&nbsp;M. Knight, Karl Battams, Daniel&nbsp;C. Boice, John Brown,
		  Silvio Giordano, John Raymond, Colin Snodgrass, Jordan&nbsp;K. Steckloff, Paul
		  Weissman, Alan Fitzsimmons, Carey Lisse, Cyrielle Opitom, Kimberley&nbsp;S.
		  Birkett, Maciej Bzowski, Alice Decock, Ingrid Mann, Yudish Ramanjooloo, and
		  Patrick McCauley.
		 The science of sungrazers, sunskirters, and other near-sun comets.
		 <em>Space Science Reviews</em>, 214(1):20, Dec 2017.
		[<a href="http://dx.doi.org/10.1007/s11214-017-0446-5">DOI</a>&nbsp;|
		<a href="https://doi.org/10.1007/s11214-017-0446-5">http</a>&nbsp;]
		</p>
		<p><a name="Wiegelmann_2004"></a>
		T.&nbsp;Wiegelmann and S.&nbsp;K. Solanki.
		 Similarities and differences between coronal holes and the quiet sun:
		  Are loop statistics the key?
		 <em>Solar Physics</em>, 225(2):227–247, Dec 2004.
		[<a href="http://dx.doi.org/10.1007/s11207-004-3747-2">DOI</a>&nbsp;|
		<a href="http://dx.doi.org/10.1007/s11207-004-3747-2">http</a>&nbsp;]
		</p>
		<p><a name="Filippov_2015"></a>
		Boris Filippov, Olesya Martsenyuk, Abhishek&nbsp;K. Srivastava, and Wahab Uddin.
		 Solar magnetic flux ropes.
		 <em>Journal of Astrophysics and Astronomy</em>, 36(1):157–184, Mar
		  2015.
		[<a href="http://dx.doi.org/10.1007/s12036-015-9321-5">DOI</a>&nbsp;|
		<a href="http://dx.doi.org/10.1007/s12036-015-9321-5">http</a>&nbsp;]
		</p>
		<p><a name="Gou_2019"></a>
		Tingyu Gou, Rui Liu, Bernhard Kliem, Yuming Wang, and Astrid&nbsp;M. Veronig.
		 The birth of a coronal mass ejection.
		 <em>Science Advances</em>, 5(3), 2019.
		[<a href="http://dx.doi.org/10.1126/sciadv.aau7004">DOI</a>&nbsp;|
		<a href="http://arxiv.org/abs/https://advances.sciencemag.org/content/5/3/eaau7004.full.pdf">arXiv</a>&nbsp;|
		<a href="https://advances.sciencemag.org/content/5/3/eaau7004">http</a>&nbsp;]
		</p>
		<p><a name="Weissman_2006"></a>
		Lucy-Ann&nbsp;Adams. McFadden, Paul&nbsp;Robert Weissman, and T.&nbsp;V. Johnson.
		 <em>Encyclopedia of the solar system</em>.
		 Elsevier Science, 2006.
		</p>
		<p><a name="NASA_2019"></a>
		Office of&nbsp;Inspector&nbsp;General.
		 Nasa’s heliophysics portfolio.
		 Ig-19-018, NASA, 2019.
		</div>
</div>
<div id="resources">
	<div class="collapsible">
		<div class="collapsible-header">
			<h2>Resources</h2>
		</div>
		<div class="panel">
			<ul>
				<li><a href="https://sdo.gsfc.nasa.gov/" target="_blank">Solar Dynamic Observatory</a></li>
				<li><a href="https://sohowww.nascom.nasa.gov/" target="_blank">Solar and Heliospheric Observatory</a></li>
				<li><a href="http://parkersolarprobe.jhuapl.edu/" target="_blank">Parker Solar Probe</a></li>
				<li><a href="https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter" target="_blank">Solar Orbiter</a></li>
			</ul>
		</div>
	</div>
</div>
