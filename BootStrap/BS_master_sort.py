#!/usr/bin/python 

import os,sys,glob
from tqdm import tqdm
import numpy as np


# Enter folder with Trajectories
path = os.getcwd()
p1 = path + '/Trajectories'
os.chdir(p1)
# Enumerate Taxa
d_ = glob.glob('*.gro')
e_ = glob.glob('*.xtc')
if len(d_) != len(e_):
	raise ValueError('Mismatch between structures and topologies. This condition should not happen.')
# Create N_trials number of folders
N_trials = 100
dir_trial = np.arange(0,100,1)
# Creating Analysis directory for easy hand-ling
os.system('mkdir Trials')
p2 = path + '/Trajectories/Trials'
os.chdir(p2)
# Make trial folders
for folders in dir_trial:
	os.system('mkdir trial_' + str(folders))
	os.system('cp ../../Scripts/* trial_'+str(folders))
# Generate list of random numbers for each trajectory and save them
# Access each trajectory 
# For each random number in saved file
for traj in d_:
	xtc = traj[0:traj.index('.')] + ".xtc" #@Alex
	output = traj[0:traj.index('.')] + "_frames.pdb" #@Alex
	#fr = traj[0:traj.index('.')] + ".ndx" #@Alex
	#frame_sel = np.random.randint(0,2500,N_trials) # Generates N_trials numbers to get a frame per trial
	#with open(p1 + '/' + traj.split('.')[0]+'.ndx','a') as f:
	#	f.write('`[frames]' + '\n')
	#	for val_ in frame_sel:
	#		f.write(str(val_) + '\n')
	#	f.write('`\n')
	j=0
	for i in range(N_trials):
		os.chdir(p1)
		fr = traj.split('.')[0]+'.ndx'
		with open(fr,'w') as f:
			f.write('`[frames]\n' + str(np.random.randint(0,2500)) + '`')
		os.system('echo 1 | gmx trjconv -s ' + traj + ' -f ' + xtc + ' -o ' + p2 + '/trial_' + str(j) + '/' + output + ' -fr ' + fr) #@Alex - pulls frames from trajectory files using GROMACS instead of VMD
		j = j+1
	#@Alex - save frames (from GROMACS) to trial folders
	#with open(p1 + )
		#open(p2 + )
# save frame to trial folder
# TCL
#os.system('/Applications/VMD\ 1.9.4.app/Contents/MacOS/startup.command -dispdev text -eofexit < BS_slave.tcl ')