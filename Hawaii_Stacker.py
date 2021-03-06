from Stacker import Stacker
import clustering_scripts as cs
import numpy as np
import os
import plotting_scripts as ps

class Hawaii_Stacker(Stacker):
	
	def adaptive_stack(self, geographical=False):
		
		print("Stacking...")
		
		cut_length = round(len(self.seis_data)/10)
		self.cluster, self.stacks = cs.second_cluster(self.cluster, self.coords, self.stacks, threshold=cut_length, crit='maxclust', dist=True, corr=False)
		#self.read_in(785, 7855, 750, 'hawaii_first_stack')
		#self.remove_anoms(5)
		while len(self.stacks) > 35:
			if geographical == True:
				self.cluster, self.stacks = cs.second_cluster(self.cluster, cs.stack_coords(self.cluster, self.coords), self.stacks, threshold=1, crit='inconsistent', dist=True, corr=False)
			else:
				self.cluster, self.stacks = cs.second_cluster(self.cluster, cs.stack_coords(self.cluster, self.coords), self.stacks, threshold=1, crit='inconsistent', dist=True, corr=True)
			self.remove_anoms(self.average_cluster_variance()*1.5, variance=True)
			#self.remove_anoms(round(self.average_stack_size()/3))
		#self.remove_anoms(200)
		return

	
	def plot(self, indiv=True):
		
		print("Plotting...")
		
		os.mkdir(self.filename)
		os.chdir(self.filename)
		ps.plot(self, self.filename, plot_individual=indiv)
		ps.mag_plot(self, self.filename+'_mags')
		ps.interpolation(self, self.filename+'_interpol')
		os.chdir('..')
		
		return

