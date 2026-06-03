
# Required classes:

# TestCase — represents a single test
#   Instance Attributes 
#       name
#       Description
#       run()
#       Various assert statements 
#
# TestSuite — a collection of test cases
#       list_of_tests
#       add_test(name)
#       run()
#       get_size()
# TestResult — the outcome of running a test
#   Instance Attributes 
#       passed
#       duration
#       display_result()
#       
# TestRunner — executes a suite and collects results
#       run()




class TestCase:
    """Represents a single test case.

    Class Attributes:
        total_created (int): Count of all TestCase objects ever created

    Instance Attributes:
        name (str): Test name (e.g., "test_login_valid")
        description (str): What this test verifies
        priority (str): "high", "medium", or "low" (default: "medium")
        tags (list): Labels like ["smoke", "regression"]
    """
    
    # TODO: Implement __init__, run(), and a class method

    total_created = 0
    def __init__(self, name:str, description:str, priority:str="medium", tags:list=None):
        self.name=name
        self.description=description
        self.priority=priority
        self.tags=tags or []
        TestCase.total_created += 1

    def run(self):
        """Simulate running the test. Return True for pass, False for fail.
        For now, use: return "fail" not in self.name
        """
        return "fail" not in self.name

    @classmethod
    def from_dict(cls, data):
        """Create a TestCase from a dictionary.
        Example: TestCase.from_dict({"name": "test_login", "priority": "high"})
        """

        return cls(
            name=data["name"],
            description=data.get("description",""),
            priority=data.get("priority", "medium"),
            tags=data.get("tags",[])
        )
        

    @staticmethod
    def is_valid_name(name):
        """Check if name starts with 'test_' and has no spaces."""
        return name.startswith("test_") and " " not in name




class TestResult:
    """The outcome of running a single test.

    Instance Attributes:
        test_name (str): Which test was run
        status (str): "pass" or "fail"
        duration_ms (float): How long it took
        error_message (str or None): Error details if failed
    """
    # TODO: Implement

    def __init__(self, test_name:str, status:str, duration_ms:float, error_message:str=None):
        self.test_name = test_name
        self.status = status
        self.duration_ms = duration_ms
        self.error_message = error_message

    def summary(self):
        """Return a one-line summary like: '✅ test_login (120ms)'"""
        if self.status == "pass":
            return f"✅ {self.test_name} ({self.duration_ms}ms)"
        else:
            return f"❌ {self.test_name} ({self.duration_ms}ms)"
        
    

class TestSuite:
    """A collection of test cases.

    Instance Attributes:
        name (str): Suite name
        tests (list): List of TestCase objects

    Methods:
        add_test(test): Add a TestCase
        remove_test(name): Remove by name
        get_by_priority(priority): Return tests matching the priority
        count(): Return number of tests
    """
    def __init__(self, name:str, tests:list=None):
        self.name=name
        self.tests= tests if tests is not None else []
    
    def add_test(self,test):
        """ Add a TestCase"""
        self.tests.append(test)

    def remove_test(self, name):
        self.tests=[t for t in self.tests if t.name != name]

    def get_by_priority(self,priority):
        result=[]
        for test in self.tests:
            if test.priority==priority:
                result.append(test)
        return result
    
    def count(self):
        return len(self.tests)
    


class TestRunner:
    """Executes a TestSuite and collects results.

    Methods:
        run(suite): Run all tests in a suite, return list of TestResult
        summary(results): Print a formatted summary
    """
    # TODO: Implement

    def run(self, suite):
        """Run each test in the suite and return a list of TestResults."""
        import time
        import random
        results = []
        for test in suite.tests:
            start = time.time()
            passed = test.run()
            duration = (time.time() - start) * 1000
            # Simulate varying duration
            duration += random.uniform(50, 500)
            result = TestResult(
                test.name,
                "pass" if passed else "fail",
                round(duration, 1),
                None if passed else f"{test.name} assertion failed"
            )
            results.append(result)
        return results
    
    def summary(self, results):
        for result in results:
            print(result.summary())
        passed = sum(1 for r in results if r.status == "pass")
        print(f"\n{passed}/{len(results)} tests passed")

        

def main():
    
    """
    Create a main() function that:

        Creates 6+ TestCase objects (mix of passing and failing names).
        Uses TestCase.from_dict() for at least 2 of them.
        Creates a TestSuite and adds all tests.
        Uses get_by_priority("high") to list high-priority tests.
        Runs the suite with TestRunner.
        Prints the results summary.
    
    """
    tc1 = TestCase("test_login_valid", "Checks valid login", priority="high", tags=["smoke"])
    tc2 = TestCase("test_login_fail", "Checks failed login", priority="high", tags=["smoke"])
    tc3 = TestCase("test_checkout", "Checks checkout flow", priority="medium", tags=["regression"])
    tc4 = TestCase("test_fail_payment", "Checks failed payment", priority="low", tags=["regression"])

    
    tc5 = TestCase.from_dict({
        "name": "test_signup_valid",
        "description": "Checks valid signup",
        "priority": "high",
        "tags": ["smoke"]
    })
    tc6 = TestCase.from_dict({
        "name": "test_fail_logout",
        "description": "Checks failed logout",
        "priority": "medium",
        "tags": ["regression"]
    })

    
    suite = TestSuite(name="Main Suite")
    for tc in [tc1, tc2, tc3, tc4, tc5, tc6]:
        suite.add_test(tc)

    
    print("High priority tests:")
    for test in suite.get_by_priority("high"):
        print(f"  - {test.name}")

    
    runner = TestRunner()
    results = runner.run(suite)

    
    print("\nResults:")
    runner.summary(results)


main()