import unittest
from urlcheck import inspect
class TestURLs(unittest.TestCase):
    def test_ip(self): self.assertTrue(any("IP address" in s for s in inspect("https://127.0.0.1/")))
    def test_userinfo(self): self.assertTrue(any("userinfo" in s for s in inspect("https://example.com@evil.example")))
    def test_port(self): self.assertEqual(inspect("https://example.com:abc"),["Malformed URL."])
    def test_caveat(self): self.assertTrue(any("NOT" in s for s in inspect("https://example.com")))
if __name__=="__main__": unittest.main()
