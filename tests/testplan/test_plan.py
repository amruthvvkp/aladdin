import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest

from integration_tests.dummy_test import DummyIntegrationTest
from regression_tests.dummy_test import DummyRegressionTest


@test_plan(name='Aladdin')
def main(plan):
    plan.add(MultiTest(
        name="IntegrationTests",
        suites=[DummyIntegrationTest()],
    ))
    plan.add(MultiTest(
        name="RegressionTests",
        suites=[DummyRegressionTest()],
    ))


if __name__ == "__main__":
    sys.exit(main().exit_code)
