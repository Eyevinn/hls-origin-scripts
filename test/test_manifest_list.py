import pytest
import hlsorigin

class TestManifestList:
    def test_seglist_sorting_one(self):
        mockSegments = {}
        mockSegments['20170308T100730-master2404-189/287.ts'] = { 'uri': '20170308T100730-master2404-189/287.ts' }
        mockSegments['20170308T100730-master2404-188/1739.ts'] = { 'uri': '20170308T100730-master2404-188/1739.ts' }
        mockSegments['20170308T100730-master2404-188/1740.ts'] = { 'uri': '20170308T100730-master2404-188/1740.ts' }
        sortedKeys = sorted(mockSegments.keys(), key=hlsorigin.SEGMENTNO)
        for s in sortedKeys:
            print s
        assert sortedKeys == ['20170308T100730-master2404-188/1739.ts', 
            '20170308T100730-master2404-188/1740.ts',
            '20170308T100730-master2404-189/287.ts']

    def test_seglist_sorting_two(self):
        mockSegments = {}
        mockSegments['20170308T100730-master2404-188/1738.ts'] = { 'uri': '20170308T100730-master2404-188/1738.ts' }
        mockSegments['20170308T100730-master2404-188/1739.ts'] = { 'uri': '20170308T100730-master2404-188/1739.ts' }
        mockSegments['20170308T100730-master2404-188/1740.ts'] = { 'uri': '20170308T100730-master2404-188/1740.ts' }
        sortedKeys = sorted(mockSegments.keys(), key=hlsorigin.SEGMENTNO)
        for s in sortedKeys:
            print s
        assert sortedKeys == ['20170308T100730-master2404-188/1738.ts', 
            '20170308T100730-master2404-188/1739.ts',
            '20170308T100730-master2404-188/1740.ts']
   
    def test_seglist_sorting_three(self):
        mockSegments = {}
        mockSegments['1738.ts'] = { 'uri': '1738.ts' }
        mockSegments['1739.ts'] = { 'uri': '1739.ts' }
        mockSegments['1740.ts'] = { 'uri': '1740.ts' }
        sortedKeys = sorted(mockSegments.keys(), key=hlsorigin.SEGMENTNO)
        for s in sortedKeys:
            print s
        assert sortedKeys == ['1738.ts', 
            '1739.ts',
            '1740.ts']

    def test_seglist_sorting_four(self):
        mockSegments = {}
        mockSegments['master2372/00000/master2372_01771.ts'] = { 'uri': 'master2372/00000/master2372_01771.ts' }
        mockSegments['master2372/00000/master2372_01772.ts'] = { 'uri': 'master2372/00000/master2372_01772.ts' }
        mockSegments['master2372/00000/master2372_01773.ts'] = { 'uri': 'master2372/00000/master2372_01773.ts' }
        sortedKeys = sorted(mockSegments.keys(), key=hlsorigin.SEGMENTNO)
        for s in sortedKeys:
            print s
        assert sortedKeys == ['master2372/00000/master2372_01771.ts', 
            'master2372/00000/master2372_01772.ts',
            'master2372/00000/master2372_01773.ts']

    def test_seglist_sorting_five(self):
        mockSegments = {}
        mockSegments['master2372/00002/master2372_01771.ts'] = { 'uri': 'master2372/00000/master2372_01771.ts' }
        mockSegments['master2372/00001/master2372_01872.ts'] = { 'uri': 'master2372/00000/master2372_01772.ts' }
        mockSegments['master2372/00001/master2372_01873.ts'] = { 'uri': 'master2372/00000/master2372_01773.ts' }
        sortedKeys = sorted(mockSegments.keys(), key=hlsorigin.SEGMENTNO)
        for s in sortedKeys:
            print s
        assert sortedKeys == ['master2372/00001/master2372_01872.ts', 
            'master2372/00001/master2372_01873.ts',
            'master2372/00002/master2372_01771.ts']
