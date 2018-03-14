{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:hyperspy.api:The traitsui GUI elements are not available, probably because the hyperspy_gui_traitui package is not installed.\n"
     ]
    }
   ],
   "source": [
    "import hyperspy.api as hs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%matplotlib qt5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "edx_data = hs.load(\"C:/Users/Tara/Documents/Research/17-06_TEMCIGS/EDX_fitting/46_edx_20k_as_44.rpl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = hs.load(\"C:/Users/Tara/Documents/Research/17-06_TEMCIGS/GS_C5/dm3_Images/ForEDX.dm3\")\n",
    "dim = img.axes_manager.shape\n",
    "imgBin = img.rebin((dim[0],dim[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "imgBin.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "edx_data.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Integrate over the spatial 0 and 1 dimensions to get the average spectra\n",
    "s = edx_data.integrate1D(0)\n",
    "s = s.integrate1D(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "edx_data.set_signal_type('EDS_TEM')\n",
    "edx_data.set_microscope_parameters(beam_energy=200, live_time=2008, tilt_stage=0, azimuth_angle=45, elevation_angle=18, energy_resolution_MnKa=131.79)\n",
    "edx_data.set_elements(['C','N','O','Si','S','K','Na','Cl','Ca', 'Cu'])\n",
    "edx_data.change_dtype('float32')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "edx_data.add_lines([\"Cu_Kb\",\"Cu_La\",\"Cu_Lb1\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<BaseSignal, title: X-ray line intensity of EDX: C_Ka at 0.28 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Ca_Ka at 3.69 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Cl_Ka at 2.62 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Cu_Ka at 8.05 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Cu_Kb at 8.91 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Cu_La at 0.93 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Cu_Lb1 at 0.95 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: K_Ka at 3.31 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: N_Ka at 0.39 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Na_Ka at 1.04 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: O_Ka at 0.52 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: S_Ka at 2.31 keV, dimensions: (512, 512|)>,\n",
       " <BaseSignal, title: X-ray line intensity of EDX: Si_Ka at 1.74 keV, dimensions: (512, 512|)>]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "edx_data.get_lines_intensity()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "i=0\n",
    "while i<12:\n",
    "    edx_data.get_lines_intensity()[i].plot()\n",
    "    i = i+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "edx_data.get_lines_intensity()[7].plot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### Local averaging"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Area1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint1 = np.average(edx_data.data[170:360,180:340,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint1 = np.average(s_localint1[:,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "x_nm = np.zeros_like(edx_data.data[0,0,:])\n",
    "for i in range(len(x_nm)):\n",
    "    x_nm[i]=(i*edx_data.axes_manager[2].scale+edx_data.axes_manager[2].offset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fig, ax = plt.subplots(1, 1)\n",
    "plt.plot(x_nm, s_localint1, lw=2, label='Local ave')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### Area2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint2 = np.average(edx_data.data[0:170,0:180,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint2 = np.average(s_localint2[:,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fig, ax = plt.subplots(1, 1)\n",
    "plt.plot(x_nm, s_localint2, lw=2, label='Local ave')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### Area3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint3= np.average(edx_data.data[460:630,0:180,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "s_localint3 = np.average(s_localint3[:,:],0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "fig, ax = plt.subplots(1, 1)\n",
    "plt.plot(x_nm, s_localint3, lw=2, label='Local ave')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
