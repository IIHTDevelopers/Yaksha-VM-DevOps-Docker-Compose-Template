class TestUtils:
    def yakshaAssert(self, test_name, result, test_type):
        """
        Method to assert test results and record them
        
        Args:
            test_name (str): Name of the test
            result (bool): Test result (True for pass, False for fail)
            test_type (str): Type of test (e.g., "functional")
        """
        self.test_name = test_name
        self.result = result
        self.test_type = test_type
        # In a real implementation, this might write to a file or database
        # For now, we'll just return the result
        return result
