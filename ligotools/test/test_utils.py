from ligotools.utils import *
import numpy as np

def test_whiten1():	
	whitened = whiten([1,2], np.mean, 0.1)
	try:
		assert np.isclose(whitened, [0.28284271, 0.56568542]).all()
	except AssertionError as detail:
		msg = "The result does not match for input ([1,2], np.mean, 0.1)"
		raise AssertionError(detail.__str__() + "\n" +  msg)
		
def test_whiten2():	
	whitened = whiten([1,2,3,4], np.exp, 1)
	try:
		assert np.isclose(whitened, [1.7367995 , 2.83819013, 4.23287768, 5.33426831]).all()
	except AssertionError as detail:
		msg = "The result does not match for ([1,2,3,4], np.exp, 1)"
		raise AssertionError(detail.__str__() + "\n" +  msg)

def test_reqshift1():
	shifted = reqshift([1,2], 100, 1000)
	try:
		assert np.isclose(shifted, [1,2]).all()
	except AssertionError as detail:
		msg = "The result does not match for ([1,2], 100, 1000)."
		raise AssertionError(detail.__str__() + "\n" +  msg)
		
def test_reqshift2():
	shifted = reqshift([1,2], 100, 100)
	try:
		assert np.isclose(shifted, [0,0]).all()
	except AssertionError as detail:
		msg = "The result does not match for ([1,2], 100, 100)."
		raise AssertionError(detail.__str__() + "\n" +  msg)
		