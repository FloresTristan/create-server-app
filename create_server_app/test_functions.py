import os


def create_test_functions_file(project_name):
    test_content = """import pytest
import AppConfig

def test_env():
    env = AppConfig.Environment()
    assert env.getEnvironment() in [
        'localdev', 'localprod', 'clouddev', 'cloudprod', 'localTest', 'cloudTest'
    ]

if __name__ == '__main__':
    if AppConfig().getIsProductionEnvironment():
        raise Exception("Cannot run tests in production environment.")
        
    #INSERT FUNCTIONS BELOW#

"""
    with open(os.path.join(project_name, 'test_functions.py'), 'w') as f:
        f.write(test_content)
