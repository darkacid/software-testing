import hw03_firewall

import unittest

class TestFirewall(unittest.TestCase):

    def test_block_correct(self):
        fw = hw03_firewall.firewall()
        self.assertTrue(fw.block('10.42.0.1/32'))

    def test_block_notString(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.block(74),"Subnet must be a string.")

    def test_block_alreadyBlocked(self):
        fw = hw03_firewall.firewall()
        fw.block('10.42.0.1/32')
        self.assertEqual(fw.block('10.42.0.1/32'),"Subnet already blocked.")

    def test_block_invalidSubnet(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.block('10.42.0.1/666'),"Invalid IP")

    def test_unblock_correct(self):
        fw = hw03_firewall.firewall()
        fw.block('10.42.0.1/32')
        self.assertTrue(fw.unblock('10.42.0.1/32'))

    def test_unblock_notString(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.unblock(74),"Subnet must be a string.")

    def test_unblock_notBlocked(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.unblock("10.42.0.1/32"),"Subnet not blocked.")

    def test_unblock_invalidSubnet(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.block('10.42.0.1/666'),"Invalid IP")

    def test_enableService_correct_ssh(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.enableService("ssh"),True)

    def test_enableService_correct_http(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.enableService("http"),True)

    def test_enableService_notString(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.enableService(42),"Service name must be a string.")

    def test_enableService_notRecognized(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.enableService("42"),"Service name not recognized.")


    def test_disableService_correct_ssh(self):
        fw = hw03_firewall.firewall()
        fw.enableService("ssh")
        self.assertEqual(fw.disableService("ssh"),True)

    def test_disableService_correct_http(self):
        fw = hw03_firewall.firewall()
        fw.enableService("http")
        self.assertEqual(fw.disableService("http"),True)

    def test_disableService_notString(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.disableService(42),"Service name must be a string.")

    def test_disableService_notRecognized(self):
        fw = hw03_firewall.firewall()
        self.assertEqual(fw.enableService("42"),"Service name not recognized.")






if __name__ == '__main__':
    unittest.main()

