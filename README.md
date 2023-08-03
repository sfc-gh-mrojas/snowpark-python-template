# Python Project Template for Snowpark

Use this template to start writing data applications on Snowflake using Python.

## Setup

Set the following environment variables with your Snowflake account information:

```bash
# Linux/MacOS
export SNOWSQL_ACCOUNT=<replace with your account identifer>
export SNOWSQL_USER=<replace with your username>
export SNOWSQL_PWD=<replace with your password>
export SNOWSQL_DATABASE=<replace with your database>
export SNOWSQL_SCHEMA=<replace with your schema>
export SNOWSQL_WAREHOUSE=<replace with your warehouse>
```

```powershell
# Windows/PowerShell
$env:SNOWSQL_ACCOUNT = "<replace with your account identifer>"
$env:SNOWSQL_USER = "<replace with your username>"
$env:SNOWSQL_PWD = "<replace with your password>"
$env:SNOWSQL_DATABASE = "<replace with your database>"
$env:SNOWSQL_SCHEMA = "<replace with your schema>"
$env:SNOWSQL_WAREHOUSE = "<replace with your warehouse>"
```


Optional: You can set this env var permanently by editing your bash profile (on Linux/MacOS) or 
using the System Properties menu (on Windows).

### Install dependencies

Create and activate a conda environment using [Anaconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands):

```bash
conda env create --file environment.yml
conda activate snowpark
```

### Configure IDE

#### VS Code

Press `Ctrl`+`Shift`+`P` to open the command palette, then select **Python: Select Interpreter** and select the **snowpark** interpeter under the **Conda** list.

> NOTE: VS Code is a very customizable IDE. Under the `.vscode` folder you can find some files like (.settings.json, launch.json) those files can use to setup the VSCode terminal, debugger and other IDE settings. See https://code.visualstudio.com/docs/python/environments for more details. 

#### PyCharm

Go to **File** > **Settings** > **Project** > **Python Interpreter** and select the snowpark interpreter.

## Prereqs

To develop your applications locally, you will need

- A Snowflake account
- Python 3.8
- An IDE or code editor (VS Code, PyCharm, etc.)

## Usage

Once you've set your credentials and installed the packages, you can test your connection to Snowflake by executing the stored procedure in [`app.py`](src/procs/app.py):

```bash
python src/procs/app.py
```

You should see the following output:

```
------------------------------------------------------
|Hello world                                         |
------------------------------------------------------
|Welcome to Snowflake!                               |
|Learn more: https://www.snowflake.com/snowpark/     |
------------------------------------------------------
```

### Run tests

You can run the test suite locally from the project root:

```bash
python -m pytest
```

### Packaging your application for deployment

Snowpark allows you to package your application as a zip for deployment. A simple way to package your app will be:
```
python setup.py bdist_wheel
for file in dist/*.whl; do mv -- "$file" "${file%.whl}.zip"; done
```

On Windows Command Prompt:
```
python setup.py bdist_wheel
for %i in (dist\*.whl) do ren "%i" "%~ni.zip"
```
Now your code is ready to be upload into an stage

### Deploy to Snowflake

The GitHub Actions [workflow file](.github/workflows/build-and-deploy.yml) allows you to continously deploy your objects to Snowflake. When you're ready,
create secrets in your GitHub repository with the same name and values as the environment variables you created earler (`SNOWSQL_PWD`, `SNOWSQL_ACCOUNT`, etc.). The workflow will create a stage, upload the Python source code, and create the stored procedure object. For more information, see [`resources.sql`](resources.sql).



## Project Structure

- [procs/](src/procs/): Directory for stored procedures
- [udf/](src/udf/): Directory for your user-defined functions
- [util/](src/util/): Directory for methods/classes shared between UDFs and procedures

## Docs

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
- [Creating Stored Procedures](https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-sprocs)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/index.html)

## Contributing

Have a question or ran into a bug? Please [file an issue](https://github.com/Snowflake-Labs/snowpark-python-template/issues/new) and let us know.

Have an idea for an improvement? Fork this repository and open a PR with your idea!
