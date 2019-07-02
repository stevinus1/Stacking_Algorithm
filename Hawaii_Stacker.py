from Stacker import Stacker
import clustering_scripts as cs
import numpy as np

class Hawaii_Stacker(Stacker):
	
	def adaptive_stack(self, geographical=False):
		
		print("Stacking...")
		
		cut_length = round(len(self.seis_data)/10)
		self.cluster, self.stacks = cs.second_cluster(self.cluster, self.coords, self.stacks, threshold=cut_length, crit='maxclust', dist=True, corr=False)
		#self.read_in(785, 7855, 750, 'hawaii_first_stack')
		self.remove_anoms(5)
		while len(self.stacks) > 40:
			if geographical == True:
				self.cluster, self.stacks = cs.second_cluster(self.cluster, cs.stack_coords(self.cluster, self.coords), self.stacks, threshold=1, crit='inconsistent', dist=True, corr=False)
			else:
				self.cluster, self.stacks = cs.second_cluster(self.cluster, cs.stack_coords(self.cluster, self.coords), self.stacks, threshold=1, crit='inconsistent', dist=True, corr=False)
			self.remove_anoms(self.average_cluster_variance()*2, variance=True)
			self.remove_anoms(round(self.average_stack_size()/4))
		print(len(self.stacks))
		print(len(self.coords))
		
		return
