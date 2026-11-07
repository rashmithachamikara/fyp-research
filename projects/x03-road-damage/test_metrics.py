import unittest
import numpy as np
from metrics import xyxy,match,masks,average_precision_binary,select_threshold,grid_cell
from prepare import convert_box

class MetricsTest(unittest.TestCase):
    def test_voc_conversion(self):
        self.assertEqual(convert_box([1,1,100,100],100,100),[.5,.5,1,1])
        with self.assertRaises(ValueError): convert_box([80,80,10,10],100,100)
    def test_one_to_one_and_wrong_class(self):
        gt=np.array([[0,0,0,10,10]])
        pred=np.array([[0,0,10,10,.9,0],[0,0,10,10,.8,0],[0,0,10,10,.95,1]])
        pairs,fp,miss=match(gt,pred,.5)
        self.assertEqual(pairs,[(0,0)]); self.assertEqual(set(fp),{1,2}); self.assertEqual(miss,[])
    def test_empty_cases(self):
        pairs,fp,miss=match(np.zeros((0,5)),np.array([[0,0,10,10,.9,0]]),.5)
        self.assertEqual(fp,[0]); self.assertEqual(miss,[])
        self.assertEqual(match(np.array([[0,0,0,10,10]]),np.zeros((0,6)),.5)[2],[0])
    def test_union_counts_once(self):
        gt=np.array([[0,0,0,10,10],[0,0,0,100,10],[0,0,0,100,100]])
        mm=masks(gt,640,640)
        self.assertEqual(int(mm['small_or_thin'].sum()),2)
        self.assertEqual(int(mm['B_eligible'].sum()),2)
    def test_tied_ap(self):
        self.assertAlmostEqual(average_precision_binary([True,False],[0,0]),.5)
        self.assertIsNone(average_precision_binary([False],[1]))
    def test_letterbox_grid_and_boundaries(self):
        self.assertEqual(grid_cell(0,0,1280,720),(8,0))
        self.assertEqual(grid_cell(1280,720,1280,720),(31,39))
        self.assertEqual(grid_cell(640,640,640,640),(39,39))
        self.assertEqual(grid_cell(16,16,640,640),(1,1))
    def test_threshold_uses_supplied_selection_only(self):
        records=[dict(id='selection',width=100,height=100,group='a',boxes=[[0,.5,.5,1,1]])]
        threshold,info=select_threshold(records,{'selection':[[0,0,100,100,.8,0]],'unseen':[[0,0,100,100,.1,0]]})
        self.assertLessEqual(threshold,.8); self.assertGreater(threshold,.79)
        self.assertIn('precision',info['rule'])

if __name__=='__main__': unittest.main()
