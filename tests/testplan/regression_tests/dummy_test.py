from testplan.testing.multitest import testsuite, testcase


@testsuite
class DummyRegressionTest:

    @testcase
    def dummy_test(self, env, result):
        result.equal(1, 1, 'Check if 1==1')
