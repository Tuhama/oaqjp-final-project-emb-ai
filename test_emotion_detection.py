from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for positive sentiment
        result = emotion_detector('I love working with Python')
        self.assertEqual(result['dominant_emotion'], 'joy')

unittest.main()