### Installation and assembly instructions

To successfully install and build the project, make sure that you have the following versions of Python and pip installed:

- Python == 3.8-3.12
- pip == ^22.3

You can install the necessary dependencies by running the following commands:

- `make install` - install project dependencies.
- `make build` - build the project.
- `make package-install` - install the assembled package.

## How to use

- `gendiff --format json`
The result will be displayed in the console, and will also be saved in files in a directory named data.

If the package is in the sisyphus branch, but it is not in the p10 branch, it is assigned the value: "only sisyphus".

If the package is in the p10 branch, but it is not in the sisyphus branch, it is assigned the value: "only p10".

If there are packages in both branches, but they have different versions, the value is assigned: "different versions".

If packages are present in both branches and they have the same versions, the value "unchanged" is assigned.