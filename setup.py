from xml.sax.handler import version
import cx_Freeze

executables = [cx_Freeze.Executable("shootingspacejetgame/__main__.py", shortcut_name='Shooting Space Jet Game', shortcutDir='DesktopFolder')]

cx_Freeze.setup(
    name="Shooting Space Jet Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["shootingspacejetgame/assets/"]}},
    executables = executables,
    version = "1.0.0",
    authors = 'Harkirat Singh (honey.harkirat@outlook.com)',
    description = 'Demonstration project of shooting space jet game.'

    )


# from distutils.core import setup
# from importlib.metadata import entry_points
# # from importlib_metadata import entry_points
# from setuptools import find_packages

# setup(
#     name='ShootingSpaceJetGame',
#     version='1.0',
#     packages=['shootingspacejetgame'],
#     include_package_data=True,
#     license='MIT',
#     author='Harkirat Singh (honey.harkirat@outlook.com)',
#     install_requires=["pygame"],
#     long_description=open('README.md').read(),
#     entry_points = {
#         'distutils.commands': [
#             'my_command = shootingspacejetgame.__main__:entry_point' 
#         ]
#     }
# )
