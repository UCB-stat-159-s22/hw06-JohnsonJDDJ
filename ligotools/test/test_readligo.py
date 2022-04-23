from ligotools import readligo as rl
import numpy as np

strain, time, dq = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')

def test_loaddata_strain():	
	try:
		assert np.isclose(strain[0], 2.087638998830647e-19)
	except AssertionError as detail:
		msg = "The strain value loaded from data is not correct."
		raise AssertionError(detail.__str__() + "\n" +  msg)

def test_loaddata_time():	
	try:
		assert np.isclose(time[0], 1126259446.0)
	except AssertionError as detail:
		msg = "The time value loaded from data is not correct."
		raise AssertionError(detail.__str__() + "\n" +  msg)
		
def test_loaddata_dq():	
	try:
		assert dq.items()[0][0] == u'NO_BURST_HW_INJ'
	except AssertionError as detail:
		msg = "The dq value loaded from data is not correct."
		raise AssertionError(detail.__str__() + "\n" +  msg)
		
def test_dq_channel_to_seglist():
	DQflag = 'CBC_CAT3'
	segment_list = rl.dq_channel_to_seglist(dq[DQflag])
	try:
		assert len(segment_list) == 1
	except AssertionError as detail:
		msg = "The length of the segment does not match."
		raise AssertionError(detail.__str__() + "\n" +  msg)