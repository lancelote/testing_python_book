"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh
from paver.setuputils import setup, find_package_data


package_data = find_package_data()
entry_points = {
    'console_scripts': [
        'run_server = bank.bank.bank_app:main',
    ]
}


setup(name='bank_app',
      version='0.0.1',
      author='Pavel Karateev',
      maintainer='Pavel Karateev',
      description='Example application to demonstrate'
                  'Python testing techniques.',
      license='License :: Public Domain',
      include_package_data=True,
      packages=['bank'],
      package_data=package_data,
      entry_points=entry_points)


@task
@needs('paver.misctasks.generate_setup', 'distutils.command.sdist')
def sdist():
    """
    Generates the setup file and packages up the
    commercial_inventory application.
    """


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
