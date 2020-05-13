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
					$$B_r (r, \theta, \phi) = B \Big(\theta, \phi + \frac{r \Omega}{v} \Big) \Big(\frac{r_0}{r}\Big)^2 .$$
					where \(\Omega\) represents the angular velocity of the Sun, $v$ is the velocity of the radial winds, while $\theta$ and $\phi$ represent traditional polar and azimuthal angles.
					<!-- $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$ -->
				</p>
			<h5>The chromosphere</h5>
				<p>
					&emsp;The chromosphere is the lowest region of the solar atmosphere and contains a mixture of cool gas and hot plasma that is released from the surface. This region of the Sun's atmosphere has structure that is particularly difficult to observe directly with spectroscopic methods as a consequence of weak magnetic fields, the insensitive spectral lines broaden (Kontar, 2008). However, utilizing the magnetic field's interactions with X-rays it is possible to quantitatively define the loop structure (Kontar, 2008; Watko, 2000). For the purposes of this paper, we will not continue this discussion regarding the chromosphere, as this region is usually not the focus of observation for coronagraphs.
				</p>
			<h5>The corona</h5>
			    <p>
			        &emsp;The corona is the furthest part of the solar atmosphere and is the focus of observation for coronagraphs, as we will discuss in more detail later. The corona has also been observed elongated between 0.07 AU and 0.45 AU (Howard, 2019). There are three primary components associated with the corona, denoted by the letters: F, K, and L.
							<br>
							&emsp;The F-component is the outer portion of the corona and is a consequence of diffraction via interplanetary dust (Waldmeier, 1963). The dark absorption lines of the solar spectrum, Fraunhofer lines, are observed in this region unlike the K-corona. (Calbert, 1972) characterizes the light intensity of this region as a function of the elongation angle of corona $\epsilon$ as ,
							$$i(\epsilon) = E(\lambda)\iint\frac{\pi a^2}{r^2} n(r,a) I(\theta) dl da. $$
							where $E(\lambda)$ is the total light radiated per steradian, $a$ is the radius of the interplanetary dust, $r$ is the distance between the dust particle and the center of the Sun, $n(r,a)$ defines the number of particles of the given radius between differential positions.
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
						&emsp;Solar coronagraphs are utilized at looking at our Sun, rather than at distant star systems. The original design for a coronagraph included an external occulting disk with a planoconvex lens, ground from borosilicate crown glass, with diameter of twenty centimeters and a focal length of four meters (Lyot, 1939). The main tube was made from duralumin with a length of six meter which can be seen in Figure \ref{fig:Lyot_corona}. In the original design it can be noted that there was a spectrograph integrated into the instrument. The imaging device that was used in this design was a simple camera, noted by R in Figure \ref{fig:Lyot_corona}. From his design, by applying a orange filter and a "weak" eyepiece, Lyot stated that the innermost regions of the solar corona can be observed. One of the many products of the invention of the coronagraph was a mechanism called the Lyot Stop. This simple mechanism reduces the intensity of flare cause by the diffraction of other field stops in a optical system (Noll, 1973).
						<br>
						&emsp;The modern coronagraphs that we will look at include the High Altitude Observatory *(HAO)*, the Solar and Heliospheric Observatory *(SoHO)*, a probe with three coronagraphs on-board including one hybrid coronagraph, and the Solar Terrestrial Relations Observatory *(STeReO)*.
						<br>
						&emsp;The HAO has a focus on research pertaining to various disciplines of space science and solar physics. The telescope itself is, as mentioned before, a ground-based photometer with a Lyot design (Evans, 1948). The telescope is equipped with two externally occulting disks with a linear diameter analytically defined as
						$$O_1 = 2\varphi d + a_1,$$
						$$O_2 = 2f_1 ( \varphi + {a_1 \over d} ).$$
						where $\varphi$ is the angular radius of the sun *(usually about 0.0047 radians)*, $d$ is the distance between the first occulting disk and the aperture of diameter $a_1$, the focal length of the optical system is defined by $f_1$ (Evans, 1948). The first occulting disk is used primarily to block out the direct sunlight, the second disk was applied early on to negate the effects of vignetting that became apparent during the initial tests of the coronagraph (Evans, 1948).
						<br>
						&emsp;The SoHO payload includes the Large Angle Spectroscopic Coronagraph *(LASCO)*; a collection of three coronagraphs labeled: C1, C2, and C3. Some of the basic properties of the three telescopes are included in Table \ref{tab:lasco}. Each of the coronagraphs is equipped with a three-phase, front-side illuminated 1024 $\times$ 1024 pixel CCD imaging system (Brueckner, 1995).
					</p>
		</div>
	</div>
</div>
<div id="references">
	<div class="collapsible">
		<div class="collapsible-header">
			<h2>References</h2>
		</div>
		<div class="panel">
		    <div id="ref1">
                <p style="color: #000; display:inline;">
                    [1]
                </p>
                <a href="https://scied.ucar.edu/solar-chromosphere">
                The Sun's Chromosphere (lower Atmosphere), UCAR.
                </a>    
            </div>
            <div id="ref2">
                <p style="color: #000; display:inline;">
                    [2]
                </p>
                <a href="https://scied.ucar.edu/solar-corona">
                The Sun's Corona (upper Atmosphere), UCAR.
                </a>    
            </div>
		</div>
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
