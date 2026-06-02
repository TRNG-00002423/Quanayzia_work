def format_test_name(name):
    """Convert a human-readable name to a test function name.

    Example:
        format_test_name("Valid Login") → "test_valid_login"
        format_test_name("  Search Results Page  ") → "test_search_results_page"

    Rules:
        - Lowercase
        - Spaces replaced with underscores
        - Leading/trailing whitespace stripped
        - Prefixed with "test_"
    """
    return  "test_" + name.strip().lower().replace(" ", "_")


def is_valid_test_name(name):
    """Check if a string is a valid test function name.

    Rules:
        - Must start with "test_"
        - Must contain only lowercase letters, digits, and underscores
        - Must be at least 6 characters (e.g., "test_x")

    Returns: bool
    """
    name=name.strip()
    return (
        name.startswith("test_")
        and name.islower()
        and len(name) >= 6
        and all(c.isalnum() or c == "_" for c in name))


assert format_test_name("Valid Login") == "test_valid_login"
assert format_test_name("  Search Results  ") == "test_search_results"
assert is_valid_test_name("test_login") == True
assert is_valid_test_name("login_test") == False
assert is_valid_test_name("test_") == False



### TASK 2

def create_test_result(name, status="pass", duration_ms=0, error=None):
    """Create a test result dictionary.

    Args:
        name: Test name (required)
        status: "pass" or "fail" (default: "pass")
        duration_ms: Execution time in ms (default: 0)
        error: Error message if failed (default: None)

    Returns:
        dict with keys: name, status, duration_ms, error
    """
    return { "name":name, "status": status, "duration_ms": duration_ms, "error": error}


def format_duration(ms, unit="ms"):
    """Format a duration value with the specified unit.

    Args:
        ms: Duration in milliseconds
        unit: "ms", "s", or "min" (default: "ms")

    Returns:
        Formatted string like "1,200ms" or "1.20s" or "0.02min"
    """
    if unit == "ms":
        return f"{ms:,}ms"

    elif unit == "s":
        seconds = ms / 1000
        return f"{seconds:.2f}s"

    elif unit == "min":
        minutes = ms / 60000
        return f"{minutes:.2f}min"

    else:
        raise ValueError("Invalid unit. Use 'ms', 's', or 'min'.")
    

r1 = create_test_result("test_login")
assert r1 == {"name": "test_login", "status": "pass", "duration_ms": 0, "error": None}

r2 = create_test_result("test_checkout", status="fail", duration_ms=2300, error="Timeout")
assert r2["status"] == "fail"
assert r2["error"] == "Timeout"

assert format_duration(1200) == "1,200ms"
assert format_duration(1200, "s") == "1.20s"



#Task 3: *args and **kwargs

def calculate_stats(*scores):
    """Calculate statistics for any number of scores.

    Returns:
        dict with keys: count, total, average, min, max

    Raises:
        ValueError if no scores provided
    """
    if not scores:
        raise ValueError("No score was provided")

    return {
        "count": len(scores),
        "total": sum(scores),
        "average": sum(scores) / len(scores),
        "min": min(scores),
        "max": max(scores)
    }


def build_test_config(**settings):
    """Build a test configuration with defaults.

    Default config:
        browser: "chrome"
        headless: False
        timeout: 30
        retries: 0
        base_url: "http://localhost:3000"

    Any **settings passed override the defaults.

    Returns: dict
    """

    config={
    "browser": "chrome",
    "headless": False,
    "timeout": 30,
    "retries": 0,
    "base_url": "http://localhost:3000"
    
}
    
    config.update(settings)

    return config


stats = calculate_stats(85, 92, 78, 95, 88)
assert stats["count"] == 5
assert stats["average"] == 87.6
assert stats["min"] == 78
assert stats["max"] == 95

config = build_test_config(headless=True, timeout=60)
assert config["browser"] == "chrome"  # default
assert config["headless"] == True     # overridden
assert config["timeout"] == 60       # overridden



#4.Task 4: Multiple Return Values & Composition 

def analyze_results(*results):
    """Analyze a list of test result dicts.

    Args:
        *results: test result dicts (from create_test_result)

    Returns:
        tuple of (passed_count, failed_count, pass_rate, avg_duration)
    """

    passed_count = 0
    failed_count = 0
    total_duration = 0

    for result in results:
        if result["status"] == "pass":
            passed_count += 1
        else:
            failed_count += 1

        total_duration += result["duration_ms"]

    total = len(results)
    pass_rate = passed_count / total
    avg_duration = pass_rate = (passed_count / total) * 100

    return (passed_count, failed_count, pass_rate, avg_duration)


def generate_report(*results):
    """Generate a formatted test report string.

    Calls analyze_results() internally and formats the output.

    Returns: formatted multi-line string
    """
    passed, failed, pass_rate, avg_duration = analyze_results(*results) # unpack the tuple using *

    return (
    f"Passed: {passed}\n"
    f"Failed: {failed}\n"
    f"Pass Rate: {pass_rate:.1f}%\n"
    f"Average Duration: {avg_duration:.2f}ms"
)


results = [
    create_test_result("test_login", "pass", 1200),
    create_test_result("test_search", "pass", 850),
    create_test_result("test_checkout", "fail", 2300, "Timeout"),
    create_test_result("test_profile", "pass", 450),
]

passed, failed, rate, avg = analyze_results(*results)
assert passed == 3
assert failed == 1
assert rate == 75.0

