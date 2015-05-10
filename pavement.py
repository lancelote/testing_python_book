"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def unit_tests():
    """
    Run unittests
    """
    sh("py.test bank/ bank/test/unit/")


@task
def behave_test():
    """
    BDD testing
    """
    sh("behave bank/test/bdd/features/")


@needs('unit_tests', 'behave_test')
@task
def default():
    """
    Default test runner
    """
    pass